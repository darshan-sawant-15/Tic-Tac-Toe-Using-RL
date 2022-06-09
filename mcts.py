#MCTS algorithm implementation

#packages

import math
import random

#tree node class definition
class TreeNode():
    #class constructor (Create tree node class instance)
    def __init__(self, board, parent):
        # init associated board state
        self.board = board

        # is node terminal (flag)
        if self.board.is_won() or self.board.is_draw():
            # we have a terminal node
            self.is_terminal = True
        else:
            #we have a non-terminal node
            self.is_terminal = False
        
        # init is Fully expanded flag
        #fully expanded means that all the children this node has have been created
        self.is_fully_expanded = self.is_terminal


        #init parent node if available
        self.parent = parent

        #initialise the number of node visits
        self.visits = 0

        #init the total score of the node
        self.score = 0

        #init current node's children
        self.children = {}


#MCTS class definition

class MCTS():
    
    def __init__(self, iterations):
        self.iterations = iterations 

    #search for the best move in the current position
    def search(self, initial_state):
        #initial state is the state for which we want to search the best move for
        self.root = TreeNode(initial_state, None)

        #walk through 1000 iterations 
        for iteration in range(self.iterations):
            # select a node (selection)
            node = self.select(self.root)

            # score current node (simulation)
            score = self.rollout(node.board)
            #light rollout is random self play and heavy rollout has a an algorithm to calculate the score

            #backpropagate results
            self.backpropagate(node, score)

        # pick up the best move in the current position
        try:
            return self.get_best_move(self.root, 0)
            #second paramter is an exploration constant, 0 means we only exploit available knwoledge and not explore any more
    
        except:
            pass


    

    #select most promising node
    def select(self, node):
        #make sure that we are dealing with non-terminal nodes
        while not node.is_terminal:
            #case where the node is fully expanded
            if node.is_fully_expanded: 
                node = self.get_best_move(node, 2)

            #case where the node is not fully expanded
            else:
                #otherwise expand the node
                return self.expand(node)
        #return node
        return node



    def expand(self, node):
        # generate legal states (moves) for the given node
        states = node.board.generate_states()

        #loop over generated states (moves)
        for state in states:
            # make sure that current state (move) is not present in the child nodes
            if str(state.position) not in node.children:
                #this would look for 'state.position' key in children dictionary
                
                #create a new node
                new_node = TreeNode(state, node)

                # add child node to parents node's children list (dict)
                node.children[str(state.position)] = new_node

                #figure out whether the current (parent) node is fully expanded or not
                if len(states) == len(node.children):
                    node.is_fully_expanded = True

                #return newly created node
                return new_node
            
        #debugging
        print('Shouldn\'t get here!!!')

                

    # simulate the game via making random moves until reach end of the game
    def rollout(self, board):
        #make random moves for both sides until terminal state of the game is reached 
        while not board.is_won():
            #try to make a move 
            try:
                #make the move on board
                board = random.choice(board.generate_states())
                
            #no moves available 
            except:
                #return a draw score
                return 0

        #return score from the player 'x' perspective
        if board.player_2 == 'x':
            return 1
        elif board.player_2 == 'o':
            return -1
        


    #backpropagate the number of visits and score upto the root node
    def backpropagate(self, node, score):
        #update node's visit count and score upto root node
        while node is not None:
            # update node visits
            node.visits += 1
        
            #update node's score
            node.score += score

            #set node to parent
            node = node.parent



    #select the best node based on UCB1 formula
    def get_best_move(self, node, exploration_constant):
        # define best score and best moves
        best_score = float('-inf')
        best_moves = []

        # loop over child nodes
        for child_node in node.children.values():
            #define current player
            if child_node.board.player_2 == 'x': 
                current_player = 1
            elif child_node.board.player_2 == 'o':
                current_player = -1

            move_score = current_player * child_node.score / child_node.visits + exploration_constant * math.sqrt(math.log(node.visits/child_node.visits))

            #better move has been found
            if move_score > best_score:
                best_score = move_score
                best_moves = [child_node]

            #found as good move as already available
            elif move_score == best_score:
                best_moves.append(child_node)

        #return one of the best moves randomly
        return random.choice(best_moves)