num=int(input("Enter numbers: "))

if num<=1:
    print(f"{num}  He is not a prime number.")
elif num==2 or num==3:
    print(f"{num}  He is a prime number -_- ")
elif num%2==0 or num%3==0:
    print(f"{num}  He is not a prime number.")
else:
    for i in range(5, int(num**0.5) +1 ,2):
        if num%i==0:
            print(i)
            print(f"{num} is not a prime number. It is divisible by {i}.")
            break
    else:
        print(f"{num} it is prime number -_- ")