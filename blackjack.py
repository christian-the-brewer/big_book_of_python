#blackjack by Christian Brewer
#https://inventwithpython.com/bigbookpython/project4.html

import random, sys

#Constants
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)
BACKSIDE = "backside"

def main():
  print("""Rules:
       Try to get as close to 21 without going over.
       Kings, Queens, and Jacks are worth 10 points.
       Aces are worth 1 or 11 points.
       Cards 2 through 10 are worth their face value.
       (H)it to take another card.
       (S)tand to stop taking cards.
       On your first play, you can (D)ouble down to increase your bet
       but must hit exactly one more time before standing.
       In case of a tie, the bet is returned to the player.
       The dealer stops hitting at 17.""")

  money = 5000

  while True: #game loop
    #check if player has money
    if money <= 0:
      print("You are broke!\nThanks for playing!")
      sys.exit()
    #Enter bet 
    print(f"Money: {money}")
    bet = getBet(money)

    #Give healer and player two cards from the deck
    deck = getDeck()
    dealerHand = [deck.pop(), deck.pop()]
    playerHand = [deck.pop(), deck.pop()]

    #handle player actions
    print(f"Bet: {bet}")
    #looping until player stands or busts
    while True:
      displayHands(playerHand, dealerHand, False)
      print()

      #check if player has bust
      if getHandValue(playerHand) > 21:
        break

      #get player'compile
      move = getMove(playerHand, money - bet)

      #handle player action
      if move == "d":
        #player is doubling down
        additionalBet = getBet(min(bet, (money - bet)))
        bet += additionalBet
        print(f"Bet increased to {bet}.")
        print(f"Bet:{bet}")

      if move in ("h", "d"):
        newCard = deck.pop()
        rank, suit = newCard
        print(f"You drew a {rank} of {suit}.")
        playerHand.append(newCard)
        if getHandValue(playerHand) > 21:
          continue

      if move in ("s", "d"):
        break

    #handle dealer actions
    if getHandValue(playerHand) <= 21:
      while getHandValue(dealerHand) < 17:
        #dealer hits
        print("Dealer hits...")
        dealerHand.append(deck.pop())
        displayHands(playerHand, dealerHand, False)
        if getHandValue(dealerHand) > 21:
          breakpoint
        input("Press Enter to continue...")
        print("\n\n")

    displayHands(playerHand, dealerHand, True)
    playerValue = getHandValue(playerHand)
    dealerValue = getHandValue(dealerHand)
    if dealerValue > 21:
      print(f"Dealer busts! You win {bet}!")
      money += bet
    elif (playerValue > 21) or (playerValue < dealerValue):
      print("You lose!")
      money -= bet
    elif playerValue > dealerValue:
      print(f"You win {bet}!")
      money += bet
        
