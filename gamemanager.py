# ####################################################
# DE2-COM2 Computing 2
# Individual project
#
# Title: GameManager
# Authors: Zachary Yamaoka (28th October 2017)
# Last updated: 7th December 2017
# ####################################################

import numpy as np
import gamepieces

class GameManager():

    def  __init__(self, target):

        self.gameboard = target
        self.working_gameboard = gamepieces.load_gameboard(target, 13)
        self.padded_gameboard = gamepieces.load_gameboard(target, 7)
        self.temp_gameboard = None
        self.gamepieces = gamepieces.load_gamepieces()

        W, H = np.array(self.padded_gameboard).shape

        sol = np.empty((W,H), dtype=object)
        for x in range(W):
            for y in range(H):
                sol[x, y] = (0, 0)

        self.solution = sol

        self.complete_piece = np.zeros((7,7))
        self.path = []
        self.counter = 1
        self.piece_counter = 1

        self.i, self.j = self.indexing()
        self.goal = False
        self.row = 0

    def indexing(self):
        field_height = 7
        field_width = 7
        W, H = 7, 7

        i0 = np.repeat(np.arange(field_height), field_width)
        i1 = np.repeat(np.arange(7), 7)

        j0 = np.tile(np.arange(field_width), field_height)
        j1 = np.tile(np.arange(7), 7)

        i = i0.reshape(-1, 1) + i1.reshape(1, -1)
        j = j0.reshape(-1, 1) + j1.reshape(1, -1)
        return i, j

    def getStartState_(self):

        gameboard = self.gameboard[self.row:,:]

        for row in gameboard:
            j = 0
            for colum in row:
                if colum == 1:
                    start_state = (self.row+3, j+3)
                    return start_state
                j += 1

            self.row += 1

        self.goal = True
        return None

    def isGoalState(self, state):
        return self.goal

    def done(self):
        return self.goal

    def updateBoard(self, location):
        self.gameboard[location[0]-3,location[1]-3] = 0
        self.padded_gameboard[location[0]][location[1]] = 0
        self.working_gameboard[location[0]+3][location[1]+3] = 0

    def estimateValue(self, location, block):

         i = self.i + (location[0] - 3)
         j = self.j + (location[1] - 3)

         domain = np.dot(self.gamepieces, self.working_gameboard[i,j])

         new_gameboard = np.copy(self.working_gameboard)
         new_gameboard[location[0]+3,location[1]+3]= 0
         new_domain = np.dot(self.gamepieces, new_gameboard[i,j])

         domain[domain < 4] = 0
         new_domain[new_domain < 4] = 0

         domain = np.sum(domain, axis=0)
         new_domain = np.sum(new_domain, axis=0)

         value = (np.sum(domain) - np.sum(new_domain)) / (np.sum(domain) + 1e-6)

         zeros = np.count_nonzero(domain) - np.count_nonzero(new_domain) - 1

         if zeros == 0:
             return value
         elif np.abs(block-2) >= zeros:
             return value - 1000
         else:

            return value + 1000

    def getSolution(self):
        return self.solution[3:-3,3:-3]

    def clearSolution(self):
        self.complete_piece = np.zeros((7,7))
        self.counter = 1
        self.path = []

    def updateSolution(self, location):
        if self.counter == 1:

            self.complete_piece[3][3] = 1
            self.path.append(location)
            self.counter += 1

        elif self.counter == 2 or self.counter == 3:
            x, y = self.path[0]
            self.path.append(location)
            new_x, new_y = location
            self.complete_piece[3 + (new_x - x)][3 + (new_y - y)] = 1
            self.counter += 1

        elif self.counter == 4:
             x, y = self.path[0]
             self.path.append(location)
             new_x, new_y = location
             self.complete_piece[3 + (new_x - x)][3 + (new_y - y)] = 1

             domain = np.dot(np.array(self.complete_piece).ravel(), self.gamepieces.T)
             piece = np.argmax(domain)

             piece = piece / 4

             if piece < 1:
                  piece_id = 1

             elif piece < 2:
                  piece_id = 2

             elif piece < 3:
                  piece_id = 3

             elif piece < 4:
                  piece_id = 4

             elif piece < 5:
                  piece_id = 5

             elif piece < 6:
                  piece_id = 6

             elif piece < 7:
                  piece_id = 7

             elif piece < 8:
                  piece_id = 8

             elif piece < 9:
                  piece_id = 9

             elif piece < 10:
                  piece_id = 10

             elif piece < 11:
                  piece_id = 11

             elif piece < 12:
                  piece_id = 12

             elif piece < 13:
                  piece_id = 13

             elif piece < 14:
                  piece_id = 14

             elif piece < 15:
                  piece_id = 15

             elif piece < 16:
                  piece_id = 16

             elif piece < 17:
                  piece_id = 17

             elif piece < 18:
                  piece_id = 18

             elif piece < 19:
                  piece_id = 19

             for location in self.path:
                 self.solution[location[0]][location[1]] = (piece_id, self.piece_counter)

             self.complete_piece = np.zeros((7,7))
             self.counter = 1
             self.piece_counter += 1
             self.path = []

    def getSuccessors(self, state):
        successors = []
        x = state[0]
        y = state[1]

        if self.padded_gameboard[x-1,y] == 1:
            successors.append((x-1,y))

        if self.padded_gameboard[x+1,y] == 1:
            successors.append((x+1,y))

        if self.padded_gameboard[x,y-1] == 1:
            successors.append((x,y-1))

        if self.padded_gameboard[x,y+1] == 1:
            successors.append((x,y+1))

        return successors
