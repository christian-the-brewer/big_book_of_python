#bagel game

import random

DIGITS = 3 #constant for digits in number
GUESSES = 10 #max guesses

game = True

print('''
Bagels, a deductive logic game.
 
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico           One digit is correct but in the wrong position.
  Fermi          One digit is correct and in the right position.
  Bagels         No digit is correct.
  
For example, if the secret number was 248 and your guess was 843, the
  clues would be Fermi Pico. Clues will be given in alphabetical order.'''.format(DIGITS))


def get_secret_number():
  #pick random numbers from list, then remove them after.
  nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
  i = 0
  secret_number_list = []
  while i < DIGITS:
    number = random.choice(nums)
    secret_number_list.append(number)
    nums.remove(number)
    i += 1
    #print(number) #TEST
  #print(secret_number_list) #TEST
  return ''.join([num for num in secret_number_list])

def guess_correct(guess):
  #check user guess to see if guess is 'in' secret_number and return bool
  if guess in secret_number:
    return True
  else:
    return False

def check_guess(guess, secret_number):
  clues = [] #list to hold possible clues Pico, Fermi, Bagels
  guess_list = list(guess) #convert guess into iterable list
  secret_number_list = list(secret_number) #convert secret number into iterable list
  for digit in guess_list: #iterate over each digit in guess
    if digit in secret_number_list:
      if guess_list.index(digit) ==secret_number_list.index(digit):
        clues.append("Fermi")
      else:
        clues.append("Pico")
  if clues == []:
    return "Bagels"
  else:
    return ' '.join([clue for clue in sorted(clues)])
  pass
  
  
while game: #game loop
  secret_number = get_secret_number() #secret number
  guesses = GUESSES #keep track of user guesses
  
  while guesses > 0:
    while True:
      user_guess = input("Enter your guess!: ")
      if len(list(user_guess)) == DIGITS:
        break
      else:
        print(f"The number is {DIGITS} digits long.")
    guesses -= 1
    #print(secret_number) #TEST
    if guess_correct(user_guess): #check if guess is right
      tries = GUESSES - guesses #get number of attempts
      print(f"You got it right in {tries} tries!")
      break
    else:
      print(check_guess(user_guess, secret_number))
      print()

  playing = input("Play again? y/n: ")
  if playing.lower() == 'n' or playing.lower() == 'no':
    game = False

  print("Thanks for playing!")
