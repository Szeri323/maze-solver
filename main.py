from graphics import Window
from maze import Maze

        
    
def main():
    secreen_x = 800
    secreen_y = 600
    margin = 50
    num_rows = 12
    num_cols = 16
    cell_size_x = (secreen_x - 2 * margin) / num_cols
    cell_size_y = (secreen_y - 2 * margin) / num_rows
    win = Window(secreen_x, secreen_y)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    if maze.solve():
        print("Maze solved successfully!")
    else:
        print("Maze could not be solved.")
    
    win.wait_for_close()
    
if __name__ == "__main__":
    main()