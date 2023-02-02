# List Are Muteable
# alist = ["Ali","Shahbaz","Gull Khan","Sajid"]
# #print(alist)
# #print(alist[2])
# #print(alist[1])
# #print(len(alist))
# # Adding member to the list
# # append add value to the list in last by default
# alist.append("john wick")
# print(alist)
# # insert take the index number and then and value to it
# alist.insert(2,"Rocky")
# print(alist)
# # extend add more then one value at a time
# alist.extend(["zameer","nazeer", "Gull Khan"])
# print(alist)
# # This count function count the values in list how many time repeated
# x = alist.count("Gull Khan")
# print(x)
# y = alist.index("nazeer")
# print(y)
# alist.clear()
# print(alist)
# alist = ["Ali","Shahbaz","Gull Khan","Sajid"]
# print(alist)
# alist.copy() # by value it cant be change
# print(alist)
# alist2 = alist # by refrence it can change
# print(alist2)
# alist.append("newkhan")
# print(alist2)
# del alist[0]
# print(alist)
# alist.remove("Gull Khan")
# print(alist)
# poplist = alist.pop()
# print(f"This is poped {poplist}")
# print(f"This is list{alist}")
# # slicing
# print(alist)
# print(alist[0:1])
students = ["kashif","ali","Faisal","mohd","arsalan","javid"]
print(students)
print(students[:])
print(students[4:])
print(students[:3])
num1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(num1[1:17:2])
del num1[4]
print(num1)