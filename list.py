while True:
    print("   1-for addition(+) \n   2-for subtraction(-) \n   3-for multiply(*) \n   4-for division(÷) \n   5-for modulus(the rest of div ÷)")
    
    num1=float(input("Enter the first number: "))
    op=int(input("Chose your operation: "))
    num2=float(input("Enter the second number: "))
    
    if op==1:
        print(num1+num2)
    elif op==2:
        print(num1-num2)
    elif op==3:
        print(num1*num2)
    elif op==4:
        print(num1/num2)
    elif op==5:
        print(num1%num2)
    else:
        print("try again wrong operation")
    x=input("wana try again? \n1-yes \n2-no \n--")
    if x=="1":
        x
    else:
        break