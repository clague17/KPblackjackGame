from deck import Deck
from card import Card
from player import Player
from time import sleep

class Game:
	def __init__(self, newPlayers):
		"""
		takes in a dictionary 'players' which holds <playerName, buy_in> as key, val pairs
		Has parameters:
			players
			dealer
			deck
		"""
		self.players = newPlayers
		self.dealer = Player("dealer", 99999999999) #has virtually unlimited money
		self.deck = Deck()

	def __str__(self):
		return str(self.players, self.dealer, self.deck)

	def theBet(self, playersList):
		"""
		Just performs theBet portion of the game, locking in everyone's bet
		"""
		print("First, the Bet.")
		wagers = {}
		for player in playersList:
			bet = input("How much does " + player.getName() + " want to bet for this round? >") #add some input parsing
			wagers[player] = int(bet)
		return wagers

	def theDeal(self, players):
		"""
		players is a list of all the Player objects
		"""
		print("Shuffling the deck...")
		sleep(.1)
		self.deck.shuffle()
		print(".")
		sleep(.1)
		print("Dealing...")
		for player in players:
			player.hitMe(self.deck.getCard()) #give a player a random card
			print(player.getName() + " has " + player.getCards()[0].getFace())
		# self.dealer.hitMe(self.deck.getCard())
		for player in players:
			player.hitMe(self.deck.getCard())
			print(player.getName() + " has " + player.getCards()[1].getFace())

	def thePlay(self, wagers):
		"""
		wagers is a dictionary containing <player: money bet> for that round
		"""
		for player in self.players:
			print("It is " + player.getName() + " turn. ", " You have " + str([x.getFace() for x in player.getCards()]),
					" for a total of: " + str(player.getScore()))
			hitMe = input("Hit ? (Y/N) >")
			bust = False
			while (hitMe == "Y" or hitMe == "") and not bust:
				player.hitMe(self.deck.getCard())
				print([x.getFace() for x in player.getCards()], " for a total of: " + str(player.getScore()))
				bust = player.isBust()
				if bust:
					break
				hitMe = input("Hit again? (Y/N) >")
		# implementing the dealer's play!
		print("The dealer has " + str([x.getFace() for x in self.dealer.getCards()]))
		sleep(.9) #The time delays make the experience a whole lot better
		while self.dealer.getScore() < 17:
			print("...")
			sleep(1)
			self.dealer.hitMe(self.deck.getCard())
			print("The dealer has: " + str([x.getFace() for x in self.dealer.getCards()]), " for a total of: " + str(self.dealer.getScore()))
		if self.dealer.isBust():
			print("The dealer went bust!")
			sleep(.08)
			for player in self.players:
				if not player.isBust():
					print("...")
					sleep(1)
					print(player.getName() + " gets " + str(wagers[player]))
					player.updateMoney(int(wagers[player])) #update the player.money attribute
				elif player.isBust():
					print("You went bust as well, so you still lose :(")
					sleep(.8)
					print(player.getName() + " lost " + str(wagers[player]))
					player.updateMoney(-1*int(wagers[player]))
		else:
			# print("The dealer has: " + str([x.getFace() for x in self.dealer.getCards()]), " for a total of: " + str(self.dealer.getScore()))
			for player in self.players:
				if self.dealer.getScore() < player.getScore() and not player.isBust():
					print("...")
					print("You beat the dealer! " + str(player.getScore()) + " > " + str(self.dealer.getScore()))
					#then payout
					print(player.getName() + " gets " + str(wagers[player]))
					player.updateMoney(int(wagers[player]))
				else:
					if player.isBust():
						print("...")
						print(player.getName() + " went bust!")
						print(player.getName() + " lost " + str(wagers[player]))
						player.updateMoney(-1*int(int(wagers[player])))
						break
					print("...")
					print("The dealer beat you :(" + str(player.getScore()) + " < " + str(self.dealer.getScore()))
					print(player.getName() + " lost " + str(wagers[player]))
					player.updateMoney(-1*int(int(wagers[player])))
		print("...")
		sleep(1.5)
		print("The round is over.")
		# print(".")
		for player in self.players:
			print(player.getName() + " now has " + str(player.getMoney()))
