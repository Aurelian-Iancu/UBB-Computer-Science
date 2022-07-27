import random
import copy


class Strategy:
    @staticmethod
    def get_input(board):
        """
        Here we analyse if the computer should do a random choice or it should try to block the winning move
        :param board: the board
        :return: a move
        """
        winner = Strategy.get_win(board)
        if winner is not None:
            return winner
        moves = board.get_move_list()
        return random.choice(moves)

    @staticmethod
    def get_win(board):
        """
        Here we analyse if create a copy of the map with all possible moves and if one is a winning move, then we take it
        :param board: a board
        :return: The winning move, none if there is no such thing
        """
        moves = board.get_move_list()
        for move in moves:
            board_copy = copy.deepcopy(board)
            board_copy.execute_move(move[0], move[1])
            if board_copy.is_game_won() is True:
                return move

        return None


