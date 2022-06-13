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

	def __repr__(self):
		return self.member.name

	def add_card(self, deck):
		'''
		Adds a popped card from the deck to players hand
		Takes deck | Deck as an argument and adds to 
		self.hand
		'''
		self.hand.append(deck.remove_card())
		print(f'{self.hand}')
