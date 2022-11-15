from board.board import Board

class ServerBoard(Board):

    def __init__(self):
        super().__init__()
        self.__placed = 0
        self.__winner = '-'


    def place(self, i, j, symbol):
        super().place(i, j, symbol)
        self.__placed += 1

    def __check_if_game_over_on_diagonals(self):
        if self._data[1][1] == ' ':
            return False
        
        if self._data[0][0] == self._data[1][1] and self._data[0][0] == self._data[2][2]:
            self.__winner = self._data[1][1]
            return True
        
        if self._data[0][2] == self._data[1][1] and self._data[0][2] == self._data[2][0]:
            self.__winner = self._data[1][1]
            return True

        return False

    def __check_if_game_over_on_rows(self):
        for i in range(3):
            if self._data[i][0] == self._data[i][1] and self._data[i][2] == self._data[i][0]:
                if self._data[i][0] != ' ':
                    self.__winner = self._data[i][0]
                    return True

        return False

    def __check_if_game_over_on_cols(self):
        for i in range(3):
            if self._data[0][i] == self._data[1][i] and self._data[2][i] == self._data[0][i]:
                if self._data[0][i] != ' ':
                    self.__winner = self._data[0][i]
                    return True
                    
        return False

    def is_full(self):
        return self.__placed == 9

    def check_if_game_over(self):
        if self.__check_if_game_over_on_diagonals() == True:
            return self.__winner
        
        if self.__check_if_game_over_on_cols() == True:
            return self.__winner
        
        if self.__check_if_game_over_on_rows() == True:
            return self.__winner

        if self.__placed == 9:
            return self.__winner
        
        return 'c'


    def minimax(self, depth, isMax) :
        score = self.check_if_game_over()
    
        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 'O') :
            return 10
    
        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == 'X') :
            return -10
    
        # If there are no more moves and no winner then
        # it is a tie
        if (score == '-') :
            return 0
    
        # If this maximizer's move
        if (isMax) :    
            best = 1000
    
            # Traverse all cells
            for i in range(3) :        
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self._data[i][j]==' ') :
                    
                        # Make the move
                        self._data[i][j] = 'O'
    
                        # Call minimax recursively and choose
                        # the maximum value
                        best = min(best, self.minimax(depth + 1, not isMax))
    
                        # Undo the move
                        self._data[i][j] = ' '
                        self.__winner = '-'
            return best
    
        # If this minimizer's move
        else :
            best = -1000
    
            # Traverse all cells
            for i in range(3) :        
                for j in range(3) :
                
                    # Check if cell is empty
                    if (self._data[i][j]==' ') :
                    
                        # Make the move
                        self._data[i][j] = 'X'
    
                        # Call minimax recursively and choose
                        # the minimum value

                        best = max(best, self.minimax(depth + 1, not isMax))
    
                        # Undo the move
                        self._data[i][j] = ' '
                        self.__winner = '-'
            return best
 
    # This will return the best possible move for the player
    def find_best_move(self) :
        best_value = -1000
        best_move = (-1, -1)
    
        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3) :    
            for j in range(3) :
            
                # Check if cell is empty
                if (self._data[i][j] == ' ') :
                
                    # Make the move
                    self._data[i][j] = 'O'

                    if self.check_if_game_over() == 'O':
                        best_move = (i, j)
                        self._data[i][j] = ' '
                        self.__winner = '-'
                        return best_move
    
                    # compute evaluation function for this
                    # move.
                    move_value = self.minimax(0, False)
    
                    # Undo the move
                    self._data[i][j] = ' '
                    self.__winner = '-'
    
                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (move_value > best_value) :               
                        best_move = (i, j)
                        best_value = move_value
    
        return best_move
    
    def __str__(self):
        return super().__str__()

    
        
