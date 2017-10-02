import tkinter as tk
import typing as tp
import math

FIELD_WIDTH = 800
FIELD_LENGTH = 600


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

    #Strategy_1 basically try to move defenders to attacker's position
    new_x_att_pos = att_x + att_dx
    new_y_att_pos = att_y + att_dy

    distance_att = math.sqrt((att_dx**(2)+att_dy**(2)))
    distance_def = math.sqrt(((new_x_att_pos - x)**2) + ((new_y_att_pos - y)**2))

    if distance_def < 100:
        return 0, 0
    
    # print(new_x_att_pos,x)
    # print( distance_att,distance_def)
    # print(distance_att/distance_def)

    scale = min(distance_att / distance_def, 1)

    dx = scale * (new_x_att_pos - x)
    dy = scale * (new_y_att_pos - y)
    # multiple by #coefficient to only move defender partial distance to attaker's position


    #dx, dy = -att_dx, -att_dy
    return dx, dy

def strategy_2(x: int, y: int,
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
    #if attack move forward, defender back pedal in a line
    #if attack move backward, defender rushed up in a line
    # also shift defender vertically as attacker move up and down
    print (att_dy)
    if att_dx < 0 and att_dy < 0:
        dx = 0.8 * att_dx #back pedal fast but not as fast as attacker - wanna hold them off
        dy =  att_dy
        return dx,dy
    if att_dx >= 0 and att_dy >= 0:
        dx = 0.2 * (att_dx) #bring the line defender up but not as fast as attacker - prevent counter attack 
        dy =  att_dy
        return dx,dy

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
        prev_x, prev_y = self.x, self.y
        self.move(dx, dy)
        self.callback(prev_x, prev_y, dx, dy)
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

    def __init__(self, strategy_func):
        root = tk.Tk()
        canvas = tk.Canvas(root, width=FIELD_WIDTH, height=FIELD_LENGTH,
                           background='green4', borderwidth=2)
        canvas.create_line(FIELD_WIDTH / 2, 0, FIELD_WIDTH / 2, FIELD_LENGTH,
                           fill='white', width=2)
        canvas.create_oval(FIELD_WIDTH * 0.25 ,FIELD_LENGTH * 0.25,(FIELD_WIDTH) * 0.75,(FIELD_LENGTH)*0.75, fill ='')
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


if __name__ == '__main__':
    app = Application(strategy_1)
    app.start()
