import unittest
from proj.youtubeproj import channel, search, populate_dict, videos

class TestFileName(unittest.TestCase):
    def test_channel(self):
        with self.assertRaises(KeyError):
          channel('1@!')

    def test_search(self):
      self.assertEqual('1@!', None)

    def test_populate_dict(self):
        self.assertEqual(populate_dict({}), {})
        with self.assertRaises(KeyError):
          populate_dict({'bad' : 'input'})
        with self.assertRaises(Exception):
          populate_dict('[]')

    def test_videos(self):
        self.assertEqual(videos({}), {})
        with self.assertRaises(Exception):
          videos('[]'), 
        
if __name__ == '__main__':
    unittest.main()