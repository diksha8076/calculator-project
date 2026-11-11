def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1+num2)/2

print("select a operation : \n" "1. addition \n" "2. subtraction \n" "3.multiplication \n" "4.divide \n" "5.average\n")

select = int(input("select a operation 1,2,3,4,5 :"))

num1 = int(input("enter first number :"))

num2  = int(input("enter second number :"))

if select == 1 :
    print(num1 ,"+", num2,"=", add(num1 , num2))
elif select == 2 :
    print(num1 ,"-", num2,"=" , sub(num1 , num2))
elif select == 3 :
    print(num1 ,"*", num2,"=" , multiply(num1 , num2))
elif select == 4 :
    print(num1 ,"/", num2,"=" , divide(num1 , num2))
elif select == 5 :
    print("(",num1 ,"+", num2,")","/","2","=" , avg(num1 , num2))
    

    

    



