import numpy as np

class Board:
    """ Class that represents the game board of Tic Tac Toe """

    playerX = 1
    playerO = -1

    def __init__(self, rows = 3, cols = 3, win_threshold = 3):
        """
            rows (int)
            cols (int)
            win_threshold (int) - Do not change
        """ 
        self.state = np.zeros((rows, cols), dtype=np.int8)
        self.rows = rows
        self.cols = cols
        self.win_threshold = win_threshold

    def getState(self):
        """ Get state of game """
        return self.state
    
    def getPosition(self, x, y):
        """ Get state at position (x,y) """
        return self.state[x,y]

    def setPosition(self, x, y, value):
        """  Set state at position (x,y) with value """
        self.state[x,y] = value

    def getAvailablePos(self):
        """  Get state positions that have no value (non-zero) """
        return np.argwhere(self.state == 0)

    def getStateHash(self, inverted=False):
        """  Get hash key of state """
        factor = 1
        state_hash = 0
        for i in range(self.rows):
            for j in range(self.cols):
                
                if inverted:
                    state_hash -= self.state[i,j]*factor
                else:
                    state_hash += self.state[i,j]*factor
                
                factor = 10*factor
        return state_hash

    def checkWinner(self):
        """  Get winner, if one exists """
        """ TODO: Not general case, only works for 3x3 board """

        symbols = np.unique(self.state)
        symbols = list(symbols[np.nonzero(symbols)])

        for sym in symbols:

            # Check rows
            row= np.any((np.all(self.state == sym, axis=1)))

            # Check columns
            col = np.any((np.all(self.state == sym, axis=0)))

            # Check diagonals
            diag1 = np.array([self.state[0,0], self.state[1,1], self.state[2,2]])
            diag1 = np.all(diag1 == sym)
            
            diag2 = np.array([self.state[0,2], self.state[1,1], self.state[2,0]])
            diag2 = np.all(diag2 == sym)

            # Check if state has winner and return winner in that case
            if row or col or diag1 or diag2:
                return sym
            
        # No winner found
        return 0 

    def checkGameEnded(self):
        """ Check if game has ended by observing if there any possible moves left """
        return len(self.getAvailablePos()) == 0

    def checkWinPossible(self, last_player_value):
        """ 
            Test whether there is a winning move available for the next player.
            Return True if it is available.
            last_player (int)
        """

        # Next player is the negative of last_player_value
        next_player_player = - last_player_value

        winning_move_found = False
        for action in self.getAvailablePos():
            x = action[0]
            y = action[1]

            # Perform action
            self.setPosition(x, y, next_player_player)

            # Check if winning move
            if self.checkWinner() != 0:
                winning_move_found = True

            # Revert action
            self.setPosition(x, y, 0)

            # If found, then return True
            if winning_move_found is True:
                return True

        return False
            
        

    def resetGame(self):
        """ Reset game """
        self.state = np.zeros((self.rows, self.cols), dtype=np.int16)

    def getInvertedState(self):
        """ Return state where player O and X have swapped places """
        return -self.state

    def __str__(self):
        return str(self.state)