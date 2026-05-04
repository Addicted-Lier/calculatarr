op = input("Enter what you wish to do +,-,*,/ : ")
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

