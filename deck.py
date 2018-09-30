import random as random
from card import Card

class Deck:
	def __init__(self):
		"""
		generates a standard deck of 52 Card objects with 13 Cards for each of
		the 4 suits
		"""
	# shuffle function
	# a getCard function
	# a getRandomCard function
		allPossibleVals = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
		 					"J", "Q", "K"]
		allPossibleSuits = ["Club", "Clover", "Heart", "Diamond"]

		deck = [] #why a list? why not a dictionary?

		for suit in allPossibleSuits:
			for val in allPossibleVals:
				deck.append(Card(suit, val))

		self.deck = deck

	def __str__(self):
		"""
		Typical toString method
		"""
		return str(deck)

	def getCards(self):
		"""
		Returns the list of Card objects
		"""
		return self.deck

	def shuffle(self):
		"""
		Uses the python method for shuffling a list: list.shuffle()
		"""
		return random.shuffle(self.getCards())

	def getCard(self):
		"""
		In order to get a random card, you must shuffle first. This only returns
		the cards in order backwards.
		"""
		return self.deck.pop()
