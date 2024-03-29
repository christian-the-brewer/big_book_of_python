"""Caesar Cipher from https://inventwithpython.com/bigbookpython/project6.html"""
"""
try: 
  import pyperclip #copies text to clipboard
except ImportError:
  pass #if pyperclip is not installed do nothing

#list of every possible symbol
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
print('Caesar Cipher by Christian Brewer\nThis cipher encrypts a message by shifting symbols over by a numerical value.\n')

#choose encrypt of decrypt
while True:
  print('Do you wish to (e)ncrypt or (d)ecrypt? ')
  response = input('> ').lower()
  if response.startswith('e'):
    mode = 'encrypt'
    break
  elif response.startswith('d'):
    mode = 'decrypt'
    break
  print("please enter e or d.")

#enter cipher key
while True: 
  max_key = len(SYMBOLS) - 1
  print(f'Please enter a key (0 - {max_key})')
  response = input('> ').upper()
  if not response.isdecimal():
    continue
  if 0 <= int(response) < len(SYMBOLS):
    key = int(response)
    break

#enter message
print(f'Enter message to {mode}:')
message = input('> ')

message = message.upper()

#store encrypted/decrypted message
translated = ''

#for loop to use cipher on each symbol
for symbol in message:
  if symbol in SYMBOLS:
   #get number of symbol
    num = SYMBOLS.find(symbol)
    if mode == 'encrypt':
      num = num + key
    elif mode == 'decrypt':
      num = num - key

    #wrap around if num is larger than len of symbols
    if num >= len(SYMBOLS):
      num = num - len(SYMBOLS)
    elif num < 0:
      num = num + len(SYMBOLS)

    #add symbol to translated
    translated = translated + SYMBOLS[num]

  else:
    #add symbol to translated without changing
    translated = translated + symbol
print(translated)

try:
  pyperclip.copy(translated)
  print(f'{mode}ed message copied to clipboard.')
except:
  pass
  """
try:
  import pyperclip #try to import pyperclip and pass if not installed
except:
  pass

#list of all symbols to be translated
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ.'
#len of symbol list
len_symbol = len(SYMBOLS)

#loop to get encryption mode
while True:
  print('Would you like to (e)ncrypt or (d)ecrypt a message?')
  response = input('> ').lower()

  #test response
  if response.startswith('e'):
    mode = 'encrypt'
    break
  elif response.startswith('d'):
    mode = 'decrypt'
    break
  print('Enter e or d')

#user enter the translation key
while True:
  max_key = len_symbol - 1
  print(f'Enter the cipher key (1 - {max_key}) to use:')
  response = input("> ").upper()
  if not response.isdecimal():
    continue
    
  if 0 < int(response) <= max_key:
    key = int(response)
    break
  print()

#user enter the message
print(f'Enter message to {mode}:')
message = input('> ').upper()

#variable to hold translated message
translated = ''

#translate each symbol in message
for symbol in message:
  if symbol in SYMBOLS:
    num = SYMBOLS.find(symbol) #find index of symbol in list
    if mode == 'encrypt':
      num = num + key
    elif mode == 'decrypt':
      num = num - key

    #handle wrapping around list
    if num >= len_symbol:
      num = num - len_symbol
    elif num < 0:
      num = num + len_symbol

    translated = translated + SYMBOLS[num]

  else:
    translated = translated + symbol

#display translated message
print(translated)

