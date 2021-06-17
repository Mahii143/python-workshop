'''
Q 7: Define Exception.Write a program that accepts the date of birth along
with the personal details of a person . Throw an exception if it is an invalid date.{}
'''
name = input("Name : ")
try:
    dd, mm, yyyy = input("Date of birth (dd/mm/yyyy) : ").split('/')
    dd, mm, yyyy = int(dd), int(mm), int(yyyy)
    print("Age : ", 2021- yyyy)
except (Exception):
    print("Invalid Date")

email = input("Email : ").strip()
school = input("School : ").strip()
graduation1 = input("Year of Passing : ").strip()
college = input("College : ").strip()
graduation2 = input("Year of Passing : ").strip()

print("Code executed successfully")






