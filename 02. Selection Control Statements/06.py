# Nested if means if inside another if

age = int(input("Enter your age: "))
if age > 18:
    print("Adult")
    if age > 60:
        print("Senior citizen")

