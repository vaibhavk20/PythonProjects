def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mul(x, y):
    return x*y


def div(x, y):
    return x/y


print("Select option")
print("1.Addition")
print("2.subtraction")
print("3.multiplication")
print("4.Division")
choice = int(input("Enter choice :"))
num1 = int(input("Enter the first value"))
num2 = int(input("Enter the second value"))

if choice == 1:
    print("Addition of {} and {} is :{}".format(num1, num2, add(num1, num2)))
elif choice == 2:
    print("Subtraction of {} and {} is :{}".format(num1, num2, sub(num1, num2)))
elif choice == 3:
    print("Multiplication of {} and {} is :{}", mul(num1, num2))
elif choice == 4:
    print("Division of {} and {} is :{}", div(num1, num2))
else:
    print("Enter the valid choice ")
