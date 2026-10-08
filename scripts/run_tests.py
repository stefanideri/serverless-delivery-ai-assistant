import importlib.util
import inspect
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"
TESTS_PATH = PROJECT_ROOT / "tests"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))


def load_module_from_file(module_name: str, file_path: Path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Não foi possível carregar {file_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


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
    test_validation = load_module_from_file("test_validation", TESTS_PATH / "test_validation.py")
    test_workflow_simulator = load_module_from_file("test_workflow_simulator", TESTS_PATH / "test_workflow_simulator.py")

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
