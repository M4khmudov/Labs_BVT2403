def great(name):
    print("Привет,", name)

def square(number):
    return number ** 2

def max_of_two(x, y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return "Они идентичны"
print(max_of_two(int(input("Введите первое число: ")), int(input("Введите второе число: "))))