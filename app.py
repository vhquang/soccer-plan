import tkinter as tk
import typing as tp


class Player:
    master: tk.Canvas = None
    x, y = None, None
    SIZE_X, SIZE_Y = 20, 20
    color = 'white'
    item_id: int = None

    def __init__(self, master: tk.Canvas, x: int, y: int):
        self.master = master
        self.item_id = master.create_oval(x, y,
                                          x + self.SIZE_X, y + self.SIZE_Y,
                                          fill=self.color)


class Attacker(Player):
    color = 'blue'
    _click_x, _click_y = None, None

    def __init__(self, master: tk.Canvas, x: int, y: int):
        super().__init__(master, x, y)
        master.tag_bind(self.item_id, '<Button-1>', func=self.click)
        master.tag_bind(self.item_id, '<B1-Motion>', func=self.drag)

    def click(self, event):
        self._click_x, self._click_y = event.x, event.y

    def drag(self, event):
        dx = event.x - self._click_x
        dy = event.y - self._click_y
        self.master.move(self.item_id, dx, dy)
        self._click_x = event.x
        self._click_y = event.y


class Application:
    _canvas: tk.Canvas = None

    def __init__(self, width, height):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=width, height=height,
                           background='green4', borderwidth=2)
        _ = Attacker(canvas, 20, 20)
        canvas.pack()
        self._canvas = canvas
        root.mainloop()


def main():
    app = Application(800, 600)


if __name__ == '__main__':
    main()
