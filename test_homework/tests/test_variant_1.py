import os
import unittest
import importlib.util
from unittest.mock import patch


class TestVariant1(unittest.TestCase):
    def run_tests_for_student(self, student_name):
        solution_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../tasks/{student_name}.py'))

        if not os.path.exists(solution_file):
            self.fail(f"Solution file not found: {solution_file}")

        spec = importlib.util.spec_from_file_location(student_name, solution_file)
        student_solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_solution_module)

        test_cases = [
            (("10", "0"), "Меня буллят..."),
            (("90", "1"), "Здоровья Вартумяну."),
            (("1000", "0"), "Где роум?"),
            (("1000", "1"), "Хафизов нехороший человек.")
        ]

        for input_data, expected_output in test_cases:
            with patch('builtins.input', side_effect=input_data), patch('builtins.print') as mock_print:
                student_solution_module.student_solution()
                mock_print.assert_called_with(expected_output)

    def test_student_solution(self, student_name):
        tasks_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tasks'))

        student_file = f"{student_name}.py"
        if student_file in os.listdir(tasks_folder):
            self.run_tests_for_student(student_name)
        else:
            self.skipTest(f"Skipped tests for {student_name}: not this variant.")


if __name__ == '__main__':
    unittest.main()
