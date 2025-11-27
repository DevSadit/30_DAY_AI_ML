# question
# Create a Student class that takes name and marks of three subjects as arguments in
# constructor then create a method to print the average


class Student:
    university = "Premier University Chittagong"

    def __init__(self, name, marks):
        self.name = name
        sum = 0
        for val in marks:
            sum += val
        self.avg = sum / 3


s1 = Student("sadit", [40, 50, 60])
print(s1.name, s1.avg, s1.university)
