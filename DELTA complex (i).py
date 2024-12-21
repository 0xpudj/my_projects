print("for solve: ax²+bx+c=0 ")

a, b, c =float(input("Enter a= ")), float(input("Enter b= ")), float(input("Enter c= "))
DELTA=b**2-(4*a*c)
x1=(-b+DELTA**0.5) / (a*2)
x2=(-b-DELTA**0.5) / (a*2)

if DELTA>0:
    print("its a real value and correct, and they have two solution is:\n" + str(x1) +"\n" +str(x2))
elif DELTA==0:
    print("its a real value and not correct, he have one solution is: " + str(x1))
else :
    print("its a complex value (imaginary value):\n")
    i=DELTA*-1
    i1=-b/ (a*2)
    i1_5=(i**0.5)/ (a*2)
    i2=-b/ (a*2)
    i2_5=(-i**0.5)/ (a*2)
    print("He have two solution:\n" +str(i1)+"+"+str(i1_5)+"i\n"+str(i2)+str(i2_5)+"i")

