class User:
    def login(self):
        print("Login")
class Bussinessuser(User):
    def run_add(self):
        print("run add")
b=Bussinessuser()
b.login()
b.run_add()
