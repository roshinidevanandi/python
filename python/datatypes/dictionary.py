# details={"name":"roshini","age":23,"emp":False,"skills":["FE","BE","DB","datascience"],"add":{"r_no":3,"landmark":"peddapalli","street":"bandari kunta"}}

# print(details["add"])

# details.update({"name":"puppy"})
# print(details)

# details.update({"name":"roseee"})
# print(details)

# details.clear()
# print(details)

# del details["emp"]
# print(details)

# details.pop("name")
# print(details)

# k=details.keys()
# print(k)

# print(details.keys())


# print(details.values())

# print(details.items())

# person={
#     "name":"Roshini",
#     "age":22,
#     "city":"hyd"
# }


# if person["age"]>=20 and person["city"]=="hyd":
#         print("yes i am from india")
# else:
#         print("i am not indian citizen")



details={"name":"roshini","age":23,"emp":False,"skills":["FE","BE","DB","datascience"],"add":{"r_no":3,"landmark":"peddapalli","street":"bandari kunta"}}

req="FE"
exgisting=False
for i in details:
    if i=="skills":
        for j in range(0,len(details[i])):
            if details[i][j]==req:
                exgisting=True

if exgisting:
    print("he has the skill")
else:
    print("nothing")