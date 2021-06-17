class InvalidAge(Exception):
    def display(self):
        print("Your age is invalid... You cannot vote....")
class InvalidName(Exception):
    def display(self):
        print("Your name is invalid")

try:
    n= input("Enter your name : ")
    a = int(input("Enter age : "))
    if len(n) == 0:
        raise InvalidName
    if a >= 18:
        print("You can cast vote....")
    else:
        raise InvalidAge
except InvalidAge as e:
    e.display()
except InvalidName as b:
    b.display()
