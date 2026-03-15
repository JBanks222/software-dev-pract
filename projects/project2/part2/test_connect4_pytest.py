"""
Jalen Banks
March 15, 2026
project 2 part 2
"""

import os
import importlib.util

# Load Connect4 from part1/main.py without requiring package imports.
PART1_MAIN = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "part1", "main.py"))
SPEC = importlib.util.spec_from_file_location("connect4_main", PART1_MAIN)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC is not None and SPEC.loader is not None
SPEC.loader.exec_module(MODULE)
Connect4 = MODULE.Connect4


def test_horizontal_win():
    game = Connect4()
    row = game.ROWS - 1
    for col in range(4):
        game.board[row][col] = "X"

    assert game.check_win("X") is True


def test_vertical_win():
    game = Connect4()
    col = 0
    for row in range(4):
        game.board[row][col] = "O"

    assert game.check_win("O") is True


def test_diagonal_win_top_left_to_bottom_right():
    game = Connect4()
    for i in range(4):
        game.board[i][i] = "X"

    assert game.check_win("X") is True


def test_diagonal_win_bottom_left_to_top_right():
    game = Connect4()
    for i in range(4):
        game.board[game.ROWS - 1 - i][i] = "O"

    assert game.check_win("O") is True


def test_no_win():
    game = Connect4()
    game.board[game.ROWS - 1][0] = "X"
    game.board[game.ROWS - 1][1] = "O"
    game.board[game.ROWS - 1][2] = "X"
    game.board[game.ROWS - 1][3] = "O"

    assert game.check_win("X") is False
    assert game.check_win("O") is False


def test_successful_chip_drop():
    game = Connect4()

    success = game.drop_chip(1)

    assert success is True
    assert game.board[game.ROWS - 1][0] == "X"


def test_full_column_returns_false():
    game = Connect4()
    for _ in range(game.ROWS):
        assert game.drop_chip(1) is True

    assert game.drop_chip(1) is False


def test_invalid_column_returns_false():
    game = Connect4()

    assert game.drop_chip(0) is False
    assert game.drop_chip(game.COLS + 1) is False
    assert game.drop_chip(-1) is False


def test_full_board_no_more_chips_can_be_dropped():
    game = Connect4()
    for row in range(game.ROWS):
        for col in range(game.COLS):
            game.board[row][col] = "X"

    assert game.is_full() is True
    assert game.drop_chip(1) is False


# Test Results Documentation:
# - Framework: pytest
# - Scope covered: horizontal/vertical/diagonal/no-win conditions and drop_chip behavior
#   for successful drop, full column, invalid columns, and full-board scenario.
# - Execution status: PASS (9/9 tests passed).
# - Command used: /workspaces/software-dev-pract/.venv/bin/python -m pytest -q test_connect4_pytest.py
# - Bugs/issues identified: None during this test run.
