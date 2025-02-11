import unittest
from src import spotify

"""
Testing the little functionality I am able to 
test out of what was supposed to be the Spotify-API-Utilizing
recommendation generator
"""

class MyTestCase(unittest.TestCase):

    def test_get_id(self):
        test_id = "3x4Rb5sAP4LGXPVMmAtdQA"
        self.assertEqual(test_id, spotify.get_song_id("point blank", "ericdoa"))

if __name__ == '__main__':
    unittest.main()