import random

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return (str(self.suit, self.value))

	def getValue(self):
		"""
		Returns the actual integer value of the Card
		"""
		if self.value == "J" or self.value == "Q" or self.value == "K":
			return 10
		if self.value == "A":
			return -1 #this is an enginering decision. I'm not sure how scalable it is. Look at Design Doc.
		else:
			return int(self.value)

	def getSuit(self):
		"""
		returns the card suit
		"""
		return self.suit

	def getFace(self):
		"""
		Returns the actual face value of each card (not the integer)
		"""
		return self.value


	#getValue -- return 11 or 1 for A, 10 for JQK
	#getSuit -- return CLubs, hearts, diamonds, clovers
	#getFace -- return A,J,Q,K etc
