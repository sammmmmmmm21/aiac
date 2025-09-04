import unittest
from task_2 import assign_grade


class TestAssignGrade(unittest.TestCase):
    def test_grade_a(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(95), "A")
        self.assertEqual(assign_grade(100), "A")

    def test_grade_b(self):
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(85), "B")
        self.assertEqual(assign_grade(89), "B")

    def test_grade_c(self):
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(79), "C")

    def test_grade_d(self):
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(65), "D")
        self.assertEqual(assign_grade(69), "D")

    def test_grade_f(self):
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(30), "F")
        self.assertEqual(assign_grade(59), "F")

    def test_boundary_values(self):
        self.assertEqual(assign_grade(89.99), "B")
        self.assertEqual(assign_grade(79.99), "C")
        self.assertEqual(assign_grade(69.99), "D")
        self.assertEqual(assign_grade(59.99), "F")
        self.assertEqual(assign_grade(59.5), "F")
        self.assertEqual(assign_grade(60.0), "D")
        self.assertEqual(assign_grade(69.0), "D")
        self.assertEqual(assign_grade(70.0), "C")
        self.assertEqual(assign_grade(79.0), "C")
        self.assertEqual(assign_grade(80.0), "B")
        self.assertEqual(assign_grade(89.0), "B")
        self.assertEqual(assign_grade(90.0), "A")
        self.assertEqual(assign_grade(100.0), "A")

    def test_invalid_inputs(self):
        self.assertEqual(assign_grade(-5), "Invalid input")
        self.assertEqual(assign_grade(105), "Invalid input")
        self.assertEqual(assign_grade("eighty"), "Invalid input")
        self.assertEqual(assign_grade(None), "Invalid input")
        self.assertEqual(assign_grade([90]), "Invalid input")
        self.assertEqual(assign_grade({}), "Invalid input")


if __name__ == "__main__":
    unittest.main()


