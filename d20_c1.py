def gmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
gmean(num1, num2)


def greater(a, b):
    if a > b:
        print("First is greater")
    elif a < b:
        print("Second is greater")
    else:
        print("Equals")


num3 = int(input("Enter num1: "))
num4 = int(input("Enter num2: "))
greater(num3, num4)
