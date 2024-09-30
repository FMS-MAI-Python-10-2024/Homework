import os
import unittest
import importlib.util


class TestVariant(unittest.TestCase):
    def run_tests_for_student(self, student_name):
        solution_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../tasks/{student_name}.py'))

        if not os.path.exists(solution_file):
            self.fail(f"Solution file not found: {solution_file}")

        spec = importlib.util.spec_from_file_location(student_name, solution_file)
        student_solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_solution_module)

        self.assertEqual(student_solution_module.student_solution([1, 2]), "Пикай Хорька!")
        self.assertEqual(student_solution_module.student_solution([1, 10]), "Каждый дуб когда был жёлудём...")
        self.assertEqual(student_solution_module.student_solution([100, 1]), "One shot - one kill.")
        self.assertEqual(student_solution_module.student_solution([999, 2]), "Хафизов нехороший человек.")

    def test_all_students(self):
        tasks_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tasks'))
        for file in os.listdir(tasks_folder):
            if file.endswith(".py") and "_variant_0" in file:
                student_name = file[:-3]  # удаляем расширение .py
                with self.subTest(student=student_name):
                    self.run_tests_for_student(student_name)


if __name__ == '__main__':
    unittest.main()
