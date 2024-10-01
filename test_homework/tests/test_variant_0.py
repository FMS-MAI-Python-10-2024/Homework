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
            (("1", "2"), "Пикай Хорька!"),
            (("1", "10"), "Каждый дуб когда был жёлудём..."),
            (("100", "1"), "One shot - one kill."),
            (("999", "2"), "Хафизов нехороший человек.")
        ]

        success_count = 0
        total_tests = len(test_cases)

        for input_data, expected_output in test_cases:
            with patch('builtins.input', side_effect=input_data), patch('builtins.print') as mock_print:
                try:
                    if hasattr(student_solution_module, 'student_solution'):
                        student_solution_module.student_solution()
                    else:
                        exec(open(solution_file).read())
                    mock_print.assert_called_with(expected_output)
                    success_count += 1
                except AssertionError:
                    print(
                        f"Test {success_count + 1}/{total_tests} failed for input: {input_data}. Expected: {expected_output}. Got: {mock_print.call_args[0][0]}")

        print(f"Results: {success_count}/{total_tests} tests passed.")

    def test_student_solution(self):
        student_file = os.getenv("STUDENT_FILE")
        if not student_file:
            self.skipTest("No student file specified")

        student_name = os.path.basename(student_file).replace(".py", "")

        tasks_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tasks'))

        if student_file in os.listdir(tasks_folder):
            self.run_tests_for_student(student_name)
        else:
            self.fail(f"Test skipped: no file {student_file} found in tasks folder.")


if __name__ == '__main__':
    unittest.main()


# a, b = map(int, input().split())
# summ = a + b
#
# if summ <= 10:
#     print("Пикай Хорька!")
# elif 10 < summ <= 100:
#     print("Каждый дуб когда был жёлудём...")
# elif 100 < summ <= 1000:
#     print("One shot - one kill.")
# else:
#     print("Хафизов нехороший человек.")

# a, b = map(int, input().split())
# summ = a + b
#
# if summ <= 10:
#     print("Пdghfdgfикай Хорька!")
# elif 10 < summ <= 100:
#     print("Кажdgfdjgfjдый дуб когда был жёлудём...")
# elif 100 < summ <= 1000:
#     print("Ondgfdjgfe shot - one kill.")
# else:
#     print("Хафизовdjfdjh нехороший человек.")