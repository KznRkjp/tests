import unittest
import sys
sys.path.insert(0, './tests')
import tictactoe

board = [[2, 2, 0], [1, 0, 2], [1, 1, 0]] #все ок, игра идет
board_x = [[1, 2, 2], [1, 0, 2], [1, 1, 0]] #все ок, выйграл Х
board_false = [[2, 2, 0], [1, 0, 2], [1, 1, 0],[1, 1, 0]] #доска сломана
board_0_x = [[2, 1, 0], [1, 2, 2], [1, 2, 0]] #ноликов больше - ошибка
board_other = [[2, 2, 2], [1, 1, 1], [0, 0, 0]] #странная ситуация - выйграл и Х и 0

class MyTictactoeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("[1,2,3,4,5 - начинаем проверять]")
        print("v" * 30)
    @classmethod
    def tearDownClass(cls):
        print("^" * 30)
        print("[закончили проверять]")

    def test_validate_board_type(self):
        """ проверка типа bool"""
        self.assertIsInstance(tictactoe.validate_board(board), bool)

    def test_validate_board_result_true(self):
        """проверка правильности результата True """
        self.assertTrue(tictactoe.validate_board(board) is True)

    def test_validate_board_result_false(self):
        """проверка правильности результата False"""
        self.assertFalse(tictactoe.validate_board(board_false) is True)

    def test_validate_board_count_0_X(self):
        """проверка числа «ноликов» и «крестиков»"""
        self.assertFalse(tictactoe.validate_board(board_0_x) is True)

    def test_game_finished(self):
        """проверка  формат вывода (числовой)"""
        self.assertIsInstance(tictactoe.game_finished(board), int)

    def test_game_finished_still_going(self):
        """проверка 0, если на поле ещё идёт игра"""
        self.assertEqual(tictactoe.game_finished(board), 0)

    def test_game_finished_someone_wins(self):
        """проверка  1 или 2, если выиграл какой-то игрок"""
        self.assertEqual(tictactoe.game_finished(board_x), 1 or 2)

    def test_game_finished_something_else(self):
        """проверка других случаев, где мы от функции ждём -1"""
        self.assertEqual(tictactoe.game_finished(board_other), -1)

    def test_render_board(self):
        """проверка  формат вывода (str)"""
        self.assertIsInstance(tictactoe.render_board(board), str)




if __name__ == "__main__":
    unittest.main()
