__author__ = 'Zach'

# Player Class
# This holds the player's name, and all of his statistics that will later be printed to an HTML page
class Player:
    def __init__(self, name):
        self.name = name

    def set_minutes(self, mins):
        self.minutes = mins

    def get_minutes(self):
        return self.minutes

    def set_rebounds(self, rebs):
        self.rebounds = rebs

    def get_rebounds(self):
        return self.rebounds

    def set_assists(self, asts):
        self.assists = asts

    def get_assists(self):
        return self.assists

    def set_steals(self, stls):
        self.steals = stls

    def get_steals(self):
        return self.steals

    def set_blocks(self, blks):
        self.blocks = blks

    def get_blocks(self):
        return self.blocks

    def set_turnovers(self, tos):
        self.turnovers = tos

    def get_turnovers(self):
        return self.turnovers

    def set_points(self, pts):
        self.points = pts

    def get_points(self):
        return self.points
