import simplegui
WIDTH = 560
HEIGHT = 800
LIVES = 3

#Class list: game
#URL https://py3.codeskulptor.org/#user303_48FbQ12A06N4ZQu_0.py
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
