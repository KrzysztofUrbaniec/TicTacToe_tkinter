import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from constants import DIMENSION_OF_SQUARE, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS

from view import View

class Controller(tk.Tk):
    def __init__(self):
        # Player turn: 1 - X, 0 - O
        self.player_turn = 1
        self.player_symbols = {1:'X',0:'O'}
        self.winner = None
        self.game_running = True

        tk.Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frame = View(container, self)
        self.frame.grid(row=0, column=0, sticky='nsew') 
        self.frames[View] = self.frame

        self.show_frame(View)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def alternate_player(self):
        # Turn to O's turn
        if self.player_turn == 1:
            self.player_turn = 0
        # Turn to X's turn 
        elif self.player_turn == 0:
            self.player_turn = 1

    def check_for_victory(self):
        # ? Can these conditions be done differently?
        # Rows
        if (self.frame.used_tiles[(0,0)] == self.player_turn and
            self.frame.used_tiles[(0,1)] == self.player_turn and
            self.frame.used_tiles[(0,2)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(0.1*DIMENSION_OF_SQUARE, 0.5*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, 0.5*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        elif (self.frame.used_tiles[(1,0)] == self.player_turn and
            self.frame.used_tiles[(1,1)] == self.player_turn and
            self.frame.used_tiles[(1,2)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(0.1*DIMENSION_OF_SQUARE, 1.5*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, 1.5*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        elif (self.frame.used_tiles[(2,0)] == self.player_turn and
            self.frame.used_tiles[(2,1)] == self.player_turn and
            self.frame.used_tiles[(2,2)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(0.1*DIMENSION_OF_SQUARE, 2.5*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, 2.5*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        #Columns
        elif (self.frame.used_tiles[(0,0)] == self.player_turn and
            self.frame.used_tiles[(1,0)] == self.player_turn and
            self.frame.used_tiles[(2,0)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(0.5*DIMENSION_OF_SQUARE, 0.1*DIMENSION_OF_SQUARE, 0.5*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        elif (self.frame.used_tiles[(0,1)] == self.player_turn and
            self.frame.used_tiles[(1,1)] == self.player_turn and
            self.frame.used_tiles[(2,1)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(1.5*DIMENSION_OF_SQUARE, 0.1*DIMENSION_OF_SQUARE, 1.5*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        elif (self.frame.used_tiles[(0,2)] == self.player_turn and
            self.frame.used_tiles[(1,2)] == self.player_turn and
            self.frame.used_tiles[(2,2)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(2.5*DIMENSION_OF_SQUARE, 0.1*DIMENSION_OF_SQUARE, 2.5*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        # Diagonals
        if (self.frame.used_tiles[(0,0)] == self.player_turn and
            self.frame.used_tiles[(1,1)] == self.player_turn and
            self.frame.used_tiles[(2,2)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(0.1*DIMENSION_OF_SQUARE, 0.1*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        elif (self.frame.used_tiles[(2,0)] == self.player_turn and
            self.frame.used_tiles[(1,1)] == self.player_turn and
            self.frame.used_tiles[(0,2)] == self.player_turn):
            self.winner = self.player_symbols[self.player_turn]
            self.frame.canvas.create_line(0.1*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, 2.9*DIMENSION_OF_SQUARE, 0.1*DIMENSION_OF_SQUARE, width=2)
            messagebox.showinfo(message=f"Player: {self.player_symbols[self.player_turn]} won!")
            self.game_running = False
        # Tie
        elif 2 not in self.frame.used_tiles.values():
            messagebox.showinfo(message=f"Tie!")
            self.game_running = False

    def run(self):
        # Set root properties
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.title("Tic Tac Toe")
        self.geometry("500x500")
        self.resizable(0,0)
        tk.Tk.mainloop(self)

# define main() to avoid global code
def main():
    c = Controller()
    c.run()

if __name__ == '__main__':
    main()