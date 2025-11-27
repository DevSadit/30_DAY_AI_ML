# question
# Create a Student class that takes name and marks of three subjects as arguments in
# constructor then create a method to print the average


class Student:

    def __init__(self, name, marks):
        self.name = name

        sum = 0
        for val in marks:
            sum += val

        self.avg = sum / 3
        print(f"{self.name}'s average mark is {self.avg}")


s1 = Student("jahangir", [70, 80, 90])
s2 = Student("kabir", [75, 90, 68])
s3 = Student("samiya", [70, 78, 60])
