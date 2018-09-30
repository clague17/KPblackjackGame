from deck import Deck
from card import Card
from player import Player
from game import Game
from time import sleep

import re


def rules():
	"""
	Returns the rules of the Game
	"""
	# str = "WELCOME TO THIS AWESOME AMAZING GAME ITS LIT WOW AWESOME LITTY"
	str = "A bet once paid and collected is never returned. Thus, one key advantage to the dealer is that the player goes first. If the player goes bust, he has already lost his wager, even if the dealer goes bust as well. If the dealer goes over 21, he pays each player who has stood the amount of that player's bet. If the dealer stands at 21 or less, he pays the bet of any player having a higher total (not exceeding 21) and collects the bet of any player having a lower total. If there is a stand-off (a player having the same total as the dealer), no chips are paid out or collected."

	return str

def addingPlayers(keepAdding, playersList):
	"""
	keepAdding is a boolean flag signalling to continue adding players or not!
	"""
	if keepAdding:
		playerName = input("Add a player! Enter a name >")
		playerBuyIn = input("How much does " + playerName + " want to buy in? >")
		player = Player(playerName, playerBuyIn)
		playersList.append(player)
		sleep(.3)
		print(".")
		print(".")
		print(".")
		sleep(.3)
		addMore = input("Add more players ? (Y/N) > ")
		if addMore == "N" or addMore == "" or addMore == "n":
			keepAdding = False
		return addingPlayers(keepAdding, playersList)
	else:
		return playersList


def playGame(): #if the input is some random character (i.e. % or something, then display rules())
	print("This is the game that we are playing!")
	rules = input("For rules, type: 'help' Otherwise type 'play': ")
	if rules == "help":
		print(rules())
	elif rules == "play" or rules == "":
		#continue with the game !
		playersList = addingPlayers(True, [])
		print("Let's begin the Game!")
		#the Bet goes here
		keepPlaying = True
		newPlayersList = playersList
		theGame = Game(newPlayersList)
		while keepPlaying:
			wagers = theGame.theBet(newPlayersList)
			print("The bets are in!")
			print("Now we begin to Deal")
			theGame.theDeal(newPlayersList) #cards have been dealt lit
			theGame.thePlay(wagers)
			for player in theGame.players:
				newPlayersList = []
				print([x.getName() for x in newPlayersList])
				if player.getMoney() <= 0:
					print(player.getName() + " ran out of money :(")
					continue
				playAgain = input(player.getName() + " want to continue playing? (Y/N) >")
				if playAgain != "Y":
					print("Goodbye " + player.getName())
					# newPlayersList.remove(player)
				else:
					player.resetRound()
					newPlayersList.append(player)
			if not newPlayersList:
				keepPlaying = False
				print("...")
				sleep(1)
				print("Thanks for playing! Come give us your money again soon!")
				return
		# We've added everyone!
	else:
		print("You done goofed :(")
		return

### actually drive the game below here

playGame()
