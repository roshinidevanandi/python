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

# Methods
# append
# insert
# extend
# pop
# remove
# copy
# count
# clear
# reverse
# sort
# max
# min


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

# lt=[1,2,3,4,5,6,7,8,9,6]

# even=[]
# odd=[]

# for i in range(0,len(lt)):
#     if lt[i]%2==0:
#         even.append(lt[i])
#     else:
#         odd.append(lt[i])

# print(even)
# print(odd)





# _____________________PROBLEM SOLVING___________________

# 1.remove duplicates from the given list and add it to new list

# data=[1,4,6,2,8,9,4,10,6,4,1]
# data=list(set(data))
# new_list=[]
# for i in range(len(data)):
#     new_list.append(data[i])
# print(new_list)




# 2.Find the third maximum value of the list


# data=[1,4,6,2,8,9,4,10,6,4,1,29,46,86,98,9]

# c=4
# data1=list(set(data))
# for i in range(1,c):
#     data1.remove(max(data1))

# print(max(data1))



# 3.sort the given list according to the second element

# list=[[1,2],[3,40],[5,6,9]]
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i][1]<list[j][1]:
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp

# print(list)
