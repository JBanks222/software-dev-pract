"""
Jalen Banks
March 15, 2026
project 2 part 2
"""

import os
import importlib.util
import unittest

# Load Connect4 from part1/main.py without requiring package imports.
PART1_MAIN = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part1", "main.py"))
SPEC = importlib.util.spec_from_file_location("connect4_main", PART1_MAIN)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
Connect4 = MODULE.Connect4


class TestConnect4WinConditions(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_horizontal_win(self):
        row = self.game.ROWS - 1
        for col in range(4):
            self.game.board[row][col] = "X"

        self.assertTrue(self.game.check_win("X"))

    def test_vertical_win(self):
        col = 0
        for row in range(4):
            self.game.board[row][col] = "O"

        self.assertTrue(self.game.check_win("O"))

    def test_diagonal_win_top_left_to_bottom_right(self):
        for i in range(4):
            self.game.board[i][i] = "X"

        self.assertTrue(self.game.check_win("X"))

    def test_diagonal_win_bottom_left_to_top_right(self):
        # Coordinates: (5,0), (4,1), (3,2), (2,3)
        for i in range(4):
            self.game.board[self.game.ROWS - 1 - i][i] = "O"

        self.assertTrue(self.game.check_win("O"))

    def test_no_win(self):
        self.game.board[self.game.ROWS - 1][0] = "X"
        self.game.board[self.game.ROWS - 1][1] = "O"
        self.game.board[self.game.ROWS - 1][2] = "X"
        self.game.board[self.game.ROWS - 1][3] = "O"

        self.assertFalse(self.game.check_win("X"))
        self.assertFalse(self.game.check_win("O"))


class TestConnect4DropChip(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()

    def test_successful_chip_drop(self):
        success = self.game.drop_chip(1)

        self.assertTrue(success)
        self.assertEqual(self.game.board[self.game.ROWS - 1][0], "X")

    def test_full_column_returns_false(self):
        for _ in range(self.game.ROWS):
            self.assertTrue(self.game.drop_chip(1))

        self.assertFalse(self.game.drop_chip(1))

    def test_invalid_column_returns_false(self):
        self.assertFalse(self.game.drop_chip(0))
        self.assertFalse(self.game.drop_chip(self.game.COLS + 1))
        self.assertFalse(self.game.drop_chip(-1))

    def test_full_board_no_more_chips_can_be_dropped(self):
        # Fill every slot directly to simulate a full board state.
        for row in range(self.game.ROWS):
            for col in range(self.game.COLS):
                self.game.board[row][col] = "X"

        self.assertTrue(self.game.is_full())
        self.assertFalse(self.game.drop_chip(1))


if __name__ == "__main__":
    unittest.main()

# Test Results Documentation:
# - Framework: unittest
# - Scope covered: horizontal/vertical/diagonal/no-win conditions and drop_chip behavior
#   for successful drop, full column, invalid columns, and full-board scenario.
# - Execution status: PASS (9/9 tests passed).
# - Command used: /workspaces/software-dev-pract/.venv/bin/python -m unittest -v test_connect4_unittest.py
# - Bugs/issues identified: None during this test run.
