from user import User

user = User()
user.register("Kemi", "08085987444", "agbajekemisola95@gamil.com", "123456")

email= input("Enter Your Email")
password= input("Enter Your Password")
print(user.login(email, password))