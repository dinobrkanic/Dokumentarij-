import unittest
from dokumentarij import Dokumentarij 

class DokumentarijTestCase(unittest.TestCase):

    def test_same_name(self):
        game_test = DokumentarijContoller()
        name1= game_test.get_new_name()
        name2= game_test.get_new_name() 
        self.assertNotEqual(str(name1), str(name2), "Potrebno je unijeti različita imena")
    
    def test_size_of_names(self):
        game_test = Dokumentarij()
        deck = game_test.create_names()
        self.assertEqual(len(names), 200, "Dokumentarij sadrži 200 imena")

    
if __name__ == "__main__":
    unittest.main()
    