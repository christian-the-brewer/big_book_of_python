#https://inventwithpython.com/bigbookpython/project7.html

"""Caesar Hacker by Christian Brewer
a brute force hack of a caesar cipher"""

print('Enter an Caesar Cipher encrypted message: ')
message = input('> ').upper()

#list of symbols must match
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
  translated = ''

  #decrypt each symbol in message
  for symbol in message:
    if symbol in SYMBOLS:
      num = SYMBOLS.find(symbol) #find number of symbol
      num = num - key
      
      #handle wrap around
      if num < 0:
        num = num + len(SYMBOLS)
      
      #add to translated
      translated = translated + SYMBOLS[num]
      
    else:
      translated = translated + symbol
      
  print(f'Key #{key}: {translated}')
