from json import load
from collections import defaultdict
from random import randrange, sample, choice
import copy

class Game:
    def __init__(self, choice_rule):
        with open('config\cards.json') as cards:
            self.deck = load(cards)

        with open('config\members.json') as members:
            self.players = load(members)

        with open('config\game_rules.json') as rule:
            self.rule = load(rule)

        if choice_rule in list(self.rule.keys()):
            self.rules = self.rule[choice_rule]
        else:
            print(list(self.rules.keys()))

    def setting(self):
        return list(self.rules.values())

    def start(self):
        hand, draw, min_player, max_player, clockwise = self.setting()
        print(hand)
        self.throw(hand)

    def throw(self, hand):
        suit_and_number = defaultdict(list)
        player_hand = defaultdict(dict)

        for i in range(0, hand):
            for mem_cnt in self.players:
                choice_suit = choice(list(self.deck.keys()))

                choose_num = self.deck[choice_suit].pop(randrange(0, len(self.deck[choice_suit])))
                suit_and_number[choice_suit].append(choose_num)

                if choice_suit in player_hand[mem_cnt['name']]:
                    player_hand[mem_cnt['name']][choice_suit].append(choose_num)
                    
                else:
                    player_hand[mem_cnt['name']].update(dict(suit_and_number))
                suit_and_number.clear()

        print(player_hand)

if __name__ == '__main__':
    a = Game('black_jack')
    s = a.start()