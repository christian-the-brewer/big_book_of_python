"""Bagels, by Al Sweigart al@inventwithpython.com
  2. A deductive logic game where you must guess a number based on clues.
  3. This code is available at https://nostarch.com/big-book-small-python-programming
  4. A version of this game is featured in the book, "Invent Your Own
  5. Computer Games with Python" https://nostarch.com/inventwithpython
  6. Tags: short, game, puzzle"""

import random

NUM_DIGITS = 3 # Try setting this to 1 or 10
MAX_GUESSES = 10 #Try setting this to 1 or 100


def main():
  print('''Bagels, a deductive logic game.
 16. By Al Sweigart al@inventwithpython.com
 17. 
 18. I am thinking of a {}-digit number with no repeated digits.
 19. Try to guess what it is. Here are some clues:
 20. When I say:    That means:
 21.   Pico         One digit is correct but in the wrong position.
 22.   Fermi        One digit is correct and in the right position.
 23.   Bagels       No digit is correct.
 24. 
 25. For example, if the secret number was 248 and your guess was 843, the
 26. clues would be Fermi Pico.'''.format(NUM_DIGITS))

  while True: #Main game loop
    #This stores the secret number the player needs to guess:
    secretNum = getSecretNum()
    print("I have thought of a number.")
    print(f"You have {MAX_GUESSES} guesses to get it.")

    numGuesses = 1
    while numGuesses <= MAX_GUESSES:
      guess = ''
      #Keep loopng until they enter a valid guess:
      while len(guess) != NUM_DIGITS or not guess.isdecimal():
        print(f"Guess #{numGuesses}")
        guess = input("> ")

        clues = getClues(guess, secretNum)
        print(clues)
        numGuesses += 1

        if  guess == secretNum:
          break #They're correct, so break out of this loop
        if numGuesses > MAX_GUESSES:
          print("You ran out of guesses.")
          print(f"The answer was {secretNum}.")

    #Ask player if they want to play again
    print("Do you want to play again? (yes/no)")
    if not input("> ").lower().startswith("y"):
      break
  print("Thanks for playing!")


def getSecretNum():
  """Returns a string made up of NUM_DIGITS unique random digits."""
  numbers = list('0123456789') #create a list of digits 0 to 9
  random.shuffle(numbers) #shuffle them into random order

  #Get the first NUM_DIGITS digits in the list for secret number:
  secretNum = ''
  for i in range(NUM_DIGITS):
    secretNum += str(numbers[i])
  return secretNum


def getClues(guess, secretNum):
  """Returns a string with the pico, firmi, and bagels clues for a guess
  and secret number pair."""
  if guess == secretNum:
    print("You got it!")

  clues = []

  for i in range(len(guess)):
    if guess[i] == secretNum[i]:
      #A correct digit in the correct place
      clues.append("Fermi")
    elif guess[i] in secretNum:
      #A correct digit is in the incorrect place
      clues.append("Pico")
  if len(clues) == 0:
    return "Bagels" #There are no correct digits
  else:
    #sort the clues alphabetical order so their original order 
    #does'nt give anything away
    clues.sort()
    #Make a single string from the list of string clues
    return ' '.join(clues)


#If the program is run (instead of imported), run the game:
if __name__ == '__main__':
  main()
  
