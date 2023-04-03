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
  #iterate over list of birthdays and print out
  for birthday in birthdays:
    print(birthday, end=", ")
  print(get_matches(birthdays))
  



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
  return matches

  
main()
