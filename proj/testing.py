import unittest
from proj.youtubeproj import channel, search, populate_dict, videos

class TestFileName(unittest.TestCase):
    def test_channel(self):
        self.assertEqual(channel('1@!'), KeyError)
          
    def test_search(self):
        self.assertEqual(search('1@!'), None)

    def test_populate_dict(self):
        self.assertEqual(populate_dict({}), {})
        self.assertEqual(populate_dict({'bad' : 'input'}), KeyError)
        self.assertEqual(populate_dict('[]'), None)
        
    def test_videos(self):
        self.assertEqual(videos({}), {})
        self.assertEqual(videos('[]'), None)
        
if __name__ == '__main__':
    unittest.main()