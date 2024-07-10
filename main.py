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
        
        
def main():
    win = Window(800, 600)
    point1 = Point(200, 300)
    point2 = Point(400, 150)
    line1 = Line(point1=point1,point2=point2)
    point3 = Point(700, 100)
    point4 = Point(700, 500)
    line2 = Line(point3, point4)
    line1.draw(win.canvas, "red")
    line2.draw(win.canvas, "blue")
    win.wait_for_close()
    
if __name__ == "__main__":
    main()