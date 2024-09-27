# for comment (#) (ctrl + /)

# Arthimetic Operaotrs:

# +
# -
# *
# /
# // Floor Division
# %
# **
print("Plus: ", 2 + 2)
print("Minus: ", 2 - 2)
print("Divide: ", 6 / 3)
print("Floor Division: ", 9 // 5)
print("Modulus: ", 5 % 2)
print("Square: ", 5 ** 2)



# Assignment Operators:

# 1) =
name = "bilal"

# 2) +=
myAge = 12
myAge += 2
print(myAge)

# 3) -=
myAge = 12
myAge -= 2
print(myAge)

# 4) *=
myAge = 12
myAge *= 2
print(myAge)

# 5) /=
my_age = 12.0
my_age /= 2
print(my_age)

# 6) //=
my_age = 12.8
my_age //= 2
print(my_age)

# 7) **=
my_age = 12
my_age **= 2
print(my_age)

# Comparison Operators:
# 1) ==
# 2) <
print(False < 1)
# 3) >
print(3 > 1)
# 4) <=
# 5) >=
# 6) !=
print(int("3") == 3)

# Membership Opearators

# in
my_list = ["hammad", "bilal"]
print("IN Operator: ", "bilal" in my_list)

# not in
print("NOT IN Operator: ", "bilal" not in my_list)

# to find all mothods related to data type
# print(dir("bilal"))


# Logical Operators:

print("Logical and: ", 1 == 1 and 2 < 4)
print("Logical or: ", 1 == 1 or 2 > 4)

# String Methods:

# 1) Format method

my_message = """
My name is {1}
I am a {0}
""".format("bilal", "developer")

my_other_message = """
My name is {1}
I am a {0}
""".format(my_list[0], "developer")
print(my_message)

#
print("bilal raza".capitalize())
print("bilal".upper())
print("Bilal raza".lower())
print("bilal raza".title())
print("bilal raza"[0])
print("Bilal raza".casefold())
print("Bilal raza".count("l"))
print("Bilal raza".encode())
print("Bilal raza".endswith("za"))
print("bilal raza".startswith("bi"))
print("bilal raza".find("l"))
print("bilal raza".index("i"))
print("bilal raza".rfind("l"))
print(" bilal raza".removeprefix("bi"))
print(" bilal raza".removeprefix(" "))
print("bilal raza".islower())
print("bilal raza".isupper())
print("     bilal raza ".strip())
print("     bilal raza ".lstrip())
print("     bilal raza ".rstrip())
print("bilal raza".replace("l", "L"))
print("  ".isspace())
print("bilal raza".istitle())
print("2".isdecimal())
print("bilal\traza".expandtabs(16))

message = "Bilal raza"

print([*message])


import re

my_name = "Bilal    raza"
information = re.sub(" {2,10}", "", my_name)
print(information)