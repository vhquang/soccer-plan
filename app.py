# from graphic import *
import tkinter as tk
import typing as tp


class Attacker(tk.Canvas):
    def __init__(self, window: tk.Tk, x: int, y: int):
        super().__init__(window, width=40, height=40, bg='blue')
        self.place(x=x, y=x, anchor=tk.CENTER)
        self.bind('<B1-Motion>', self.drag)

    def drag(self, event):
        event.widget.place(x=event.x_root, y=event.y_root,anchor=tk.CENTER)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._root = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.player = Attacker(self._root, 300, 300)
        self.player.pack()

        # self.hi_there = tk.Button(self)
        # self.hi_there["text"] = "Hello World\n(click me)"
        # self.hi_there.pack(side="top")

        # self.quit = tk.Button(self, text="QUIT", fg="red",
        #                       command=root.destroy)
        # self.quit.pack(side="bottom")

def main():
    pass

if __name__ == '__main__':
    root = tk.Tk()
    # root.geometry('600x450')  # 120x90
    root.configure(bg='green4')
    app = Application(master=root)
    app.mainloop()

def showPosEvent(event):
    print('Widget={} X={} Y={}'.format(event.widget, event.x, event.y))
     
def onLeftDrag(event):
    print('Got left mouse button drag:')
    showPosEvent(event)
     
# tkroot = Tk()
# labelfont = ('courier', 20, 'bold')                
# widget = Label(tkroot, text='Hello bind world')
# widget.config(bg='red', font=labelfont)            
# widget.config(height=5, width=20)                  
# widget.pack(expand=YES, fill=BOTH)

# widget.bind('<B1-Motion>', onLeftDrag)             

# widget.focus()                                     
# tkroot.title('Click Me')
# tkroot.mainloop()


# def callback(event):
#     draw(event.x, event.y)

# def draw(x, y):
#     paint.coords(circle, x-20, y-20, x+20, y+20)

# root = Tk()
# paint = Canvas(root)
# paint.bind('<Motion>', callback)
# paint.pack()

# circle = paint.create_oval(0, 0, 0, 0)
# root.mainloop()


# from tkinter import *
# window = Tk()
# # window.state('zoomed')
# window.geometry('600x400')
# window.configure(bg = 'green4')

# def drag(event):
#     print(event.x, event.y)
#     print(dir(event))
#     event.widget.place(x=event.x_root, y=event.y_root,anchor=CENTER)

# card = Canvas(window, width=74, height=97, bg='blue')
# card.place(x=300, y=300,anchor=CENTER)
# card.bind("<B1-Motion>", drag)

# another_card = Canvas(window, width=74, height=97, bg='red')
# another_card.place(x=500, y=300,anchor=CENTER)
# another_card.bind("<B1-Motion>", drag)

# window.mainloop()
