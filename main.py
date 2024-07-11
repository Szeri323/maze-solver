from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Test"
        self.canvas = Canvas(width=width,height=height)
        self.canvas.pack()
        self.__root_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(line, fill_color):
        line.draw_line(fill_color=fill_color)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__root_running = True
        while self.__root_running:
            self.redraw()
        
    def close(self):
        self.__root_running = False
        
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def draw(self, canvas, fill_color):
            canvas.create_line(
                self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2
            )

class Cell:
    def __init__(self, x1, x2, y1, y2, win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    
    def draw(self, fill_color):
        if self.has_left_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x1, self._y2)
            left_wall = Line(point1=point1,point2=point2)
            left_wall.draw(self._win.canvas, fill_color)
        if self.has_right_wall:
            point1 = Point(self._x2, self._y1)
            point2 = Point(self._x2, self._y2)
            right_wall = Line(point1=point1,point2=point2)
            right_wall.draw(self._win.canvas, fill_color)
        if self.has_top_wall:
            point1 = Point(self._x1, self._y1)
            point2 = Point(self._x2, self._y1)
            top_wall = Line(point1=point1,point2=point2)
            top_wall.draw(self._win.canvas, fill_color)
        if self.has_bottom_wall:
            point1 = Point(self._x1, self._y2)
            point2 = Point(self._x2, self._y2)
            bottom_wall = Line(point1=point1,point2=point2)
            bottom_wall.draw(self._win.canvas, fill_color)
    
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        #if self.has_right_wall == False and to_cell.has_left_wall == False:
        point1 = Point(self._x1 + (self._x2 - self._x1) / 2, self._y2 - (self._y2 - self._y1) / 2)        
        point2 = Point(to_cell._x2 - (to_cell._x2 - to_cell._x1) / 2, to_cell._y2-(to_cell._y2-to_cell._y1)/2)    
        line = Line(point1, point2)
        line.draw(self._win.canvas, fill_color)    
        
def main():
    win = Window(800, 600)
    # point1 = Point(200, 300)
    # point2 = Point(400, 150)
    # line1 = Line(point1=point1,point2=point2)
    # point3 = Point(700, 100)
    # point4 = Point(700, 500)
    # line2 = Line(point3, point4)
    # line1.draw(win.canvas, "red")
    # line2.draw(win.canvas, "blue")
    cell1 = Cell(50, 150, 150, 250, win)
    cell1.draw("black")
    cell2 = Cell(250, 350, 150, 250, win)
    cell2.draw("black")
    cell3 = Cell(150, 250, 50, 150, win)
    cell3.draw("black")
    cell4 = Cell(150, 250, 250, 350, win)
    cell4.draw("black")
    cell1.draw_move(cell2)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()