print("Quiz math game ,answer the following question: \n\n")
ans=list()
score=0
False_answer=0

x=['C', 'A', 'B', 'C', 'B', 'C', 'A', 'D', 'B', 'B']
y=['3', '1', '2', '3', '2', '3', '1', '4', '2', '2']

Quiz=['''.1. What is the sum of 130+125+191?\nA. 335\nB. 456\nC. 446\nD. 426\n''' ,
    '''2: If we minus 712 from 1500, how much do we get?\nA. 788\nB. 778\nC. 768\nD. 758\n''',
    '''3: 50 times of 8 is equal to:\nA. 80\nB. 400\nC. 800\nD. 4000\n''',
    '''4: 20+(90÷2) is equal to:\nA. 50\nB. 55\nC. 65\nD. 60\n''',
    '''5: The product of 82 and 5 is:\nA. 400\nB. 410\nC. 420\nD. None of these\n''',
    '''6: Find the missing terms in multiple of 3: 3, 6, 9, __, 15\nA. 10\nB. 11\nC. 12\nD. 13\n''',
    '''7: Solve 24÷8+2.\nA. 5\nB. 6\nC. 8\nD. 12\n''',
    '''8: Solve: 300 – (150×2)\nA. 150\nB. 100\nC. 50\nD. 0\n''',
    '''9: The product of 121 x 0 x 200 x 25 is\nA. 1500\nB. 0\nC. 4000\nD. None of these\n''',
    '''10: What is the next prime number after 5?\nA. 6\nB. 7\nC. 9\nD. 11\n''']


for i in Quiz:
    print(i)
    ans.append(input("Enter your answer Here: ").upper())    

for i in range(10):
    if ans[i] == x[i] or ans[i] == y[i]:
        score+=1
    else:
        False_answer+=1
print(f"Your score is {score} and you missing {False_answer} point. ")