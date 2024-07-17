from INTRODUCTION_TO_OOP import User


class User:
    def _init_(self, schoolName, schoolAddress):
        self.schoolName = schoolName
        self.schoolAddress = schoolAddress

    def show(self):
        print(self.schoolName, "\nAdress", self.schoolAddress)

    Victoria = User("BIngham university", "Nassarawa")

    def register(self, name, phone, email, password):
        return name

    def login(self, email, password):
        if email == "test@mail.com" and password == "abc":
            return True
        else:
            return False



