#Bitmap message

import sys

bitmap = """....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

print("Bitmay Message, by Christian Brewer")
message = input("Enter the message to display with the bitmap: ")
if message == "":
  sys.exit()

#loop over each line
for line in bitmap.splitlines():
  #loop over each character in the line
  for i, bit in enumerate(line):
    if bit == " ":
      #print an empty space for the space in the bitmap
      print(" ", end="")
    else:
      #print a character from the message
      print(message[i % len(message)], end="")
  print() #print new line
