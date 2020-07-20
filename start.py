from log_parser import LogParser
from game import GameReporter
import pprint, sys
p = LogParser("games.log")
p.load_to_memory()
p.import_games()
def start():
    while True:
        print('loading from games.log...')
        select = input( "Please select one of the following options\n"+
                        "   1 - Simple report\n"+
                        "   2 - Simple Report Paginated\n"+
                        "   3 - Detailed Report Paginated\n"+
                        "   4 - Single Report By ID\n"+
                        "   5 - Overall Ranking\n"+
                        "   6 - Exit\n")
        if select == '1':
            simple_report()    
        if select == '2':
            simple_report_paginated()    
        if select == '3':
            detailed_report_paginated()    
        if select == '4':
            single_report()
        if select == '5':
            overall_ranking()
        if select == '6':
            sys.exit(0)
# Simple report of all games without pagination
def simple_report():
    i = 0    
    print("==SIMPLE REPORT==")
    for game in p.games:
        game.proccess_kills()
        pprint.pprint(GameReporter().simple_report(("game_"+str(i)), game))
        i +=1 
    input("\npress enter to return")
    return       
        
def simple_report_paginated():
    i = 0
    j = 0
    print("==SIMPLE REPORT PAGINATED==")
    for game in p.games:
        game.proccess_kills()
        pprint.pprint(GameReporter().simple_report(("game_"+str(i)), game))
        i +=1
        j +=1
        if j == 3:
            j = 0
            input("press enter to continue")
    input("\npress enter to return")
    return

# Single report from ID
def single_report():
    while True:
        select = input('Please type the id as an integer or -1 to return to the previous menu\n')
        try:
            select = int(select)
        except:
            print("Please type the id as an integer")
        if select < 0:
            return
        if select >(len(p.games)-1):
            print("index out of range, select an index between 0 and "+str(len(p.games)-1))
        else:
            print("==SINGLE REPORT==")
            pprint.pprint(GameReporter().report(("game_"+str(select)), p.games[select]))
            input("\nPress enter to return")

def detailed_report_paginated():
    i = 0
    j = 0
    print("==DETAILED REPORT PAGINATED==")
    for game in p.games:
        game.proccess_kills()
        pprint.pprint(GameReporter().report(("game_"+str(i)), game))
        i +=1
        j +=1
        if j == 3:
            j = 0
            input("press enter to continue")
    input("\npress enter to return")
    return

def overall_ranking():
    total_kills = 0
    kills = {}
    for game in p.games:
        game.proccess_kills()
        total_kills += len(game.kills)
        for player in game.players:
            if game.players[player].name not in kills:
                kills[game.players[player].name] = game.players[player].kills
            else:
                kills[game.players[player].name] += game.players[player].kills
    print("==OVERALL RANKING==")                
    pprint.pprint({"total_kills":total_kills, "kills":kills})
    input("\nPress enter to return")

start()