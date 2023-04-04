#Birthday paradox
"""Birthday Paradox by Christian Brewer
This program shows the likelihood of two people sharing the same birthday in a group of people. """
import random

#days in months
days_in_month = {"January": 31,
  "February": 28,
  "March": 31,
  "April": 30,
  "May": 31,
  "June": 30,
  "July": 31,
  "August": 31,
  "September": 30,
  "October": 31,
  "November": 30,
  "December": 31,}

#list of months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
  #get sample size
  num_people = int(input("How many birthdays shall I generate? (Max 100): "))
  #show list
  print(f"Here are {num_people} birthdays:")
  
  #for each person, generate a month and day
  birthdays = get_birthdays(num_people)
  i = 1
  #iterate over list of birthdays and print out
  for birthday in birthdays:
    if i < num_people:
      print(birthday, end=", ")
    else:
      print(f"and {birthday}", end=".\n")
    i += 1
  matches = get_matches(birthdays)
  if len(matches) == 0:
    print("In this simulation, no one has matching birthdays.")
  else:
    i = 1
    print("In this simulation, multiple people have a birthday on ",end="")
    for birthday in matches:
      if i < len(matches):
        print(birthday, end=", ")
      else:
        if len(matches) == 1:
          print(birthday, end=".")
        else:
          print(f"and {birthday}", end=".\n")
      i += 1
  run_simulation(num_people, 100000)
    
  



#func for generating birthdays
def get_birthdays(number):
  birthday_list = []
  for num in range(number):
    month = random.choice(months)
    day = random.randrange(1, days_in_month[month])
    birthday = f"{month} {day}"
    birthday_list.append(birthday)
  return birthday_list

def get_matches(birthdays):
  matches = set()
  shared_birthdays = {birthday for birthday in birthdays if birthday in matches or (matches.add(birthday) or False)}
  return shared_birthdays

def run_simulation(num_birthdays, samples):
  i = 0
  matching_sims = 0

  while (i < samples):
    birthdays = get_birthdays(num_birthdays)
    matches = get_matches(birthdays)
    if matches:
      matching_sims += 1
    i += 1
    if i % 10000 == 0:
      print(f"{i} simulations run...")
  result = (matching_sims / samples) * 100
  print(f"Out of {samples} simulations of {num_birthdays}, there was a matching birthday in that group {matching_sims} times. This means that {num_birthdays} people have a {result}% chance of having a matching birthday in their group.\nThat's probably more than you would think!")
  
main()
