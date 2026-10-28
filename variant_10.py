class Employee:
    def __init__(self, hours, rate, bonus_coefficient):
        if hours <= 0:
            raise ValueError("Количество рабочих часов должно быть больше нуля")
        if rate < 0:
            raise ValueError("Ставка не может быть отрицательной")
        if bonus_coefficient < 0:
            raise ValueError("Коэффициент премии не может быть отрицательным")

        self.hours = hours
        self.rate = rate
        self.bonus_coefficient = bonus_coefficient

    def calculate_bonus(self):
        return self.hours * self.rate * self.bonus_coefficient

    def __eq__(self, other):
        if type(self) is not type(other):
            return NotImplemented
        return vars(self) == vars(other)


class SeniorEmployee(Employee):
    def __init__(self, hours, rate, bonus_coefficient, specialization):
        super().__init__(hours, rate, bonus_coefficient)
        self.specialization = specialization

    def salary_per_hour(self):
        base_salary = self.hours * self.rate
        return (base_salary + self.calculate_bonus()) / self.hours


class Director(Employee):
    def __init__(self, hours, rate, bonus_coefficient, department):
        super().__init__(hours, rate, bonus_coefficient)
        self.department = department

    def salary_per_hour(self):
        base_salary = self.hours * self.rate
        return (base_salary + self.calculate_bonus()) / self.hours


if __name__ == "__main__":
    employee = Employee(160, 500, 0.2)
    senior = SeniorEmployee(160, 700, 0.3, "Backend")
    director = Director(180, 1_000, 0.5, "Development")
    same_senior = SeniorEmployee(160, 700, 0.3, "Backend")

    print(f"Премия сотрудника: {employee.calculate_bonus()}")
    print(f"Зарплата старшего сотрудника за час: {senior.salary_per_hour()}")
    print(f"Зарплата директора за час: {director.salary_per_hour()}")
    print(f"Старшие сотрудники равны: {senior == same_senior}")
