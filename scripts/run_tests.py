import sys
from pathlib import Path
import inspect

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
TESTS_PATH = PROJECT_ROOT / "tests"

sys.path.insert(0, str(SRC_PATH))
sys.path.insert(0, str(TESTS_PATH))

import test_validation
import test_workflow_simulator

def run_module_tests(module):
    passed = 0
    failed = 0
    for name, obj in inspect.getmembers(module):
        if name.startswith("test_") and callable(obj):
            try:
                obj()
                print(f"  [PASS] {name}")
                passed += 1
            except Exception as e:
                print(f"  [FAIL] {name}: {e}")
                failed += 1
    return passed, failed

def main():
    print("Executando testes do Delivery AI Assistant...")
    print("\nTestes de validação:")
    p1, f1 = run_module_tests(test_validation)
    print("\nTestes do simulador de workflow:")
    p2, f2 = run_module_tests(test_workflow_simulator)
    
    total_passed = p1 + p2
    total_failed = f1 + f2
    print(f"\nResumo: {total_passed} passaram, {total_failed} falharam.")
    if total_failed > 0:
        sys.exit(1)
    print("Todos os testes passaram com sucesso!")

if __name__ == "__main__":
    main()
