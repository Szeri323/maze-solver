from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height) -> None:
        self.__root = Tk()
        self.__root.title = "Test"
        self.canvas = Canvas(width=width,height=height)
        self.canvas.pack()
        self.__root_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__root_running = True
        while self.__root_running:
            self.redraw()
        
    def close(self):
        self.__root_running = False
        
def main():
    win = Window(800, 600)
    win.wait_for_close()
    
if __name__ == "__main__":
    main()