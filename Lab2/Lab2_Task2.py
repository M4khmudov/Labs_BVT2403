def is_prime(number):
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
print(is_prime(int(input("Введите число: "))))