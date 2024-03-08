class Tasks:
    def __init__(self):
        pass

    # Task 1: Ask for name, surname, and age, then create a sentence with this information.
    def get_info_and_create_sentence(self):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        age = input("Enter your age: ")
        print(f"{name} {surname} is {age} years old.")

    # Task 2: Convert temperature from Celsius to Fahrenheit.
    def celsius_to_fahrenheit(self):
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")

    # Task 3: Reverse to change Fahrenheit to Celsius.
    def fahrenheit_to_celsius(self):
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")

    # Task 4: Convert to the Polish grading system and add the grade to consist of 3 elements.
    def convert_to_polish_grade(self):
        score = float(input("Enter your score: "))
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print("Your grade is:", grade)

    # Task 5: Change the code so that there are two inputs and the first number is separated by the second.
    def check_number_even_or_odd(self):
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
        if number1 % number2 == 0:
            result = "Even"
        else:
            result = "Odd"
        print("The number is:", result)

    # Task 6: Add a check to see if a triangle can be drawn with the given sides.
    def check_triangle_type(self):
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))
        if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
            if side1 == side2 == side3:
                triangle_type = "Equilateral"
            elif side1 == side2 or side1 == side3 or side2 == side3:
                triangle_type = "Isosceles"
            else:
                triangle_type = "Scalene"
            print("The triangle is:", triangle_type)
        else:
            print("These side lengths cannot form a triangle.")

    # Task 7: Add a check to see if someone is trying to divide by zero, if so, give an appropriate message.
    def perform_operation(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error! Division by zero.")
                return
            result = num1 / num2
        else:
            result = "Invalid operation"
        print("Result:", result)


tasks = Tasks()
tasks.get_info_and_create_sentence()
tasks.celsius_to_fahrenheit()
tasks.fahrenheit_to_celsius()
tasks.convert_to_polish_grade()
tasks.check_number_even_or_odd()
tasks.check_triangle_type()
tasks.perform_operation()
