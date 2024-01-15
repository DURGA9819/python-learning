# fruits=["mango","orange"]
# for x in fruits:
#     print(x)
#     if x =="mango":
#         break

# fruits.append("apple")
# for x in fruits:
#     if x =="orange":
#         break
#     print(x)


# for x in "broadway":
#     print("\n",x)

# for x in fruits:
#     print("fruits",x)   

# for i in range(10):
#     print("hello world")    

# dict_data = {
#     "name" : "sujan",
#     "age" : 24
# }

# for y in dict_data:
#     print(dict_data[y])

# for z in range(10):
#     print(z)

# fruits.append("apple")
# for x in fruits:
#     if x =="orange":
#         continue
#     print(x)

# data = [1,2,3,4.4,5,6]
# for i in data:
#     if isinstance(i,float):
#         break
#     print(i)
    
# dict_num = {
#     "a":1,
#     "b":2,
#     "c":1.1,
#     "d":3
# }  

# for c in dict_num:
#     if isinstance(dict_num[c],float):
#         break
#     print(dict_num[c])


# # entered number multiplication
# a = int(input("enter a number"))
# for i in range(1, 11):
#     print(f'{a} * {i}= {a*i}')

# # 1 to 10 multiplication
# for a in range(1,11):
#  for i in range(1, 11):
#      print(f'{a} * {i}= {a*i}')

# a=[1,3,5,6,9]
# for a in a:
#  print("\n")
#  for i in range(1, 11):
#     print(f'{a} * {i}= {a*i}')

x=int(input("enter a number for mutiplication"))
if x<5:
     for i in range(1,x+1,1):
          a = int(input("enter a number"))
          for i in range(1, 11):
             print(f'{a} * {i}= {a*i}') 
else:
     print("number not multiply")


