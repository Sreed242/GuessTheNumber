# Guess The Number Game
import random
numCorFun = 0
numCor = random.randint(0,99)
print("Welcome to Guess the Number\nPick a 2 digit number until you find the answer")
while numCorFun == 0:
    numGuess = int(input("What is your guess?   "))
    if numGuess > numCor: # If guess is too high
        print("Too high")
    if numGuess < numCor: # If guess is too low
        print("Too low")
    if numGuess == numCor: # If guess is correct
        print("Congrats you did it!")
        numCorFun = 1