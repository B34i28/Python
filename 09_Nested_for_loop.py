# for a in range(5):
#     print("Inner Loop start")
#     for char in "Malta":
#         print(a , char)
# tableNumber = int(input("Entre table Numeber "))
# for a in range(1,11):
#     print(f"{tableNumber} * {a} = {tableNumber*a}")
tables = int(input("Entre the Table "))
for table in range(2,tables +1):
    for num in range(1 ,11):
        print(f"{table} * {num} = {table*num}")