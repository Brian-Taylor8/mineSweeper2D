import tkinter as tk
import random as r
WIDTH, LENGTH = 20, 20

class Button():
    def __init__(self, mine, bt):
        self.mine = mine
        self.bt = bt

def square_draw(mine, col, row):
    bt = tk.Button(window, width=5, height=2, text="", command=lambda: click(col, row))
    bt.grid(column=(col+1)*5, row=(row+1)*2)
    return Button(mine, bt)

def click(col, row, depth=3):
    # Expansion algo in all directions, terminates when 
    #it hits spaces that are invalid
    curr = listing[col][row]
    
    if curr.mine:
        print("You clicked on a mine dude")
    else:
        total = 0
        for i in range(max(0,col-1), min(WIDTH, col+2)):
            for j in range(max(0, row-1), min(LENGTH, row+2)):
                neighbor = listing[i][j]
                if neighbor.mine:
                    total += 1
                # else:
                #     click(i, j)
        curr.bt["text"] = str(total)

    print(row, col)
        


window = tk.Tk()
window.title("Minesweeper 2d")

disp = tk.Label(window, text="Minesweeper 2d")
disp.grid(column=0, row=0, columnspan=WIDTH*5)
listing = []
for i in range(WIDTH):
    listing.append([])
    for j in range(LENGTH):
        val = False
        if r.random() < 0.2:
            val = True
        listing[i].append(square_draw(val, i, j))


window.mainloop()