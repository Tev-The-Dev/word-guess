import random
print('Welcome to the word guesser game.')
name = input('What is your name?\n')
print('Good luck', name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print('Start by guessing a letter')

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print()
        print("You win!")
        print("The word is: ", word)
        break
    print()
    guess = input("Guess a character\n")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns,"more guesses")
        if turns == 0:
            print("You lose")
