def inc(x):
    x+=1
    return x
def dec(x):
    x-=1
    return x

def add(z,y):
    while True:
        z=inc(z)
        y=dec(y)
        if y ==0:
            return z

def mul(a, b):
    result = 0
    while b > 0:
        result = add(result, a)  
        b = dec(b)
    return result

def div(a, b):
    result=0
    while a >= b:
        a = a - b
        result += 1
    return result,a
print(div(15,5))
a=15
b=5





