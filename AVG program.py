sum_marks=0
models=0
while True:
    user=input("        Enter to chose an option:\nI-'1' add a note   II-'END' see result.\n")
    if user== '1':
        mark=float(input("Enter your note in the exam (0-20)"))
        if 0<= mark<=20:
            sum_marks += mark
            models += 1
        else:
            print("Invalid value, don't be stupid. ")
    elif user.upper()== "END":
        break
    else:
        print("invalid input, try again!")

avg= sum_marks/models
if float(avg) <10:
    print(f"You will repeat the year because you failed, result: {avg}")
else:
    print(f"Congratulation, You are passed the year with: {avg}")