import simplegui
WIDTH = 840
HEIGHT = 560
LIVES = 3

#Class list: game
#URL https://py3.codeskulptor.org/#user303_48FbQ12A06N4ZQu.py
#Author: Silas
again = True
class Game:
	def ask():
		# after trying to find nice popup box, will have quit and again buttons on side
		pass
	def game():
		while again:
			showWelcomeScreen()
			player = playerStats()
			player.setLife(LIVES)
			while(player.getLife() != 0):
				#play Game
				# needs interaction stuff to affect lives 
				pass
			again = ask("Would you like to play again?")

Game.game()
