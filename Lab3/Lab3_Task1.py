def read_txt(type):
    if type == "целиком":
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
    if type == "по строчно":
        with open('example.txt', 'r') as file:
            for line in file:
                print(line)
read_txt(input("""Введите тип ввода: Целиком или По строчно
>>> """).lower())