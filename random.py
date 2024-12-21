import random
import termcolor

trying=0
x=random.randrange(50,5000)
while True:
    try:
        answer = int(input("Please Guess the number in range [50,5000]: "))
        trying+=1
        if answer == x:
            termcolor.cprint(f"Congratulations! You have guessed the number, you guessed {trying} times", "green")
            break
        elif answer > x:
            termcolor.cprint("Try a smaller number", "blue")
        else:
            termcolor.cprint("Try a bigger number", "red")
    except ValueError:
        termcolor.cprint('Enter an interger value', 'green')  