from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
width=1366
height=768
global buttons,board
current_player="X"
board = [[' ' for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
def gameplay():
    canvas.destroy()
    x=910
    y=260
    player=Label(win,text="Player 1's Turn",width=20,font=custom_font,bg="skyblue",fg="black",borderwidth=8,relief=RAISED)
    player.place(x=920,y=203)
    for i in range(3):
        for j in range(3):
            buttons[i][j] = Button(win, text=" ",bg="skyblue", font=("Helvetica", 20), width=5, height=2,
                                    command=lambda row=i, col=j: on_click(row, col),borderwidth=8,relief=RAISED)
            buttons[i][j].place(x=x, y=y)
            x+=90
        x-=270
        y+=90
    exit_game=Button(win,text="Exit",command=win.destroy,width=15,font=custom_font,bg="skyblue",fg="black",borderwidth=8,relief=RAISED)
    exit_game.place(x=950,y=550)
def on_click(row, col):
    global current_player
    if board[row][col] == ' ':
        buttons[row][col].config(text=current_player)
        board[row][col] = current_player
        if(current_player=="X"):
            player=Label(win,text="Player 2's Turn",width=20,font=custom_font,bg="skyblue",fg="black",borderwidth=8,relief=RAISED)
            player.place(x=920,y=203)
        else:
            player=Label(win,text="Player 1's Turn",width=20,font=custom_font,bg="skyblue",fg="black",borderwidth=8,relief=RAISED)
            player.place(x=920,y=203)
        if check_winner():
            show_winner()
        elif check_draw():
            show_draw()
        else:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

def check_draw():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def show_winner():
    winner = "Player 2" if current_player == "O" else "Player 1"
    messagebox.showinfo("Tic Tac Toe", f"{winner} has won the Match!")
    reset_board()

def show_draw():
    messagebox.showinfo("Tic Tac Toe", "Oh! It's a draw!")
    reset_board()

def reset_board():
    global current_player, board
    current_player = "X"
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=" ")
win=Tk()
win.geometry("%dx%d" % (width, height))
win.title("Tic Tac Toe")
bg_image = PhotoImage(file="tictactoe_bg.png")
label1 = Label( win, image = bg_image)
label1.place(x = 0, y = 0)
p1 = PhotoImage(file = 'SNDS.png')
win.iconphoto(False, p1)
custom_font = Font(family="Magz", size=15, weight="bold", slant="italic")
# button shape
canvas = Canvas(win, width=225, height=150,background="black",borderwidth=0)
canvas.place(x=950,y=370)
button_shape = canvas.create_oval(15, 15, 210, 135, fill="skyblue")  # Oval with rounded edges
canvas.tag_bind(button_shape, '<Button-1>', lambda event: gameplay())
canvas.create_text(107, 75, text="Play Now", font=("Magz",20,"bold","italic"), fill="black")
win.mainloop()