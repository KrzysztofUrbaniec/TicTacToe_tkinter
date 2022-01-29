import tkinter as tk
from tkinter import messagebox
from turtle import width
from constants import DIMENSION_OF_SQUARE, NUMBER_OF_ROWS, NUMBER_OF_COLUMNS

class View(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        self.used_tiles = {(0,0):2, (0,1):2, (0,2):2,
                           (1,0):2, (1,1):2, (1,2):2,
                           (2,0):2, (2,1):2, (2,2):2}

        # Create frame for all elements
        self.frame_main = tk.Frame(self)
        self.frame_main.pack(expand=True, fill='both', side='top')
        
        # self.create_layout()
        self.create_upper_menu()
        self.create_layout()
        self.canvas.bind("<Button-1>", self.on_square_clicked)
    
    def create_layout(self):
        self.create_upper_menu()
        self.create_canvas()
        self.draw_board()

    def initizalize_game(self):
        self.controller.game_running = True
        self.used_tiles = {(0,0):2, (0,1):2, (0,2):2,
                           (1,0):2, (1,1):2, (1,2):2,
                           (2,0):2, (2,1):2, (2,2):2}
        self.canvas.destroy()
        self.create_canvas()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_square_clicked)

    def create_canvas(self):
        canvas_width = DIMENSION_OF_SQUARE * NUMBER_OF_COLUMNS
        canvas_height = DIMENSION_OF_SQUARE * NUMBER_OF_COLUMNS
        self.canvas = tk.Canvas(self.frame_main, width=canvas_width, height=canvas_height, bg='white')
        self.canvas.pack(padx=5, pady=5, expand=True, fill="both")

    def create_upper_menu(self):
        self.menu = tk.Menu(self.controller)
        self.controller.config(menu=self.menu)
        self.create_file_menu()
        #self.create_about_menu()

    def create_file_menu(self):
        self.file_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Game", menu=self.file_menu)
        self.file_menu.add_command(label="New game", command=self.initizalize_game)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=quit)

    def create_edit_menu(self):
        pass

    def create_about_menu(self):
        self.about_menu = tk.Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="About", menu=self.file_menu)
        self.about_menu.add_command(label="Info", command=tk.messagebox.showinfo(message="Simple Tic Tac Toe game, Krzysztof Urbaniec"))

    def draw_board(self):
        for row in range(NUMBER_OF_ROWS):
            for column in range(NUMBER_OF_COLUMNS):
                x1,y1 = self.get_x_y_coordinates(row, column)
                x2,y2 = x1 + DIMENSION_OF_SQUARE, y1 + DIMENSION_OF_SQUARE
                self.canvas.create_rectangle(x1,y1, x2, y2, outline='black', width=2)
    
    def get_x_y_coordinates(self, row, column):
        x = column*DIMENSION_OF_SQUARE
        y = row*DIMENSION_OF_SQUARE
        return (x,y)

    def on_square_clicked(self, event):
        if self.controller.game_running:
            # Get number of columns and rows clicked
            row_clicked, column_clicked = self.get_row_col_clicked(event)
            if self.controller.player_turn == 1 and self.used_tiles[(row_clicked, column_clicked)] == 2:
                line_x1 = 0.2*DIMENSION_OF_SQUARE + column_clicked*DIMENSION_OF_SQUARE
                line_y1 = 0.2*DIMENSION_OF_SQUARE + row_clicked*DIMENSION_OF_SQUARE
                line_x2 = 0.8*DIMENSION_OF_SQUARE + column_clicked*DIMENSION_OF_SQUARE
                line_y2 = 0.8*DIMENSION_OF_SQUARE + row_clicked*DIMENSION_OF_SQUARE
                self.canvas.create_line(line_x1, line_y1, line_x2, line_y2, width=2)
                self.canvas.create_line(line_x1, line_y2, line_x2, line_y1, width=2)
                self.used_tiles[(row_clicked, column_clicked)] = self.controller.player_turn
                self.handle_game_events()
            elif self.controller.player_turn == 0 and self.used_tiles[(row_clicked, column_clicked)] == 2:
                square_x1 = 0.2*DIMENSION_OF_SQUARE + column_clicked*DIMENSION_OF_SQUARE
                square_y1 = 0.2*DIMENSION_OF_SQUARE + row_clicked*DIMENSION_OF_SQUARE
                square_x2 = 0.8*DIMENSION_OF_SQUARE + column_clicked*DIMENSION_OF_SQUARE
                square_y2 = 0.8*DIMENSION_OF_SQUARE + row_clicked*DIMENSION_OF_SQUARE
                self.canvas.create_oval(square_x1, square_y1, square_x2, square_y2, width=2)
                self.used_tiles[(row_clicked, column_clicked)] = self.controller.player_turn
                self.handle_game_events()
            else:
                print("This tile is occupied")
                print(self.used_tiles)
    
    def handle_game_events(self): 
        self.controller.check_for_victory() 
        self.controller.alternate_player()

    def get_row_col_clicked(self, event):
        column_size = row_size = DIMENSION_OF_SQUARE
        clicked_column = event.x // column_size
        clicked_row = event.y // row_size
        return (clicked_row, clicked_column)
        