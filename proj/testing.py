import unittest
from youtubeproj.py import channel, search, populate_dict, videos

class TestFileName(unittest.TestCase):
    def test_channel(self):
        self.assertRaises(channel('1@!'), KeyError)

    def test_search(self):
        self.assertRaises(search('1@!'), invalidChannelId)

    def test_populate_dict(self):
        self.assertEqual(populate_dict({}), {})
        self.assertRaises(populate_dict('[]'), Exception)
        self.assertRaises(populate_dict({'bad' : 'input'}), KeyError)

    def test_videos(self):
        self.assertRaises(populate_dict('[]'), Exception)
        self.assertEqual(videos({}), {})
      
if __name__ == '__main__':
    unittest.main()