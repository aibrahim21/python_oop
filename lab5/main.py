from classes import *

from classes import *

# Create Samy's car
fiat = Car(name="Fiat 128", fuelRate=100, velocity=60)

# Create Samy
samy = Employee(
    name="Samy", money=2000, mood="happy", healthRate=100,
    emp_id=1, car=fiat, email="samy@iti.com", salary=3000,
    distanceToWork=20
)

# Create ITI Office
iti_office = Office("ITI Smart Village")
iti_office.hire(samy)

# Simulate going to work
samy.drive(distance=20, velocity=60)
iti_office.check_lateness(emp_id=1, moveHour=7.5)

