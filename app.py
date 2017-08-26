import tkinter as tk
import typing as tp


class Attacker:
    x, y = None, None
    SIZE_X, SIZE_Y = 20, 20
    master: tk.Canvas = None
    item_id: int = None
    _click_x, _click_y = None, None

    def __init__(self, master: tk.Canvas, x: int, y: int):
        self.master = master
        self.item_id = master.create_oval(x, y,
                                          x + self.SIZE_X, y + self.SIZE_Y,
                                          fill='blue')
        master.tag_bind(self.item_id, '<Button-1>', func=self.click)
        master.tag_bind(self.item_id, '<B1-Motion>', func=self.drag)

    def click(self, event):
        self._click_x, self._click_y = event.x, event.y
        print(event.x, event.y)

    def drag(self, event):
        canvas: tk.Canvas = event.widget
        current_x, current_y = event.x, event.y
        dx = event.x - self._click_x
        dy = event.y - self._click_y
        self.master.move(self.item_id, dx, dy)
        self._click_x = event.x
        self._click_y = event.y
        # self.x, self.y = event.x, event.y


class Application:
    _canvas: tk.Canvas = None

    def __init__(self, width, height):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=width, height=height,
                           background='green4', borderwidth=2)
        Attacker(canvas)
        canvas.pack()
        self._canvas = canvas
        root.mainloop()

    def drag(self, event):
        canvas: tk.Canvas = event.widget
        x, y = event.x, event.y
        print(x, y)
        # event.widget.place(x=event.x_root, y=event.y_root, anchor=tk.CENTER)


def main():
    app = Application(800, 600)


if __name__ == '__main__':
    main()
