# data types

# 1.Numeric data types
# int
# float
# complex


# 2.Dictionary

# 3.Boolean


# 4.Set

# 5.Sequence data types
# list
# tuple
# string



# --------------------LIST------------------

# lt=[1,2,3,4,5,6,7,8,9,6]

# print(lt)

# index()
# print(lt.index(4))
# lt[0]=8
# print(lt)

# count()
# print(lt.count(6))


# append()
# lt.append(9)
# print(lt)

# extend()
# lt.extend([1.5,2,3])
# print(lt)

# copy()
# new_lt=lt.copy()
# print(new_lt)


# clear()
# lt.clear()
# print(lt)

# insert()
# lt.insert(3,44)
# print(lt)

# pop()
# lt.pop(3) #it will take the index value so it is with parameters
# print(lt)

# remove()
# lt.remove(9)
# print(lt)

# reverse()
# lt.reverse()
# print(lt)

# sort()
# lt.sort()
# print(lt)

# max
# print(max(lt))

# min
# print(min(lt))






# "Write a Python program to separate the even and odd numbers from a given list and store them in two separate lists."

lt=[1,2,3,4,5,6,7,8,9,6]

even=[]
odd=[]

for i in range(0,len(lt)):
    if lt[i]%2==0:
        even.append(lt[i])
    else:
        odd.append(lt[i])

print(even)
print(odd)