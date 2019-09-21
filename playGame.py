from deck import Deck
from card import Card
from player import Player
from game import Game
from time import sleep

import re


def daRules():
    """
	Returns the rules of the Game
	"""
    # print("hello")
    print(
        "Each participant attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21."
    )
    print(
        "It is up to each individual player if an ace is worth 1 or 11. Face cards are 10 and any other card is its pip value."
    )
    print(
        "A bet once paid and collected is never returned. Thus, one key advantage to the dealer is that the player goes first."
    )
    print(
        "If the player goes bust, he has already lost his wager, even if the dealer goes bust as well."
    )
    print("------------------------------")
    print("Really, you'll get the hang of it after playing a few rounds!")
    print(
        "Be SURE to follow the instructions to the T. Don't try anything goofy or the program will fail :("
    )
    print("------------------------------")


def addingPlayers(keepAdding, playersList):
    """
	keepAdding is a boolean flag signalling to continue adding players or not!
	"""
    if keepAdding:
        playerName = input("Add a player! Enter a name >")
        playerBuyIn = input("How much does " + playerName + " want to buy in? >")
        player = Player(playerName, playerBuyIn)
        playersList.append(player)
        sleep(0.3)
        print(".")
        print(".")
        print(".")
        sleep(0.3)
        addMore = input("Add more players ? (Y/N) > ")
        if addMore == "N" or addMore == "" or addMore == "n":
            keepAdding = False
        return addingPlayers(keepAdding, playersList)
    else:
        return playersList


def playGame():  # if the input is some random character (i.e. % or something, then display rules())
    print("Welcome to BlackJack!")
    rules = input("For rules, type: 'help' Otherwise type 'play': ")
    if rules == "help":
        daRules()
        playGame()
    elif rules == "play" or rules == "":
        # continue with the game !
        playersList = addingPlayers(True, [])
        print("Let's begin the Game!")
        # the Bet goes here
        keepPlaying = True
        newPlayersList = playersList
        theGame = Game(newPlayersList)
        while keepPlaying:
            wagers = theGame.theBet(newPlayersList)
            print("The bets are in!")
            print("Now we begin to Deal")
            theGame.theDeal(newPlayersList)  # cards have been dealt lit
            theGame.thePlay(wagers)
            for player in theGame.players:
                newPlayersList = []
                print([x.getName() for x in newPlayersList])
                if player.getMoney() <= 0:
                    print(player.getName() + " ran out of money :(")
                    continue
                playAgain = input(
                    player.getName() + " want to continue playing? (Y/N) >"
                )
                if playAgain not in ["Y", "y", "yes", "yuh", "yeah"]:
                    print("Goodbye " + player.getName())
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
