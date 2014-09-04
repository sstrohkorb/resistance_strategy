from random import *

class Resistance_Member:

  def __init__(self, num_players, my_index, round_counts):
    self.identity = 'resistance'
    self.num_players = num_players
    self.my_index = my_index
    self.round_counts = round_counts

    # game states
    self.round = 0
    self.missions_lost = 0
    self.mission_history = {}

  def __str__(self):
    return self.identity

  def select_mission_team(self):
    mission_team = []
    num_players_on_mission = self.round_counts[self.round]

    # putting myself on the team
    mission_team.append(self.my_index)

    while len(mission_team) < num_players_on_mission:
      rand_player_index = randint(0, self.num_players - 1)
      if rand_player_index not in mission_team:
        mission_team.append(rand_player_index)

    return mission_team

  # Vote 1 for approve, 0 for disapprove
  def vote_on_mission(self, mission_team):
    return 1

  # Return a 'P' or 'F'
  def go_on_mission(self, mission_team):
    return 'P'





