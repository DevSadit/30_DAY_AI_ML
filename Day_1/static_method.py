class Student:

    def __init__(self, name, marks):
        self.name = name
        sum = 0
        for val in marks:
            sum += val
        self.avg = sum / 3

    @staticmethod
    def print_hello():
        print("hello.......")


s1 = Student("sadit -->", [40, 50, 60])
# print(s1.name, s1.avg)
# s1.print_hello()
