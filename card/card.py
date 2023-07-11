"""
caption

Args

"""
import random
from collections import defaultdict

class card:
    def __init__(self, cards, member, given):
        self.cards = cards
        self.member = member
        if given == 0:
            self.ALL_FLAG = True
            self.given, mod = divmod(len(cards), len(member))
            self.mod = mod
            #print(self.mod)
        else:
            self.ALL_FLAG = False
            self.given = given
            #print(self.given)

    def show_hand(self, hand, show_player):
        """
        Args:

        Returns:
            
        Raises:

        Yields:
            
        Example:
            draw = Cards.draw(player_hands, member[0], 26)
        """
        return hand[show_player]

    def show_deck(self):
        """
        Args:

        Returns:
            
        Raises:

        Yields:
            
        Example:
            draw = Cards.draw(player_hands, member[0], 26)
        """
        return self.cards

    def check_deck(func):
        """
        Args:

        Returns:
            
        Raises:

        Yields:
            
        Example:
            draw = Cards.draw(player_hands, member[0], 26)
        """
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                print("ドローできるカードがありません。")
        return wrapper

    def partition(self) -> object :
        """
        Args:
            None
        Returns:
            object(dict)
        Raises:
            None
        Yields:
            プレイヤーと初期ドロー数を設定して
        Example:
            draw = Cards.draw(player_hands, member[0], 26)
        """
        deck = self.cards
        mem_hand = defaultdict(list)
        for count in range(0, self.given):
            for member_cards in self.member:
                hand = []
                take = deck.pop(random.randrange(0, len(deck)))
                hand.append(take)
                mem_hand[member_cards].append(take)
            if self.ALL_FLAG:
                for count in range(1, self.mod + 1):
                    take = deck.pop(random.randrange(0, count))
                    for mod_cards in random.sample(self.member, self.mod):
                        mem_hand[mod_cards].append(take)
                        self.mod -= 1
        return dict(mem_hand)

    @check_deck
    def draw(self, add_card_dict: dict, draw_player, draw_count: int):
        """
        Args:

        Returns:
            
        Raises:

        Yields:
            
        Example:
            draw = Cards.draw(player_hands, member[0], 26)
        """
        for count in range(0, draw_count):
            hand = []
            take = self.cards.pop(random.randrange(0, len(self.cards)))
            hand.append(take)
            add_card_dict[draw_player].append(take)
        return dict(add_card_dict)

if __name__ == "__main__":
    cards = [
	's1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11','s12','s13',
	'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13',
	'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10','h11','h12','h13',
	'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10','d11','d12','d13'
	]
    member = ['a', 'b', 'c', 'd', 'e']
    given = 0
    CardIns = card(cards, member, given)

    print(CardIns.partition())
