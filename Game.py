import simplegui
WIDTH = 840
HEIGHT = 560
LIVES = 3

#Class list: game
#by Silas
again = True
class Game:
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

Game.game
