# sum generator
def sum(x, y):
    total = x + y
    return total


# biggest number finder
def bigest(x, y, z):
    if (x > y) and (x > z):
        return x
    elif (y > z) and (y > x):
        return y
    else:
        return z


# finding sum in lists
def list_sum(list):
    sum = 0
    for x in list:
        sum += x
    return sum


# print(sum(12, 3))
# print(bigest(12, 3, 60))

lists = [10, 50, 70, 10]
# print(list_sum(lists))
