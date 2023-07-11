import random
from collections import defaultdict

class CardSet:
	def __init__(self, cards, member, given):
		self.cards = cards
		self.member = member
		if given == 0:
			self.ALL_FLAG = True
			self.given, mod = divmod(len(cards), len(member))
			self.mod = mod
			print(self.mod)
		else:
			self.ALL_FLAG = False
			self.given = given
			print(self.given)
		
	def show_cards(self):
		return self.cards
		
	def partition_card(self) -> object :
		deck = self.cards
		mem_hand = defaultdict(list)
		for count in range(0, self.given):
			for member_cards in self.member:
				hand = []
				take = deck.pop(random.randrange(0, len(deck)))
				hand.append(take)
				mem_hand[member_cards].append(take)
				
		
		if self.ALL_FLAG:
			for count in range(1, self.mod):
				take = deck.pop(random.randrange(0, count))
				for mod_cards in random.sample(self.member, self.mod):
						mem_hand[mod_cards].append(take)
		
		self.cards = deck

		return mem_hand, deck

if __name__ == "__main__":
	cards = [
	's1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13',
	'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13',
	'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13',
	'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13'
	]
	member = ['a', 'b', 'c', 'd', 'e']
	given = 0
	CardIns = CardSet(cards, member, given)
	
	print(CardIns.partition_card())
	print('¥n')
	print(CardIns.partition_card())