import re

# ----------------- Person Class ----------------- #
class Person:
    mood_options = ("happy", "tired", "lazy")

    def __init__(self, name, money, mood="happy", healthRate=100):
        self.name = name
        self.money = money
        self.mood = mood
        self._healthRate = healthRate

    @property
    def healthRate(self):
        return self._healthRate

    @healthRate.setter
    def healthRate(self, value):
        if 0 <= value <= 100:
            self._healthRate = value
        else:
            raise ValueError("Health rate must be between 0 and 100.")

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            self.healthRate = 0

    def buy(self, items):
        self.money -= items * 10


# ----------------- Car Class ----------------- #
class Car:
    def __init__(self, name, fuelRate=100, velocity=0):
        self.name = name
        self._fuelRate = fuelRate
        self._velocity = velocity

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = max(0, min(value, 100))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            raise ValueError("Velocity must be between 0 and 200.")

    def run(self, velocity, distance):
        self.velocity = velocity
        fuel_needed = (distance / 10) * 10
        if self.fuelRate >= fuel_needed:
            self.fuelRate -= fuel_needed
            self.stop(0)
        else:
            distance_possible = (self.fuelRate / 10) * 10
            self.fuelRate = 0
            self.stop(distance - distance_possible)

    def stop(self, remain_distance):
        self.velocity = 0
        if remain_distance == 0:
            print("You reached your destination.")
        else:
            print(f"You stopped with {remain_distance} km left due to no fuel.")


# ----------------- Employee Class ----------------- #
class Employee(Person):
    def __init__(self, name, money, mood, healthRate, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if re.match(r"[^@]+@[^@]+\.[^@]+", value):
            self._email = value
        else:
            raise ValueError("Invalid email address.")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 1000:
            self._salary = value
        else:
            raise ValueError("Salary must be at least 1000.")

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        self.car.run(velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, msg, receiver_name):
        with open("email.txt", "w") as f:
            f.write(f"From: {self.email}\n")
            f.write(f"To: {to}\n\n")
            f.write(f"Hi, {receiver_name}\n\n")
            f.write(f"{msg}\n\n")
            f.write(f"{subject}")


# ----------------- Office Class ----------------- #
class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            Office.employeesNum -= 1

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= deduction

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward

    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if emp:
            is_late = Office.calculate_lateness(9, moveHour, emp.distanceToWork, emp.car.velocity)
            if is_late:
                self.deduct(emp.id, 10)
            else:
                self.reward(emp.id, 10)

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num


