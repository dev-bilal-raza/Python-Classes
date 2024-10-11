import math
import random

print("Ceil value: ", math.ceil(4.6))
print("Floor value: ", math.floor(4.6))
print("Floor value: ", math.isclose(4.6, 4.5))
print("Floor value: ", math.factorial(5))
print("Floor value: ", math.pi)
print("Random Choice: ", random.choice(["bilal", "razaq"]))
print("Random Integer: ", random.randint(1, 2))

# List methods:

user_list: list[int | list] = [1,5,9,2,4,5,7,8]
# user_list.append(10)
# print("Apended: ", user_list)

# user_list.append([10, 11, 12])
# print(user_list[7])

# user_list.extend([10, 11, 12])
# print(user_list)

# user_list.reverse()
# print(user_list)

# user_list.remove(4)
# print(user_list)


# print(user_list.index(4))

# user_list.pop(4)
# print(user_list)

# user_list.insert(4, 20)
# print(user_list)

print(user_list.count(4))

# user_list.clear()
# del(user_list)
user_list.sort()
print(user_list)
