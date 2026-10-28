class Employee:
    def __init__(self, hours, rate, bonus_coefficient):
        self.hours = hours
        self.rate = rate
        self.bonus_coefficient = bonus_coefficient

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if value <= 0:
            raise ValueError("Количество рабочих часов должно быть больше нуля")
        self._hours = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if value < 0:
            raise ValueError("Ставка не может быть отрицательной")
        self._rate = value

    @property
    def bonus_coefficient(self):
        return self._bonus_coefficient

    @bonus_coefficient.setter
    def bonus_coefficient(self, value):
        if value < 0:
            raise ValueError("Коэффициент премии не может быть отрицательным")
        self._bonus_coefficient = value

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

    @property
    def specialization(self):
        return self._specialization

    @specialization.setter
    def specialization(self, value):
        if not value:
            raise ValueError("Специализация не может быть пустой")
        self._specialization = value

    def salary_per_hour(self):
        base_salary = self.hours * self.rate
        return (base_salary + self.calculate_bonus()) / self.hours


class Director(Employee):
    def __init__(self, hours, rate, bonus_coefficient, department):
        super().__init__(hours, rate, bonus_coefficient)
        self.department = department

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, value):
        if not value:
            raise ValueError("Отдел не может быть пустым")
        self._department = value

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

    employee.rate = 600
    print(f"Премия после повышения ставки: {employee.calculate_bonus()}")
