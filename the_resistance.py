from random import *
from spy import *
from resistance_member import *

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

class Resistance_Game:

  def __init__(self, game_info):
    self.round_counts = []
    for i in range(5):
      self.round_counts.append(game_info[i + 2])

    # represents the leader in the self.players array, will increment
    # by one after every turn
    self.leader_index = 0

    self.round = 0          # the round the game state is currently in
    self.missions_won = 0   # missions won by the resistance
    self.missions_lost = 0  # missions lost by the resistance

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
        self.players.append(Spy())
      else:
        self.players.append(Resistance_Member())

  def play_game(self):
    for i in range(5):
      play_round()
      self.round += 1
      self.leader_index += 1

  def play_round(self):
    while True:
      # The leader selects the team going on the mission
      mission_team = self.players[self.leader_index].select_mission_team(self.round, self.round_counts[self.round], self.missions_lost)

      # The players vote on the team
      vote_total = 0
      for player in self.players:
        vote_total += player.vote_on_mission(self.round, self.missions_lost, mission_team)


      # If the vote succeeds, the players will go on the mission
      # If not, the leadership changes and we repeat this process

    # The players go on the mission and submit their mission pass/fail



game = Resistance_Game(six_players)
for player in game.players:
  print player



