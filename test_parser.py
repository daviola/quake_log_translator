import unittest
from log_parser import LogParser

class testParser(unittest.TestCase):
    def setUp(self):
        self.parser = LogParser('games.log')
    def test_load(self):
        self.assertEqual(self.parser.filename, 'games.log')
        self.assertEqual(self.parser.games, [])
        self.assertEqual(self.parser.content, '')
        self.parser.load_to_memory()
        self.assertNotEqual(self.parser.content, '')
    def test_import(self):        
        self.assertEqual(len(self.parser.games), 0)
        self.parser.load_to_memory()
        self.parser.import_games()
        self.assertEqual(len(self.parser.games), 21)
    def test_import_without_load(self):
        self.parser.import_games()
        self.assertEqual(len(self.parser.games), 0)
if __name__ == '__main__':
    unittest.main()
