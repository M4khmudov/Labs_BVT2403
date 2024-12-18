class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self):
        if input("Введите ваш предыдущий пароль: ") == self.__password:
            self.__password = input("Введите новый пароль: ")
            print("пароль успешно изменён")
        else:
            print("Пароль неверный, попробуйте ещё раз")
            UserAccount.set_password(self)
    def check_password(self):
        if input("Введите пароль: ") == self.__password:
            print(True)
        else:
            print(False)
    def get_password(self):
        print(self.__password)

Akhmad = UserAccount("Akhmad", "12345@gmail.com", "abc")
Akhmad.get_password() 
Akhmad.set_password()
Akhmad.get_password()
Akhmad.check_password()