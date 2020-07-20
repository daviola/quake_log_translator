from resource import MEANS, WORLD_ID

class Game():
    def __init__(self):        
        self.players = {}
        self.kills = []
    def reset_players_kills(self):
        for player in self.players:
            self.players[player].kills = 0       
    def proccess_kills(self): 
        self.reset_players_kills()
        for kill in self.kills:
            if kill.killer == WORLD_ID:
                self.players[kill.killed].kills -=1
            else:
                self.players[kill.killer].kills +=1

class Kill():
    def __init__(self, killer, killed, mean):
        self.killer = killer
        self.killed = killed
        self.mean = mean

class Player():
    def __init__(self, name):
        self.name = name
        self.kills = 0

        