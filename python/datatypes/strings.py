# --------------STRINGS------------

# String is a collection of charectors
# It is immutable we can't change the elements and it is primitive data type
# In strings elements are accessed through the index
# It is a sequence data type



data=" helloeveryONE234"
# print(data)

# data[0]="r"    -->TypeError: 'str' object does not support item assignment


# METHODS

# upper()
# print(data.upper())

# lower()
# print(data.lower())

# swapcase()
# print(data.swapcase())


# strip()  --->it removes the spaces
# print(data.strip())

# lstrip()
# print(data.lstrip())

# rstrip()
# print(data.rstrip())


# # replace()
# print(data.replace("e","E"))
# print(data.replace("e","9"))

# isalpha()
# print(data.isalpha())

# isdigit()
# print(data.isdigit())

# isalnum()
# print(data.isalnum())

# startswith()
# print(data.startswith("h"))

# endswith()
# print(data.endswith("r"))

# find()  ->it finds the index of the element
# print(data.find("e"))

# zfill() -->zero fill
# print(data.zfill(30))

# center()
# print(data.center(30,"*"))


for i in range(len(data)):
    print(data[i])
