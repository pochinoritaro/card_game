from card import card

TRUMP = [
's1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13',
'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13',
'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13',
'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13'
]
member = ['a', 'b', 'c', 'd', 'e']
given = 2

Cards = card(TRUMP, member, given)
car = Cards.show()
player_hands = Cards.partition()

print(player_hands)
Cards.draw(player_hands, member[0], 2)
