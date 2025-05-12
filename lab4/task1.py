class Human:
 #human has name, age ,gender and can speak walk and eat
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def speak(self, message):
        print(f"{self.name} says: {message}")

    def walk(self, distance):
        print(f"{self.name} walked {distance} meters")

    def eat(self, food):
        print(f"{self.name} is eating {food}")


# Employee Class
class Employee:
    #employee has name, position,salary and can eat , work
    def __init__(self, name, position, salary):
        # Human attributes
        self.name = name
        self.position = position
        self.salary = salary

    def eat(self, food):  # Fixed: Added 'self' parameter
        print(f"{self.name} is eating {food}")

    def work(self, task):  # Fixed: Added 'self' parameter
        print(f"{self.name} is working on: {task}")

# Instances

person1 = Human(name="Nora", age=28, gender="female")
emp1 = Employee(name="James", position='driver', salary=6500)


person1.speak("Hello!")
emp1.work("delivery route")