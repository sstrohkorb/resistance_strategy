class Spy:

  def __init__(self, num_players, my_index, spy_indicies):
    self.identity = 'spy'
    self.num_players = num_players
    self.my_index = my_index
    self.spy_indicies = spy_indicies

  def __str__(self):
    return self.identity

  def select_mission_team(round, num_on_mission, missions_lost):
    print "Spy selects mission team"

  def vote_on_mission(round, missions_lost, mission_team):
    print "Spy votes on mission"