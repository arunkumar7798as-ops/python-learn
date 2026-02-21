
import random

number = random.randint(1,10)
attempts = 0

while True:
    guess= int(input("Guess the number between 1 and 10:"))
    attempts+=1
    if guess == number:
       print("Congratulation! You guessed it right in",attempts,"tries!")
       break
    elif guess<number:
       print("Too low! try again,")
    else:
       print("Too high!try again,")
 
