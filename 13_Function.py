# # Defined function first def and then function name and ():

# def add():
#     num1 = int(input("Entre the first Number "))
#     num2 = int(input("Entre the second Number "))
#     print(num1 + num2)
# # Function call Without call a function it can not be executed
# add()


# def add(a,b):
#     print(a + b)
# add(12,21)


# def fullName(first,middle,last):
#     print(first,middle,last)
# fullName("Ali ","Khan ","Saab")
# # Sequence matters in positional arguments
# # Keyword Arguments does not require Sequence
# print(fullName(middle ="khan",last ="Saab" ,first ="Ali"))


# # Default parameter
# def num(number1= 0,number2= 0):
#     print(number1 + number2)
# num(number2= 5)


# def pizzaOrder(size,falvor,*topping):
#     print(f"size of Pizza is {size} and falvor {falvor} and the topping is {topping}" )
# pizzaOrder(12 ,"Fruite","chikken","Mutton")


# # passing information back from function
# def add(val1 ,val2):
#     ans = val1 + val2

#     return ans
# result = add(3 ,3)
# print(result)


# # Using Function As Variable
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return b-a
# result = add(2,3) + sub(2,3)
# print(result)


# Local Variable
# Call only in function not outside the function

# def name1():
#     name = "Mr.A"
#     print(f"{name} is very happy today")
# name1()


# # Golbal Variable
# # Call in the function and also from outside the function

# anotherName = "Mr.B"
# def sad():
#     print(f"{anotherName} is very sad today")
# sad()


# Function with in a function

def commisionCalc(sales):
    if sales>100:
        return sales*100
    elif sales>50:
        return sales*50
    elif sales>20:
        return sales*20
    else:
        return 0

def salaryCalc(basic, sales):
    grossSalary = basic + commisionCalc(sales)
    print(f"Your gross salary is {grossSalary}")
salaryCalc(30000,120)