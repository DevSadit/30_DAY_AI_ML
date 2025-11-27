# creating dictionary
student = {"name": "jahangir", "age": 20, "marks": [20, 40, 60]}
# print(student)

# accesing value by key
x = student["marks"]
# print(x)s


# update a key
y = student["name"] = 25
# print(y)


# remove a key
# del student["marks"]
# print(student)


# loop through a dictionary
for val in student["marks"]:
    print(val)
