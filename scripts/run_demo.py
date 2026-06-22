import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

from delivery_ai_assistant.workflow_simulator import simulate_delivery_workflow


def main() -> int:
    if len(sys.argv) != 2:
        print("Uso: python scripts/run_demo.py examples/order-approved.json")
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.is_absolute():
        input_path = PROJECT_ROOT / input_path

    with input_path.open("r", encoding="utf-8") as file:
        order_data = json.load(file)

    result = simulate_delivery_workflow(order_data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

