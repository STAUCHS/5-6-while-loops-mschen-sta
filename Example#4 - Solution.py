# Example 4 - Guessing Game - Correct Solution

import random

num = random.randrange(1, 101)

guess = int(input("Enter a guess: "))

while guess != num:
  if guess > num:
    print("Guess is too high. Guess again.")
  else:
    print("Guess is too low. Guess again.")
    
  guess = int(input("Enter a guess: "))

print("Congratulations! You guessed correct!")
