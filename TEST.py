import PROJECT_CODE as pc
import unittest
import pickle as pk

model = pk.load(open('model.sav', 'rb'))

class Tests(unittest.TestCase):
    def test_search(self):
        self.assertEqual(pc.search_num('Wii', pc.platforms, pc.df.Platform),18)

if __name__ == '__main__':
    unittest.main()
