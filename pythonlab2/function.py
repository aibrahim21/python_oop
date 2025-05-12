import math

def calc_area(*arg):
    if arg[0] in ('triangle', 't','tri'):
        return 0.5*arg[1]*arg[2]
    elif arg[0] in ('circle','c','cir'):
        return math.pi*arg[1]**2  # Fixed circle area formula
    elif arg[0] in ('rectangle','rec','r'):
        return arg[1]*arg[2]
    elif arg[0] in ('square','sqr','s'):
        return arg[1]*arg[1]
    else:
        print("Please enter a correct shape")
        exit()

shape_data = {
    'triangle': {'aliases': ['triangle', 't', 'tri'], 'params': 2},
    'circle': {'aliases': ['circle', 'c', 'cir'], 'params': 1},
    'rectangle': {'aliases': ['rectangle', 'rec', 'r'], 'params': 2},
    'square': {'aliases': ['square', 'sqr', 's'], 'params': 1}
}

# Get shape input
shape_input = input("Enter type of shape: ").lower().strip()  # Added strip() to remove whitespace

# Find matching shape
matched_shape = None
param_count = 0
for shape, data in shape_data.items():
    if shape_input in data['aliases']:
        matched_shape = shape_input
        param_count = data['params']
        break

if matched_shape is None:  # Moved this check outside the loop
    print("You didn't enter a valid shape")
    exit()

# Get dimensions
dimensions = []
for i in range(1, param_count + 1):
    while True:
        value = input(f"Enter dimension #{i}: ").strip()
        
        # Check if input consists only of digits and at most one decimal point
        if value.isdecimal():
            value = float(value)
            if value > 0:
                dimensions.append(value)
                break
            else:
                print("Please enter a positive number")
        else:
            print("Please enter a valid positive number")

# Calculate and display area
area = calc_area(matched_shape, *dimensions)
print(f"The area is: {round(area,2)}")