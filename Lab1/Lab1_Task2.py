first_num, second_num = int(input("Введите первое число: ")), int(input("Введите второе число: "))
if first_num == second_num:
    print("Они идентичные")
else:
    print("Большее число:", max(first_num, second_num))