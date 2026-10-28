import unittest

from variant_10 import Director, Employee, SeniorEmployee


class EmployeeTests(unittest.TestCase):
    def test_calculate_bonus(self):
        employee = Employee(hours=160, rate=500, bonus_coefficient=0.2)

        self.assertEqual(employee.calculate_bonus(), 16_000)

    def test_accepts_zero_rate_and_bonus_coefficient(self):
        employee = Employee(hours=160, rate=0, bonus_coefficient=0)

        self.assertEqual(employee.calculate_bonus(), 0)

    def test_rejects_invalid_pay_data(self):
        invalid_arguments = (
            {"hours": 0, "rate": 500, "bonus_coefficient": 0.2},
            {"hours": -1, "rate": 500, "bonus_coefficient": 0.2},
            {"hours": 160, "rate": -1, "bonus_coefficient": 0.2},
            {"hours": 160, "rate": 500, "bonus_coefficient": -0.1},
        )

        for arguments in invalid_arguments:
            with self.subTest(arguments=arguments):
                with self.assertRaises(ValueError):
                    Employee(**arguments)

    def test_senior_employee_uses_inherited_data_and_has_specialization(self):
        employee = SeniorEmployee(160, 500, 0.2, specialization="Backend")

        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.specialization, "Backend")
        self.assertEqual(employee.salary_per_hour(), 600)

    def test_director_uses_inherited_data_and_has_department(self):
        director = Director(200, 1_000, 0.5, department="Development")

        self.assertIsInstance(director, Employee)
        self.assertEqual(director.department, "Development")
        self.assertEqual(director.salary_per_hour(), 1_500)

    def test_equal_objects_of_the_same_exact_class(self):
        first = SeniorEmployee(160, 500, 0.2, "Backend")
        second = SeniorEmployee(160, 500, 0.2, "Backend")
        different = SeniorEmployee(160, 500, 0.2, "Frontend")

        self.assertEqual(first, second)
        self.assertNotEqual(first, different)

    def test_equality_returns_not_implemented_for_different_classes(self):
        employee = Employee(160, 500, 0.2)
        senior = SeniorEmployee(160, 500, 0.2, "Backend")

        self.assertIs(employee.__eq__(senior), NotImplemented)
        self.assertIs(senior.__eq__(employee), NotImplemented)
        self.assertNotEqual(employee, senior)


if __name__ == "__main__":
    unittest.main()
