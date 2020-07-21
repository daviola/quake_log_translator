import unittest
from game import Game, GameReporter, Kill, Player, MEANS

class testReporter(unittest.TestCase):
    def setUp(self):
        self.game1 = Game()
        player1 = Player('John')
        player2 = Player('Paul')
        self.game1.players["1"] = player1
        self.game1.players["2"] = player2
        self.game1.kills.append(Kill('1', '2', '5'))
        self.game1.kills.append(Kill('1', '2', '6'))
        self.game1.kills.append(Kill('1', '2', '7'))
        self.game1.kills.append(Kill('1', '2', '8'))
        self.game1.kills.append(Kill('2', '1', '2'))
        self.game1.proccess_kills()
    def testType(self):
        self.assertEqual(type(GameReporter().report('game_1', self.game1)), dict)
        self.assertEqual(type(GameReporter().report('game_1', self.game1)['game_1']), dict)
        self.assertEqual(type(GameReporter().report('game_1', self.game1)['game_1']['kills']), dict)
        self.assertEqual(type(GameReporter().report('game_1', self.game1)['game_1']['total_kills']), int)
        self.assertEqual(type(GameReporter().report('game_1', self.game1)['game_1']['players']), list)
    def testContents(self):
        self.assertEqual(GameReporter().report('game_1', self.game1)['game_1']['total_kills'], 5)
        self.assertEqual(GameReporter().report('game_1', self.game1)['game_1']['kills'], {'John':4, "Paul":1})
        self.assertEqual(GameReporter().report('game_1', self.game1)['game_1']['players'], ['John', 'Paul'])
        self.assertIn(MEANS[5], GameReporter().report('game_1', self.game1)['game_1']['kills_by_mean'])
        self.assertIn(MEANS[6], GameReporter().report('game_1', self.game1)['game_1']['kills_by_mean'])
        self.assertIn(MEANS[7], GameReporter().report('game_1', self.game1)['game_1']['kills_by_mean'])
        self.assertIn(MEANS[8], GameReporter().report('game_1', self.game1)['game_1']['kills_by_mean'])
        self.assertIn(MEANS[2], GameReporter().report('game_1', self.game1)['game_1']['kills_by_mean'])
        self.assertEquals(GameReporter().report('game_1', self.game1)['game_1']['kills_by_mean'][MEANS[2]], 1)
    def testGetPlayers(self):
        self.assertEquals(type(GameReporter().get_players(self.game1)), list)
        self.assertEquals(len(GameReporter().get_players(self.game1)), 2)
    def testGetKills(self):
        self.assertEquals(type(GameReporter().get_kills(self.game1)), dict)
        self.assertEquals(len(GameReporter().get_kills(self.game1)), 2)
    def testGetKillsByMean(self):
        self.assertEquals(type(GameReporter().get_kills_by_mean(self.game1)), dict)
        self.assertEquals(len(GameReporter().get_kills_by_mean(self.game1)), 5)


if __name__ == '__main__':
    unittest.main()