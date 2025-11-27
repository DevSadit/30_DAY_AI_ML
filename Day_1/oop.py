# # making class
# class Student:
#     name = "MD."


# # object
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# understanding constructor
class Student:
    def __init__(self, name, age):  # s1 and self location is same
        print("new student created...")
        self.name = name
        self.age = age


# object
s1 = Student("Abol", 80)
print(f"{s1.name} is {s1.age} years old")  # || s1 and self location is same


s2 = Student("Rafiq", 39)
print(f"{s2.name} is {s2.age} years old")
