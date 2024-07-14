from cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win 
        if seed is not None:
            self.seed = random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._reset_cells_visited()
        
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._break_walls_r(i, j)
        
    def _create_cells(self):
        for row in range(self._num_rows):
            col_cells = []
            for col in range(self._num_cols):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
                
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows-1][self._num_cols-1].has_bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)
        
    def _break_wall(self, i, j, di, dj):
        if (di, dj) == (-1, 0):
            self._cells[i][j].has_top_wall = False
            self._cells[i-1][j].has_bottom_wall = False
        elif (di, dj) == (1, 0):
            self._cells[i][j].has_bottom_wall = False
            self._cells[i+1][j].has_top_wall = False
        elif (di, dj) == (0, -1):
            self._cells[i][j].has_left_wall = False
            self._cells[i][j-1].has_right_wall = False
        elif (di, dj) == (0, 1):
            self._cells[i][j].has_right_wall = False
            self._cells[i][j+1].has_left_wall = False
                
        self._draw_cell(i, j)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(self._cells) and 0 <= nj < len(self._cells[0]):
                    if not self._cells[ni][nj].visited:
                        to_visit.append((ni, nj, di, dj))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                ni, nj, di, dj = random.choice(to_visit)
                self._break_wall(i, j, di, dj)
                
                self._break_walls_r(ni, nj)
        
    def _reset_cells_visited(self):
        for i in range(self._num_rows-1):
            for j in range(self._num_cols-1):
                self._cells[i][j].visited = False
                print(self._cells[i][j].visited)