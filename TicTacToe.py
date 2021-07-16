from tkinter import*
from tkinter import messagebox

root = Tk()
#root.geometry("650x570")
root.title("Tic Tac Toe Game")
root.configure(background = 'White')
messagebox.showinfo("Tic Tac Toe", "Hello wecome to Tic Tac Toe Game\nGood Luck! and Playing Fun^^")

clicked = True
count = 0
def about():
    messagebox.showinfo("RULES FOR TIC-TAC-TOE", "1. The game is played on a grid that's 3 squares by 3 squares.\n\n2. You are X, your friend (or the computer in this case) is O. Players take turns putting their marks in empty squares.\n\n3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n\n4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
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

#Check The Winner
def wonthegame():
    global winner
    winner = False

    #For X
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" :
        b1.config(bg="white")
        b2.config(bg="white")
        b3.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()

    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X" :
        b4.config(bg="white")
        b5.config(bg="white")
        b6.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()
    
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" :
        b7.config(bg="white")
        b8.config(bg="white")
        b9.config(bg="white")
        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()

    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X" :
        b1.config(bg="white")
        b4.config(bg="white")
        b7.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()

    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X" :
        b2.config(bg="white")
        b5.config(bg="white")
        b8.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()
    
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X" :
        b3.config(bg="white")
        b6.config(bg="white")
        b9.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()
    
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X" :
        b1.config(bg="white")
        b5.config(bg="white")
        b9.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()

    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X" :
        b3.config(bg="white")
        b5.config(bg="white")
        b7.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "X Winning The Games\nO is a Loser!")
        disable_all_buttons()

    #For O
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" :
        b1.config(bg="white")
        b2.config(bg="white")
        b3.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()

    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O" :
        b4.config(bg="white")
        b5.config(bg="white")
        b6.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()
    
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" :
        b7.config(bg="white")
        b8.config(bg="white")
        b9.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()

    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O" :
        b1.config(bg="white")
        b4.config(bg="white")
        b7.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()

    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O" :
        b2.config(bg="white")
        b5.config(bg="white")
        b8.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()
    
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O" :
        b3.config(bg="white")
        b6.config(bg="white")
        b9.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()
    
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O" :
        b1.config(bg="white")
        b5.config(bg="white")
        b9.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O" :
        b3.config(bg="white")
        b5.config(bg="white")
        b7.config(bg="white")

        winner = True
        messagebox.showinfo("Congratulations", "O Winning The Games\nX is a Loser!")
        disable_all_buttons()
   
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "Its a Tie\nNo one wins this game! Try again")

#Button Clicked Function
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True :
        b["text"] = "X"
        clicked = False
        count += 1
        wonthegame()
    elif b["text"] == " " and clicked == False :
        b["text"] = "O"
        clicked = True
        count += 1
        wonthegame()
    else :
        messagebox.showerror("Error", "Its already selected\nPick Another Column")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked, count
    clicked = True
    count = 0

    #Build Button
    b1 = Button(root, text=" ", font=("Tw Cen MT", 22), bg="white", width=10, height=5, command=lambda:b_click(b1))
    b2 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b2))
    b3 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b3))
    b4 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b4))
    b5 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b5))
    b6 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b6))
    b7 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b7))
    b8 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b8))
    b9 = Button(root, text=" ", font=("Tw Cen MT", 22), bg='white', width=10, height=5, command=lambda:b_click(b9))

    #Grid Button
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

#Menu
mymenu = Menu(root)
root.config(menu=mymenu)

option_menu = Menu(mymenu, tearoff=False)
mymenu.add_cascade(label="Menu", menu=option_menu)
option_menu.add_command(label="Reset", command=reset)
option_menu.add_command(label="About", command=about)

reset()
about()

root.mainloop()
