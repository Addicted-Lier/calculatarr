
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


    # for items in converted:
    #     print(items)
    if converted[1] == '+':
        ans = converted[0]+converted[2]
        print (ans)
    elif converted[1] =="-":
        ans = converted[0]-converted[2]
        print(ans)
    elif converted[1] =="*":
        ans = converted[0]*converted[2]
        print(ans)
    elif converted[1] =="/":
        ans = converted[0]/converted[2]
        print(ans)
    elif converted[1] =="%":
        ans = converted[0]%converted[2]
        print(ans)
    
   
