
import re
while True:
    kuit = input("enter 'q' to quit the calculator or press any other key to continue : ")
    
    

    if kuit.lower() == 'q':
        print("quiting the calculator")
        break
    

    op = input("write the full operation to perform : ")
    parts = re.split(r'([-/*%+])', op) # be wary of regex expression 

    converted = []

    for item in parts:
        if item.isdigit() :
            number = int(item)
            converted.append(number)
        else:
            converted.append(item)
    i = 0
    while i < (len(converted)):
        if converted[i] == "*" :
            num1 = converted[i-1]
            num2 = converted[i+1]
            result = num1*num2
            converted[i-1 : i+2] = [result]
            i=0
            continue

        elif converted[i] == "/" :
            num1 = converted[i-1]
            num2 = converted[i+1]
            if num2 !=0:
                result = num1/num2
            else:
                # exptn = "Maybe you have put 0, dividing with 0 = nada."
                print("dividing a number with 0 = nada \n exiting the calculator")
                break
            converted[i-1 : i+2] = [result]
            i=0
            continue
        i+=1
    # for items in converted:
    #     print(items)
    print(converted)
    # if converted[1] == '+':
    #     ans = converted[0]+converted[2]
    #     print (ans)
    # elif converted[1] =="-":
    #     ans = converted[0]-converted[2]
    #     print(ans)
    # elif converted[1] =="*":
    #     ans = converted[0]*converted[2]
    #     print(ans)
    # elif converted[1] =="/" and converted[2]!=0:
    #     ans = converted[0]/converted[2]
    #     print(ans)
    # elif converted[1] =="%":
    #     ans = converted[0]%converted[2]
    #     print(ans)
    
    
