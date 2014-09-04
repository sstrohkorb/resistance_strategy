from random import *

# For each array that represents a 'mode' of the game (determined by
# the number of players) the first value of the array is the number
# of members, the second is the number ofspies and the following are 
# the amount of people on each mission
five_players = [5,2,2,3,2,3,3]
six_players = [6,2,2,3,4,3,4]
seven_players = [7,3,2,3,3,4,4]
eight_players = [8,3,3,4,4,5,5]
nine_players = [9,3,3,4,4,5,5]
ten_players = [10,4,3,4,4,5,5]

class The_Resistance:

  def __init__(self, game_info):
    self.round_one = game_info[2]
    self.round_two = game_info[3]
    self.round_three = game_info[4]
    self.round_four = game_info[5]
    self.round_five = game_info[6]

    num_spies = game_info[1]
    num_players = game_info[0]

    # spy selection
    spy_indicies = []
    spy_indicies.append(randint(0, num_players - 1))
    for i in range(num_spies-1):
      while True:
        rand_index = randint(0, num_players - 1)
        if rand_index not in spy_indicies:
          break
      spy_indicies.append(rand_index)

    # making the list of players
    self.players = []
    for i in range(num_players):
      if i in spy_indicies:
        self.players.append(Player('spy'))
      else:
        self.players.append(Player('resistance'))
      

class Player:

  def __init__(self, identity):
    self.identity = identity    # either 'spy' or 'resistance'

  def __str__(self):
    return self.identity


game = The_Resistance(six_players)
for player in game.players:
  print player



