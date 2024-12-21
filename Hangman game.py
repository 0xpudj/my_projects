import random
hangman_words = ["apple", "banana", "chair", "house", "ocean", "tiger", "cloud", "happy", "pizza", "dance", "puppy", "movie", "lemon", "guitar", "candy"]
trying = 0
suggest =[]

the_word=random.choice(hangman_words)
print(f'the word has {len(the_word)} letters')


for i in range(len(the_word)):
    guess = input("Guess the word: ").lower()
    if trying == len(the_word)-1:
        print("You are out of the game")
        break

    if guess != the_word:
        suggest.append(the_word[i])
        print(f"you are wrong, the first letter is {suggest}")
        trying += 1
    elif guess == the_word:
        print("You are right")
        break
