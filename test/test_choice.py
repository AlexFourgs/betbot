import unittest

from src.choice import Choice, NegativeNbBetException

class TestChoice(unittest.TestCase):

    def test_init_choice(self):
        choice_name = 'test_choise'
        index = 0
        choice = Choice(choice_name, index)

        self.assertEqual(choice.choice, choice_name)
        self.assertEqual(choice.index, index)
        self.assertEqual(choice.nb_bet, 0)

    def test_bet_on(self):
        choice = Choice('test_choice', 0)
        choice.bet_on()

        self.assertEqual(choice.nb_bet, 1)

    def test_remove_bet(self):
        choice = Choice('test_choice', 0)
        choice.bet_on()
        choice.remove_bet()

        self.assertEqual(choice.nb_bet, 0)

    def test_remove_bet_neg(self):
        choice = Choice('test_choice', 0)
        choice.bet_on()
        choice.remove_bet()
        self.assertEqual(choice.nb_bet, 0)

        with self.assertRaises(NegativeNbBetException):
            choice.remove_bet()
            self.assertEqual(choice.nb_bet, 0)
