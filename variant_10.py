from types import NotImplementedType


class Employee:
    def __init__(self, hours: int, rate: int, bonus_coefficient: float):
        self.hours = hours
        self.rate = rate
        self.bonus_coefficient = bonus_coefficient

    @property
    def hours(self) -> int:
        return self._hours

    @hours.setter
    def hours(self, value: int) -> None:
        if value <= 0:
            raise ValueError("Количество рабочих часов должно быть больше нуля")
        self._hours = value

    @property
    def rate(self) -> int:
        return self._rate

    @rate.setter
    def rate(self, value: int) -> None:
        if value < 0:
            raise ValueError("Ставка не может быть отрицательной")
        self._rate = value

    @property
    def bonus_coefficient(self) -> float:
        return self._bonus_coefficient

    @bonus_coefficient.setter
    def bonus_coefficient(self, value: float) -> None:
        if value < 0:
            raise ValueError("Коэффициент премии не может быть отрицательным")
        self._bonus_coefficient = value

    def calculate_bonus(self) -> float:
        return self.hours * self.rate * self.bonus_coefficient

    def __eq__(self, other) -> bool | NotImplementedType:
        if type(self) is not type(other):
            return NotImplemented
        return vars(self) == vars(other)


class SeniorEmployee(Employee):
    def __init__(self, hours: int, rate: int, bonus_coefficient: float, specialization: str):
        super().__init__(hours, rate, bonus_coefficient)
        self.specialization = specialization

    @property
    def specialization(self) -> str:
        return self._specialization

    @specialization.setter
    def specialization(self, value: str) -> None:
        if not value:
            raise ValueError("Специализация не может быть пустой")
        self._specialization = value

    def salary_per_hour(self) -> float:
        base_salary = self.hours * self.rate
        return (base_salary + self.calculate_bonus()) / self.hours


class Director(Employee):
    def __init__(self, hours: int, rate: int, bonus_coefficient: float, department: str):
        super().__init__(hours, rate, bonus_coefficient)
        self.department = department

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        if not value:
            raise ValueError("Отдел не может быть пустым")
        self._department = value

    def salary_per_hour(self) -> float:
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
