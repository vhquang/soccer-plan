import tkinter as tk
import typing as tp


def strategy_1(x: int, y: int,
               att_x: int, att_y: int,
               att_dx: int, att_dy: int) -> tp.Tuple[int, int]:
    """
    Calculate the move needed by the defender

    :param x: current x-axis defender position
    :param y: current y-axis defender position
    :param att_x: current x-axis attacker position
    :param att_y: current y-axis attacker position
    :param att_dx: attacker x delta
    :param att_dy: attacker y delta
    :return: dx, dy that the defender need to move
    """
    dx, dy = -att_dx, -att_dy
    return dx, dy


class Player:
    """
    The base class for Attacker and Defender
    """
    master: tk.Canvas = None
    x, y = None, None
    SIZE_X, SIZE_Y = 20, 20
    color = 'white'
    item_id: int = None

    def __init__(self, master: tk.Canvas, x: int, y: int):
        self.master = master
        self.x, self.y = x, y
        length_x, length_y = x + self.SIZE_X, y + self.SIZE_Y
        self.item_id = master.create_oval(x, y, length_x, length_y,
                                          fill=self.color)

    def move(self, dx: int, dy: int):
        self.master.move(self.item_id, dx, dy)
        self.x += dx
        self.y += dy


class Attacker(Player):
    """
    The Attacker class is draggable, and will update back to the game about its
    movement.
    """
    color = 'red'
    _click_x, _click_y = None, None
    callback: tp.Callable

    def __init__(self, master: tk.Canvas, x: int, y: int,
                 update_callback: tp.Callable):
        super().__init__(master, x, y)
        master.tag_bind(self.item_id, '<Button-1>', func=self.click)
        master.tag_bind(self.item_id, '<B1-Motion>', func=self.drag)
        self.callback = update_callback

    def click(self, event):
        self._click_x, self._click_y = event.x, event.y

    def drag(self, event):
        dx = event.x - self._click_x
        dy = event.y - self._click_y
        self.move(dx, dy)
        self.callback(self.x, self.y, dx, dy)
        self._click_x = event.x
        self._click_y = event.y


class Defender(Player):
    color = 'blue'

    def __init__(self, master: tk.Canvas, x: int, y: int):
        super().__init__(master, x, y)


class Application:
    """
    Main application logic, that will create the board, and handle strategy
    """
    _canvas: tk.Canvas = None
    defenders: tp.List[Defender] = []
    strategy: tp.Callable = None

    def __init__(self, width, height, strategy_func):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=width, height=height,
                           background='green4', borderwidth=2)
        _ = Attacker(canvas, 600, 300, update_callback=self.update_defenders)
        self.defenders.append(Defender(canvas, 200, 100))
        self.defenders.append(Defender(canvas, 200, 300))
        self.defenders.append(Defender(canvas, 200, 500))
        canvas.pack()
        self._canvas = canvas
        self.root = root
        self.strategy = strategy_func

    def update_defenders(self, att_x, att_y, att_dx, att_dy):
        for player in self.defenders:
            dx, dy = self.strategy(player.x, player.y,
                                   att_x, att_y, att_dx, att_dy)
            player.move(dx, dy)

    def start(self):
        self.root.mainloop()


def main():
    app = Application(800, 600, strategy_1)
    app.start()


if __name__ == '__main__':
    main()
