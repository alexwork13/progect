try:
    x = int(input("Enter number: "))
    print(5/x)
except ZeroDivisionError: # указываем тип исключения
    print("Error dividing by zero")
except ValueError as z:
    print(z)