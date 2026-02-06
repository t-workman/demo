import math

print("Menu of things you can do:\n")

print("\tadd\n\tsubtract\n\tmultiply\n\tdivide\n\tfloored division\n\tmod\n\tpower\n\tsquare root\n\tcosine\n\ttangent\n")

user_input = input("What would you like to do? ")

if user_input == "add":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} + {second_num} = {first_num + second_num:.2f}")
elif user_input == "subtract":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} - {second_num} = {first_num - second_num:.2f}")
elif user_input == "multiply":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} * {second_num} = {first_num * second_num:.2f}")
elif user_input == "divide":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} / {second_num} = {first_num / second_num:.2f}")
elif user_input == "floored division":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} // {second_num} = {first_num // second_num:.2f}")
elif user_input == "mod":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} % {second_num} = {first_num % second_num:.2f}")
elif user_input == "power":
    first_num = int(input("Enter the first num:"))
    second_num = int(input("Enter the second num:"))
    print(f"{first_num} ** {second_num} = {first_num ** second_num:.2f}")
elif user_input == "square root":
    first_num = int(input("Enter the num:"))
    print(f"The square root of {first_num} = {math.sqrt(first_num):.2f}")
elif user_input == "cosine":
    first_num = int(input("Enter the num:"))
    print(f"The cosine of {first_num} = {math.cos(first_num):.2f}")
elif user_input == "tangent":
    first_num = int(input("Enter the num:"))
    print(f"The tangent of {first_num} = {math.tan(first_num):.2f}")
else:
    print("I dont know how to do", user_input, "sorry.")

