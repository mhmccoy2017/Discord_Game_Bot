class Player:
	'''
	A player in the discord bot games

	Parameters:
		ID : Member of the discord channel who is playing the game
	'''

	def __init__(self, member):
		self.member = member
		self.hand = []
		self.is_playing = False

	def __str__(self):
		return self.member.name

	def add_card(self, deck):
		self.hand.append(deck.remove_card())
		print(f'{self.hand}')
