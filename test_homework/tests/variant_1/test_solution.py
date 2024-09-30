import os
import unittest
import importlib.util


class TestVariant1(unittest.TestCase):
    def run_tests_for_student(self, student_name):
        solution_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), f'../test_homework/tasks/{student_name}.py'))
        if not os.path.exists(solution_file):
            self.fail(f"Solution file not found: {solution_file}")

        spec = importlib.util.spec_from_file_location(student_name, solution_file)
        student_solution_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(student_solution_module)

        self.assertEqual(student_solution_module.student_solution([10, 0]), "Меня буллят...")
        self.assertEqual(student_solution_module.student_solution([90, 1]), "Здоровья Вартумяну.")
        self.assertEqual(student_solution_module.student_solution([1000, 0]), "Где роум?")
        self.assertEqual(student_solution_module.student_solution([1000, 1]), "Хафизов нехороший человек.")

    def test_all_students(self):
        tasks_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../test_homework/tasks'))
        for file in os.listdir(tasks_folder):
            if file.endswith(".py") and "_variant_1" in file:
                student_name = file[:-3]
                with self.subTest(student=student_name):
                    self.run_tests_for_student(student_name)


if __name__ == '__main__':
    unittest.main()
