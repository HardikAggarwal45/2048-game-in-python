import tkinter
import random
from tkinter import messagebox

def is_game_over():
    global game_over
    if (game_over):
        return
    for i in range(4):
        for j in range(4):
            if (game_state[i][j]==2048):
                messagebox.showinfo("2048", "Congratulations! You reached 2048!")
                game_over = True
                return
    for i in range(4):
        for j in range(4):
            if (game_state[i][j]==0):
                return
    for i in range(4):
        for j in range(3):
            if (game_state[i][j] == game_state[i][j+1]):
                return
            if (game_state[j][i] == game_state[j+1][i]):
                return
    game_over  =True
    messagebox.showinfo("2048", "Game Over! No more moves possible.")
    

def transpose():
    for i in range(4):
        for j in range(i + 1, 4):
            game_state[i][j], game_state[j][i] = game_state[j][i], game_state[i][j]

def new_game():
    global game_over
    game_over = False
    for i in range(4):
        for j in range(4):
            game_state[i][j]=0
    add_random()
    add_random()
    draw_board()


def add_random():
    empty_cells = [(r, c) for r in range(4) for c in range(4) if game_state[r][c] == 0]
    if len(empty_cells)==0:
        game_over = True
        return
    r, c = random.choice(empty_cells)
    sample = [2,2,2,2,2,4]
    s = random.choice(sample)
    game_state[r][c] = s
    
def move_left(event = None):
    global game_over
    if (game_over):
        return
    for i in range(4):
        L = game_state[i]
        L1=[]
        for j in range(4):
            if (L[j]!=0):
                L1.append(L[j])
        if len(L1)==0:
            L1.append(0)
            L1.append(0)
            L1.append(0)
            L1.append(0)
        elif len(L1)==1:
            L1.append(0)
            L1.append(0)
            L1.append(0)
        elif len(L1)==2:
            if (L1[0]==L1[1]):
                L1[0]=2*L1[0]
                L1[1]=0
            L1.append(0)
            L1.append(0)
        elif len(L1)==3:
            if (L1[0]==L1[1]):
                L1[0] = 2*L1[0]
                L1[1]=L1[2]
                L1[2]=0
            elif (L1[1]==L1[2]):
                L1[1]=2*L1[1]
                L1[2]=0
            L1.append(0)
        else:
            if (L1[0]==L1[1] and L1[2]==L1[3]):
                L1[0] = 2*L1[0]
                L1[1] = 2*L1[2]
                L1[2]=0
                L1[3]=0
            elif (L1[0]==L1[1]):
                L1[0] = 2*L1[0]
                L1[1]=L1[2]
                L1[2]=L1[3]
                L1[3]=0
            elif (L1[1]==L1[2]):
                L1[1]=2*L1[1]
                L1[2]=L1[3]
                L1[3]=0
            elif (L1[2]==L1[3]):
                L1[2]=2*L1[2]
                L1[3]=0
        game_state[i] = L1
    add_random()
    draw_board()

def move_right(event = None):
    global game_over
    if (game_over):
        return
    for i in range(4):
        game_state[i][0], game_state[i][3] = game_state[i][3], game_state[i][0]
        game_state[i][1], game_state[i][2] = game_state[i][2], game_state[i][1]
    move_left()
    for i in range(4):
        game_state[i][0], game_state[i][3] = game_state[i][3], game_state[i][0]
        game_state[i][1], game_state[i][2] = game_state[i][2], game_state[i][1]
    draw_board()

def move_up(event = None):
    global game_over
    if (game_over):
        return
    transpose()
    move_left()
    transpose()
    draw_board()

def move_down(event = None):
    global game_over
    if (game_over):
        return
    transpose()
    move_right()
    transpose()
    draw_board()

def draw_board():
    for i in range(4):
        for j in range(4):
            if (game_state[i][j]!=0):
                board[i][j].config(text = game_state[i][j], 
                               background = back_color[game_state[i][j]],
                            foreground = text_color[(game_state[i][j]%8)])
            else:
                board[i][j].config(text = "", 
                               background = back_color[0])
    is_game_over()

# Tile Background Colors
back_color = {
    2: "#eee4da",
    4: "#ede0c8",
    8: "#f2b179",
    16: "#f59563",
    32: "#f67c5f",
    64: "#f65e3b",
    128: "#edcf72",
    256: "#edcc61",
    512: "#edc850",
    1024: "#edc53f",
    2048: "#edc22e",
    0: "#cdc1b4"
}

# Tile Text Colors (Foreground)
# Usually, 2 and 4 use a dark gray, others use white
text_color = {
    2: "#776e65",
    4: "#776e65",
    0: "#f9f6f2" # For 8 and above
}

# making window
window = tkinter.Tk()
window.title("2048")
window.resizable(False, False)

# Binding the keys to a function
window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)

# making frame
frame = tkinter.Frame(window)


# initializing board and game_state
board = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

game_state = [[2,0,0,0],
             [0,0,0,0],
             [0,0,4,0],
             [0,0,0,0]]

game_over = False
game_2048 = False

for row in range (4):
    for column in range(4):
        board[row][column] = tkinter.Label(frame, text = "",
                                        font=("Consolas", 50, "bold"),
                                        background = back_color[0],
                                        width=3, height=1)
        board[row][column].grid(row = row, column=column)
new_game()

# restart button
button = tkinter.Button(frame, text="restart", font = ("Consolas", 20), background=back_color[0],
                        foreground="white", command=new_game)
button.grid(row=5, column=0, columnspan=4, sticky = "we")





# extra

frame.pack() #completely fill the window

# center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))

# format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop() #code runs (window stays open) until user clicks on the cross of window
