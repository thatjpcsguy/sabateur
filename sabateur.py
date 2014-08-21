import random
import json


#CONSTS
BOARD_WIDTH = 9
BOARD_HEIGHT = 5



class Game:
	def __init__(self):
		self._hands = 0
		self._players = []
		self._board = []
		self._deck = []

	def print_board(self):
		for i in self._board:
			print i

	def register_player(self, player):
		self._players.append(player)


	def setup_board(self):
		for i in range(BOARD_HEIGHT):
			self._board.append([])
			for j in range(BOARD_WIDTH):
				self._board[i].append('.')

	def place_card(self, x, y, card):
		self._board[x][y] = card

	def place_gold(self):
		self.place_card(2, 0, TileCard(left=True, right=True, up=True, down=True, indestructable=True))
		gold_cards = []
		gold_cards.append(TileCard(up=True, left=True, indestructable=True))
		gold_cards.append(TileCard(down=True, left=True, indestructable=True))
		gold_cards.append(TileCard(gold=True, indestructable=True))
		random.shuffle(gold_cards)

		self.place_card(0, 8, gold_cards.pop())
		self.place_card(2, 8, gold_cards.pop())
		self.place_card(4, 8, gold_cards.pop())


	def shuffle_deck(self):
		#TILE CARDS
		self._deck.append(TileCard(down=True, blocked=True))
		self._deck.append(TileCard(down=True, left=True, up=True, blocked=True))
		self._deck.append(TileCard(down=True, left=True, up=True, right=True, blocked=True))
		self._deck.append(TileCard(down=True, right=True, blocked=True))
		self._deck.append(TileCard(down=True, left=True, blocked=True))
		self._deck.append(TileCard(left=True, blocked=True))
		self._deck.append(TileCard(up=True, down=True, blocked=True))
		self._deck.append(TileCard(up=True, left=True, right=True, blocked=True))
		self._deck.append(TileCard(left=True, right=True, blocked=True))


		for i in range(3):
			self._deck.append(TileCard(left=True, right=True))

		for i in range(4):
			self._deck.append(TileCard(down=True, right=True))
			self._deck.append(TileCard(up=True, down=True))

		for i in range(5):
			self._deck.append(TileCard(up=True, down=True, right=True))
			self._deck.append(TileCard(down=True, left=True))
			self._deck.append(TileCard(up=True, down=True, right=True, left=True))
			self._deck.append(TileCard(left=True, right=True, up=True))			

		#ACTION CARDS
		for i in range(3):
			self._deck.append(ActionCard(pick=1))
			self._deck.append(ActionCard(pick=-1))
			self._deck.append(ActionCard(cart=1))
			self._deck.append(ActionCard(cart=-1))
			self._deck.append(ActionCard(lamp=1))
			self._deck.append(ActionCard(lamp=-1))
			self._deck.append(ActionCard(avalanche=True))

		for i in range(5):
			self._deck.append(ActionCard(reveal=True))



		#DO SHUFFLE
		random.shuffle(self._deck)

	def draw_card(self):
		return self._deck.pop()

	def __repr__(self):
		return '"GAME!"'



class ActionCard:
	def __init__(self, pick=0, cart=0, lamp=0, reveal=False, avalanche=False):
		self._pick = pick
		self._cart = cart
		self._lamp = lamp
		self._reveal = reveal
		self._avalanche = avalanche

	def __repr__(self):
		if self._pick > 0:
			return "PU"
		elif self._pick < 0:
			return "PB"

		if self._cart > 0:
			return "CU"
		elif self._cart < 0:
			return "CB"

		if self._lamp != 0:
			return "cart: "+str(self._lamp)

		if self._reveal:
			return "R"

		if self._avalanche:
			return "A"


class Player:
	def __init__(self, name, game, sabateur=False):
		self._name = name
		self._sabateur = sabateur
		self._hand = []
		self._game = game
		for i in range(4):
			self._hand.append(game.draw_card())

		self._gold = 0

		self._pick = 1
		self._lamp = 1
		self._cart = 1


	def view_hand(self):
		return self._hand

	def calculate_view(self):
		hand = []
		for i in self._hand:
			hand.append(str(i))

		return {'lamp':self._lamp,
				'cart':self._cart,
				'pick':self._pick,
				'gold':self._gold,
				'name':self._name,
				'hand':hand}


class TileCard:
	def __init__(self, left=False, right=False, up=False, down=False, blocked=False, indestructable=False, gold=False):
		self._left = left
		self._right = right
		self._up = up
		self._down = down
		self._blocked = blocked
		self._indesctructable = indestructable
		self._gold = gold

	def flip_card(self):
		print self
		temp = self._left
		self._left = self._right
		self._right = temp
		temp = self._up
		self._up = self._down
		self._down = temp

		print self

	def __repr__(self):
		return str(int(self._up))+str(int(self._down))+str(int(self._left))+str(int(self._right))+str(int(self._blocked))+str(int(self._indesctructable))+str(int(self._gold))


if __name__ == '__main__':
	game = Game()
	game.setup_board()
	
	game.place_gold()
	game.print_board()
	game.shuffle_deck()

	game.register_player(Player("James", game))
	game.register_player(Player("Willix", game))
	game.register_player(Player("Jimmy", game))
	game.register_player(Player("Martin", game))

	print
	print game._players[0].calculate_view()
	print
	print game._players[1].calculate_view()
	



