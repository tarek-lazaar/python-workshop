import datetime

year = int(input("year of birth please:"))

now = datetime.datetime.now()

age = now.year - year

print("you are" , age,"years old")
