class Player:
	def __init__(self, name, buy_in):
		#parameters: score, cards, name, money,
		self.score = 0
		self.cards = []
		self.name = str(name)
		self.money = int(buy_in)

	def __str__(self):
		return str((this.score, this.cards, this.name, this.money))

	def updateMoney(self, quantity):
		"""
		quantity can be a negative number (lost).
		Returns nothing
		"""
		self.money += quantity

	def getScore(self):
		"""
		"""
		return self.score

	def isBust(self):
		"""
		"""
		if self.score > 21:
			return 1
		# elif self.score == 21:
		# 	return -1
		else:
			return 0

		# sum = 0
		# for card in self.cards:
		# 	if card.getFace == "A":
		# 		#special case hehehe
		# 	else:
		# 		sum += card.getValue()
		# 	if sum > 21:
		# 		return True
		# 	elif sum <= 21:
		# 		return False

	def resetRound(self):
		"""
		After each round, reset each player's cards and score
		"""
		self.cards = []
		self.score = 0

	def getCards(self):
		"""
		Just returns the cards list
		"""
		return self.cards

	def hitMe(self, card):
		"""
		"""
		self.cards.append(card)
		# print([x.getFace() for x in self.cards])
		val = card.getValue()
		if self.score > 10 and val == -1: #addressing the special ace case
			self.score += 1
		elif val == -1:
			self.score += 11
		else:
			self.score += card.getValue()
		#Engineering note: If the card happens to be a 1, the tuple simulating both scores will be added
		#score will thus contian a tuple with two entries, one with A = 1, another with A = 11

	def getMoney(self):
		"""
		"""
		return self.money

	def getName(self):
		"""
		"""
		return self.name
