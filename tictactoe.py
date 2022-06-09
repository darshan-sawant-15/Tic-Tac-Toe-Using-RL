from tkinter import *
from tkinter import messagebox
from mcts import *
from board import *


root = Tk()
root.title('Tic Tac Toe')
root.resizable(False, False)
p1 = PhotoImage(file = 'tic-tac-toe.png')
root.iconphoto(True, p1)


def b_click(b,string):
    global count, board, mcts, ai_mode, clicked

    if ai_mode == True:
        #checking which box is selected
        if string=='b1':
            row = 0
            col = 0
        elif string=='b2':
            row = 0
            col = 1
        elif string=='b3':
            row = 0
            col = 2
        elif string=='b4':
            row = 1
            col = 0
        elif string=='b5':
            row = 1
            col = 1
        elif string=='b6':
            row = 1
            col = 2
        elif string=='b7':
            row = 2
            col = 0
        elif string=='b8':
            row = 2
            col= 1
        elif string=='b9':
            row = 2
            col = 2


        if b['text'] == " ":
            b['text'] = "X"
            count += 1 

            board = board.make_move(row,col)
            #srarch for the best move
            best_move = mcts.search(board) 
            try:
                #make AI move here
                board = best_move.board
            except:
                #game over
                pass
            update_game()
            checkifwon()
            
        else:
            messagebox.showwarning("Tic Tac Toe", "This tile has been already used")
    
    elif ai_mode == False:
        if b['text'] == ' ' and clicked == False:
            b['text'] = "X"
            clicked = True
            count +=1
            checkifwon()
        elif b['text'] == ' ' and clicked == True:
            b['text'] = "O"
            clicked = False
            count+=1
            checkifwon()
        else:
            messagebox.showwarning("Tic Tac Toe", "This tile has been already used")

#to update the game grid after the move has been made
def update_game():
    b1['text'] = board.position[0,0].upper()
    b2['text'] = board.position[0,1].upper()
    b3['text'] = board.position[0,2].upper()
    b4['text'] = board.position[1,0].upper()
    b5['text'] = board.position[1,1].upper()
    b6['text'] = board.position[1,2].upper()
    b7['text'] = board.position[2,0].upper()
    b8['text'] = board.position[2,1].upper()
    b9['text'] = board.position[2,2].upper()

def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def checkifwon():
    global winner 
    winner = False

    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg="green")
        b2.config(bg='green')
        b3.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg="green")
        b5.config(bg='green')
        b6.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg="green")
        b8.config(bg='green')
        b9.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg="green")
        b4.config(bg='green')
        b7.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()    
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg="green")
        b5.config(bg='green')
        b8.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg="green")
        b6.config(bg='green')
        b9.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg="green")
        b5.config(bg='green')
        b9.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg="green")
        b5.config(bg='green')
        b7.config(bg='green')
        winner = True
        if ai_mode == False:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player X won')
        else:
            messagebox.showinfo('Tic Tac Toe', 'Congratulations You won')
        disable_all_buttons()

    #checking for O
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        winner = True
        if ai_mode == False:
            b1.config(bg="green")
            b2.config(bg='green')
            b3.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b1.config(bg="red")
            b2.config(bg='red')
            b3.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        winner = True
        if ai_mode == False:
            b4.config(bg="green")
            b5.config(bg='green')
            b6.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b4.config(bg="red")
            b5.config(bg='red')
            b6.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        winner = True
        if ai_mode == False:
            b7.config(bg="green")
            b8.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b7.config(bg="red")
            b8.config(bg='red')
            b9.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        winner = True
        if ai_mode == False:
            b1.config(bg="green")
            b4.config(bg='green')
            b7.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b1.config(bg="red")
            b4.config(bg='red')
            b7.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        winner = True
        if ai_mode == False:
            b2.config(bg="green")
            b5.config(bg='green')
            b8.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b2.config(bg="red")
            b5.config(bg='red')
            b8.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        winner = True
        if ai_mode == False:
            b3.config(bg="green")
            b6.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b3.config(bg="red")
            b6.config(bg='red')
            b9.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        winner = True
        if ai_mode == False:
            b1.config(bg="green")
            b5.config(bg='green')
            b9.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b1.config(bg="red")
            b5.config(bg='red')
            b9.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        winner = True
        if ai_mode == False:
            b3.config(bg="green")
            b5.config(bg='green')
            b7.config(bg='green')
            messagebox.showinfo('Tic Tac Toe', 'Congratulations Player O won')
        else:
            b3.config(bg="red")
            b5.config(bg='red')
            b7.config(bg='red')
            messagebox.showerror('Tic Tac Toe', 'Unfortunately You lost')
        disable_all_buttons()

    #check if tie
    if ai_mode == True:
        if count==5 and winner == False:
            messagebox.showinfo('Tic Tac Toe','Its a tie, no one wins')
            disable_all_buttons()    
    elif ai_mode == False:
        if count==9 and winner == False:
            messagebox.showinfo('Tic Tac Toe','Its a tie, no one wins')
            disable_all_buttons()   

#Start the game over
def reset(mode=False, difficulty=0):
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global label
    global clicked, count, ai_mode, diff_mode
    global board, mcts

    count=0
    
    if mode == False:
        ai_mode = False
        diff_mode = 0
        clicked  = False
    elif mode == True:
        ai_mode = True
        board =  Board()
        if difficulty==1:
            diff_mode = 1
            mcts = MCTS(100)
        elif difficulty==2:
            diff_mode = 2
            mcts = MCTS(1000) 

    label = Label(root)
    label.grid(row=3, column=0, columnspan=3)
    set_label(difficulty)
   
    
    #buttons
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b1, string='b1'))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b2, string='b2'))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b3, string='b3'))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b4, string='b4'))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b5, string='b5'))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b6, string='b6'))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b7, string='b7'))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b8, string='b8'))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command = lambda: b_click(b9, string='b9'))

    #Grid our buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#setting the label for the mode
def set_label(difficulty):
    global label
    if ai_mode == True:
        if difficulty == 1:
            label.config(text="Player Vs Computer - Easy Mode", font=('Helvetica, 12'))
        elif difficulty == 2:
            label.config(text="Player Vs Computer - Hard Mode", font=('Helvetica, 12'))
    else:
        label.config(text="Player Vs Player", font=('Helvetica, 12'))

#cleaning the previous label before putting the new one
def clean_label(mode, difficulty=0):
    global label
    label.config(text='')
    reset(mode, difficulty)

#menu
my_menu = Menu(root)
root.config(menu=my_menu)

#options menu
options_menu = Menu(my_menu, tearoff=False)
mode_menu = Menu(options_menu, tearoff=False)
difficulty_menu = Menu(options_menu, tearoff=False)

#menu config
my_menu.add_cascade(label = 'Options', menu=options_menu)
options_menu.add_command(label = "Reset Game", command= lambda: clean_label(ai_mode, diff_mode))
options_menu.add_cascade(label="Mode", menu=mode_menu)
mode_menu.add_command(label="Player Vs Player", command=lambda: clean_label(False))
mode_menu.add_cascade(label = "Player Vs Comp", menu=difficulty_menu )
difficulty_menu.add_command(label="Easy Mode", command = lambda: clean_label(True, 1))
difficulty_menu.add_command(label="Hard Mode", command = lambda: clean_label(True, 2))


reset()

root.mainloop()
