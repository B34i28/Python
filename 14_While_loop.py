flag = True
favFoods = []
while flag:
    userinput = input("Entre You favFood  ")
    if userinput == "q":
        flag = False
    else:
        favFoods.append(userinput)
print(favFoods)