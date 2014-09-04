from the_resistance import *

# number of games you want to run
n = 10000

num_successes = 0
for i in range(n):
  game = Resistance_Game(six_players)
  game.play_game()
  num_successes += game.game_won

prob_resistance_win = float(num_successes)/n

print "The resisance winning percentage: " + str(prob_resistance_win * 100) + "%"