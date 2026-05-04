
while True:
    kuit = input("enter 'q' to quit the calculator or press any other key to continue : ")
    
    

    if kuit.lower() == 'q':
        print("quiting the calculator")
        break
    

    op = input("Enter what you wish to do +,-,*,/ :  ")
    a = int(input("enter the first number for operation : "))
    b = int(input("enter the second number for operation : "))

    if op == "+":
        ans = a+b
        print (ans)
    elif op =="-":
        ans = a-b
        print(ans)
    elif op =="*":
        ans = a*b
        print(ans)
    elif op =="/":
        ans = a/b
        print(ans)
    elif op =="%":
        ans = a%b
        print(ans)
    
   
