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

class GameReporter():    
    def report(self, game_id, game):
        report = {}
        report[game_id] =  {'total_kills': len(game.kills),
                            'players':self.get_players(game),
                            'kills': self.get_kills(game),
                            'kills_by_mean': self.get_kills_by_mean(game)}
        return report
    def simple_report(self, game_id, game):
        report = {}
        report[game_id] =  {'total_kills': len(game.kills),
                            'players':self.get_players(game),
                            'kills': self.get_kills(game)}
        return report
    def get_players(self, game):
        players = []
        for player in game.players:
            players.append(game.players[player].name)
        return players
    def get_kills(self, game):
        kills = {}
        for player in game.players:
            kills[game.players[player].name] = game.players[player].kills
        return kills
    def get_kills_by_mean(self, game):
        kills_by_mean = {}
        for kill in game.kills:
            if MEANS[int(kill.mean)] not in kills_by_mean:
                kills_by_mean[MEANS[int(kill.mean)]] =1
            else:
                kills_by_mean[MEANS[int(kill.mean)]] +=1
        return kills_by_mean
        