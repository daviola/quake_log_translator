from resource import BREAK_LINE, INIT_GAME, USER_INFO_CHANGED, KILL
from game import Game, Kill, Player
class LogParser():
    def __init__(self, filename):
        self.filename = filename
        self.content = ""
        self.games = []
    def load_to_memory(self):
        try:
            fm = open(self.filename, "r")
            self.content = fm.read()
            fm.close()
        except:
            print("fail to load file: "+self.filename)
    def import_games(self):
        '''Read all the log data to a list of objects'''
        lines = self.content.split('\n')
        game = None
        for line in lines:
            if BREAK_LINE in line:
                pass
            if INIT_GAME in line:
                if game:
                    self.games.append(game)
                game = Game()
                continue
            if USER_INFO_CHANGED in line:
                # get user id and name from line (users can change their names)
                parsed_info = line[line.index(USER_INFO_CHANGED):].split(" ")
                id = parsed_info[1]
                name = parsed_info[2].split('\\')[1]
                # update user data
                if id in game.players:
                    game.players[id].name = name
                else:
                    game.players[id] = Player(name)
                continue
            if KILL in line:
                # Collect Killer Killed and Mean
                parsed_info = line[line.index(KILL):].split(":")[1]
                parsed_info = parsed_info.split(' ')[1:]
                game.kills.append(Kill(parsed_info[0], parsed_info[1], parsed_info[2]))
        if game:
            self.games.append(game)
        

