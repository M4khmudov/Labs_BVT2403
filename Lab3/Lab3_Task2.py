text = input("Введите текст, который хотите ввести в файл: ")
with open("user_input.txt", "a") as file:
    file.write("\n" + text)