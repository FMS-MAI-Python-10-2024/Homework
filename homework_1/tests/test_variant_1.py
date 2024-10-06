import os
import json
import random
import unittest
import importlib.util
from pathlib import Path
from unittest.mock import patch


class TestVariant1(unittest.TestCase):
    # Определяем функции выше по коду, чтобы их можно было использовать
    def generate_test_cases(self, solve_func, num_tests=40, input_range=(1, 1000)):
        test_cases = []
        for _ in range(num_tests):
            input_data = self.generate_random_input(input_range)
            expected_output = solve_func(input_data)
            test_cases.append((input_data, expected_output))
        return test_cases

    def generate_random_input(self, input_range):
        num_count = random.randint(input_range[0], input_range[1])
        first_line = ' '.join(str(random.randint(0, 10 ** 5)) for _ in range(num_count))
        second_line = str(random.randint(1, num_count))
        return f"{first_line}\n{second_line}"

    def run_tests_for_student(self, student_name, variant_number):
        student_solution_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../tasks/{student_name}.py'))

        if not os.path.exists(student_solution_file):
            self.fail(f"Solution file not found: {student_solution_file}")

        print(f"Solution file found: {student_solution_file}, running tests...")

        spec = importlib.util.spec_from_file_location(student_name, student_solution_file)
        student_solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_solution_module)

        test_params_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../test_params/params_variant_{variant_number}.json'))

        solve_variant_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../solutions/solve_variant_{variant_number}.py'))

        if not os.path.exists(solve_variant_file):
            self.fail(f"Solve file not found: {solve_variant_file}")

        # Если файла с тестовыми данными нет, создаём его
        if not Path(test_params_file).exists():
            print(f"File {test_params_file} not found, generating new test cases using solve_variant_{variant_number}.")

            # Загрузка решающей функции из solutions
            solve_spec = importlib.util.spec_from_file_location(f"solve_variant_{variant_number}", solve_variant_file)
            solve_module = importlib.util.module_from_spec(solve_spec)
            solve_spec.loader.exec_module(solve_module)

            if not hasattr(solve_module, 'solve'):
                self.fail(f"Module solve_variant_{variant_number} does not have a function 'solve'")

            solve_func = solve_module.solve
            test_cases = self.generate_test_cases(solve_func, num_tests=40, input_range=(1, 1000))

            # Сохраняем сгенерированные тесты в JSON
            with open(test_params_file, 'w') as f:
                json.dump(test_cases, f)
            print(f"Test cases saved to {test_params_file}.")
        else:
            print(f"Loading test cases from {test_params_file}.")
            with open(test_params_file, 'r') as f:
                test_cases = json.load(f)

        # Запуск тестов для решения студента
        self.run_test_cases(student_solution_module, test_cases)

    def run_test_cases(self, student_solution_module, test_cases):
        success_count = 0
        total_tests = len(test_cases)

        if not hasattr(student_solution_module, 'student_solution'):
            self.fail(f"Module does not have a function 'student_solution'")

        for input_data, expected_output in test_cases:
            with patch('builtins.input', side_effect=[input_data]), patch('builtins.print') as mock_print:
                try:
                    student_solution_module.student_solution()
                    printed_output = mock_print.call_args[0][0] if mock_print.call_args else None

                    if printed_output != expected_output:
                        self.fail(
                            f"Test {success_count+1} failed for input: {input_data}. Expected: {expected_output}, but got: {printed_output}")

                    success_count += 1
                except Exception as e:
                    self.fail(f"Test {success_count+1} encountered an error: {e}")

        print(f"Results: {success_count}/{total_tests} tests passed.")

    def test_student_solution(self):
        student_file = os.getenv("STUDENT_FILE")
        if not student_file:
            self.skipTest("No student file specified")

        student_name = os.path.basename(student_file).replace(".py", "")

        # Извлекаем номер варианта из имени файла
        variant_number = student_name.split('_')[-1]

        solution_file = os.path.abspath(student_file)

        if os.path.exists(solution_file):
            self.run_tests_for_student(student_name, variant_number)
        else:
            self.fail(f"Test skipped: no file {solution_file} found.")


if __name__ == '__main__':
    unittest.main()
