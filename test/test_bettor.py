import unittest

from src.bettor import Bettor

class TestBettor(unittest.TestCase):

    def test_init_bettor(self):
        id = 123456789
        name = 'test_bettor'
        bettor = Bettor(id, name)

        self.assertEqual(bettor.id, id)
        self.assertEqual(bettor.name, name)

    def test_update_name(self):
        id = 123456789
        name = 'test_bettor'
        new_name = 'test_new_name'

        bettor = Bettor(id, name)
        bettor.update_name(new_name)

        self.assertEqual(bettor.name, new_name)

    def test_equal_perfect(self):
        id = 123456789
        name = 'test_bettor'

        bettor_1 = Bettor(id, name)
        bettor_2 = Bettor(id, name)

        self.assertEqual(bettor_1, bettor_2)
    
    def test_equal_same_id_diff_name(self):
        id = 123456789
        name_1 = 'test_bettor_1'
        name_2 = 'test_bettor_2'

        bettor_1 = Bettor(id, name_1)
        bettor_2 = Bettor(id, name_2)

        self.assertEqual(bettor_1, bettor_2)
    
    def test_not_equal(self):
        id_1 = 123456789
        id_2 = 987654321
        name = 'test_bettor'

        bettor_1 = Bettor(id_1, name)
        bettor_2 = Bettor(id_2, name)

        self.assertNotEqual(bettor_1, bettor_2)
