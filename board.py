#AI that learns to play Tic Tac Toe using reinforcement learning
#MCTS 

#packages
from copy import deepcopy
from mcts import *
#to copy an entire instance of the board class to generate a node for our opponent

#Tic Tac Toe board class
class Board():
    #create a constructor(init board class instance)
    #init is basically the constructor in this case
    #self is the object on which we initialising
    def __init__(self, board=None):
        #define players
        self.player_1 = 'x'
        self.player_2 = 'o'
        self.empty_Square = ' '

        #define board position
        self.position = {}

        #init (reset) board
        self.init_board()

        #create a copu of a previous board state if available:
        if board is not None:
            self.__dict__ = deepcopy(board.__dict__)
            #__dict returns the internal dictionary of attributes of specific instance
        


    #init(reset) board
    def init_board(self):
        #loop over board rows
        for row in range(3):
            #loop over board columns
            for col in range(3):
                #set every board square to empty square
                self.position[row, col] = self.empty_Square


    #make move
    def make_move(self, row, col):
        #create new Board instance
        board = Board(self)

        #make move
        board.position[row,col] = self.player_1

        #swap players, as its o's turn now
        (board.player_1, board.player_2)=(board.player_2, board.player_1)

        #return new board state
        return board



    #get whether the game is draw
    def is_draw(self):
        #loop over boards squares
        for row, col in self.position:
            #empty square is available
            if self.position[row,col] == self.empty_Square:
                #this is not a draw
                return False
        return True



    #get whether the game is won
    def is_won(self):
        ############################
        #vertical sequence detection
        ############################

        #loop over board columns
        for col in range(3):
            #define the winning sequence list
            winning_sequence=[]

            #loop over board rows
            for row in range(3):
                #if found same next element in the column
                if self.position[row,col] == self.player_2:
                    #update the winning sequence
                    winning_sequence.append((row,col))
                
                #if we have 3 elements in a row
                if len(winning_sequence) == 3:
                    #the game is won state
                    return True

        ##############################
        #horizontal sequence detection
        ##############################
        for row in range(3):
            #define the winning sequence list
            winning_sequence=[]

            #loop over board rows
            for col in range(3):
                #if found same next element in the row
                if self.position[row,col] == self.player_2:
                    #update the winning sequence
                    winning_sequence.append((row,col))
                
                #if we have 3 elements in a row
                if len(winning_sequence) == 3:
                    #the game is won state
                    return True

        ################################
        #1st diagonal sequence detection
        ################################
        #define the winning sequence list
        winning_sequence=[]

        #loop over board rows
        for row in range(3):
            #init column
            col = row

            #if found same next element in the row
            if self.position[row,col] == self.player_2:
                #update the winning sequence
                winning_sequence.append((row,col))
            
            #if we have 3 elements in a row
            if len(winning_sequence) == 3:
                #the game is won state
                return True



        ################################
        #2nd diagonal sequence detection
        ################################
        #define the winning sequence list
        winning_sequence=[]

        #loop over board rows
        for row in range(3):
            #init column
            col = 3 - row - 1
            
            #if found same next element in the row
            if self.position[row,col] == self.player_2:
                #update the winning sequence
                winning_sequence.append((row,col))
            
            #if we have 3 elements in a row
            if len(winning_sequence) == 3:
                #the game is won state
                return True



        #by default not winning state
        return False



    #generate legal moves to play in the current position
    def generate_states(self):
        #define states list (move list - list of available actions to consider)
        actions = []

        #loop over board rows
        for row in range(3):
            #loop over board colums
            for col in range(3):
                # make sure that current square is empty
                if self.position[row,col] ==  self.empty_Square:
                #append available action/board state to action list
                    actions.append(self.make_move(row,col))

        #returns the list of available actions (board class instances)
        return actions


        


  