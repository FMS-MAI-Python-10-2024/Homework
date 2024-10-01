import os
import unittest
import importlib.util
from unittest.mock import patch


class TestVariant0(unittest.TestCase):
    def run_tests_for_student(self, student_name):
        solution_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../tasks/{student_name}.py'))

        if not os.path.exists(solution_file):
            self.fail(f"Solution file not found: {solution_file}")

        print(f"Solution file found: {solution_file}, running tests...")

        spec = importlib.util.spec_from_file_location(student_name, solution_file)
        student_solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_solution_module)

        test_cases = [
            ("1 2", "Пикай Хорька!"),
            ("1 10", "Каждый дуб когда был жёлудём..."),
            ("100 1", "One shot - one kill."),
            ("999 2", "Хафизов нехороший человек.")
        ]

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

        solution_file = os.path.abspath(student_file)

        if os.path.exists(solution_file):
            self.run_tests_for_student(student_name)
        else:
            self.fail(f"Test skipped: no file {solution_file} found.")


if __name__ == '__main__':
    unittest.main()