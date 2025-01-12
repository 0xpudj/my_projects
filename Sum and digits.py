nums = input("Enter a number: ")

def exr3(num):
    sumer = 0
    for num in nums:
        sumer += int(num)
    
    lenght =len(nums)
    return sumer , lenght

exr3(nums)
print("The sum of the digits is: ", exr3(nums)[0])
print("The number of digits is: ", exr3(nums)[1])   
