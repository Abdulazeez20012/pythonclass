import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_That_player_is_created(self):
        player = Player("Azeez", "X")
        self.assertEqual(player.name, "Azeez")
        self.assertEqual(player.symbol, "X")


if __name__ == "__main__":
    unittest.main()
