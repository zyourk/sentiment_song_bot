import unittest
from src.web_scraper import LyricScraper
from src.web_scraper import LyricNotFound

"""
Testing for the web scraper of the lyrics. Currently tests grabbing
the lyrics for one short song, as well as that an error is throw when
the song is not found.
More tests will likely be added in the future, perhaps such as special characters
like accent marks and other special song or artist names.
"""

class MyTestCase(unittest.TestCase):

    def test_scrape(self):
        test_lyrics = "What's it like to like yourself\nWithout needing anyone else\nTo tell me I'm doing something right\nOr to set my sights on\nMmm, what's it like"
        self.assertEqual(test_lyrics, LyricScraper.get_lyrics("zeph", "what's it like (demo)"))  # add assertion here

    def test_not_found(self):
        with self.assertRaises(LyricNotFound):
            LyricScraper.get_lyrics("FAKE ARTIST", "VERY FAKE SONG")



if __name__ == '__main__':
    unittest.main()
