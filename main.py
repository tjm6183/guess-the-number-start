#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
the_number = random.randrange(1,100)
user_guess = 0 

def guess_number():
  if user_guess > the_number:
    print("Too high.")
  elif user_guess < the_number:
    print("Too low.")
  elif user_guess == the_number:
    print(f"You got it! The number is {the_number}.")
    exit()

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 0 and 100.")
choice = input("Choose a difficulty. Type 'easy' or 'hard'.: ")

if choice == "hard":
  for x in range(1, 6):
    print(f"You have {6 - x} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    guess_number()
    print("Guess again.")
  else:
    print(f"Sorry, you did not guess the number. The number was {the_number}. ")
    
elif choice == "easy":
  for x in range(1, 11):
    print(f"You have {11 - x} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    guess_number()
    print("Guess again.")
  else:
    print(f"Sorry, you did not guess the number. The number was {the_number}. ")