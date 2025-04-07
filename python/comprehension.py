# ______________________COMPREHENSIONS__________________

# In Python, comprehensions provide a concise and efficient way to create lists, dictionaries, and
# sets by embedding loop and conditional logic within a single line of code


# LIST COMPREHENSION
 

# list=[1,2,3,4,5,6,7,8,9]

# even=[list[i] for i in range(len(list)) if list[i]%2==0]
# print(even)




# str_list=["rose","ruch","sakshi","vennelaa","ravi","papy"]

# new_str=(i for i in str_list if len(i)==4)
# print(list(new_str))


# list=[1,2,3,4,5,6,7,8,9]

# third=[list[x] for x in range(0,len(list),3)]
# print(third)



# list1=[[2,3],[1,2,3],[4,5,6,7,8,9]]

# new_list=[y for x in list1 for y in x]
# print(new_list)



# DICTIONARY COMPREHENSION

# dict={
#     "0":1,
#     "1":2,
#     "2":3
# }

# new_dict={x:y for x,y in dict.items() if y%2==0}
# print(new_dict)



# dict1={
#     "1":"roshini",
#     "2":"ruchitha",
#     "3":"Sahithi",
#     "4":"sai raj"
# }


# final_dict1={a:b for a,b in dict1.items() if b.startswith("S")}
# print(final_dict1)

# final_dict2={x:y for x,y in dict1.items() if y[0].lower()=="s"}
# print(final_dict2)