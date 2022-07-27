import random
import copy


class Strategy:
    @staticmethod
    def get_input(board):
        winner = Strategy.get_win(board)
        if winner is not None:
            return winner
        moves = board.get_move_list()
        return random.choice(moves)

    @staticmethod
    def get_win(board):
        moves = board.get_move_list()
        for move in moves:
            board_copy = copy.deepcopy(board)
            board_copy.execute_move(move)
            if board_copy.available_moves == 0:
                return move

        return None

