import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

img_background = arcade.load_texture('img/background.jpg')
img_raketa = arcade.load_texture('img/racketa.png')
img_meteor = arcade.load_texture('img/meteor.png')

class meteor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 1


    # def drow(self):
        # arcade.draw_texture_rectangle(self.x, self.y, 20, 20, img_meteor )



class Raketa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = -1
        self.speed = self.dy
        self.dir = 0
        self.hight = 580 # нужно перевести в мнтры (сейчас в пиксилях)



    def move(self):
        self.x += self.dx
        self.y += self.dy

    def update(self):
        self.hight = int(self.y * 10 - 20)

    def to_left(self):
        self.dx -= 0.3

    def to_right(self):
        self.dx += 0.3

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, 40, 80, img_raketa)
        arcade.draw_texture_rectangle(self.x, self.y, 20, 20, img_meteor)

    def power_up(self):
        self.dy += 0.1

    def power_down(self):
        self.dy -= 0.1

class Background:
    def __init__(self):
        # self.img =
        pass

    def draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, img_background)


class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Настроить игру здесь
        self.background = Background()
        self.raketa = Raketa(400, 580)
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.background.draw()
        self.raketa.draw()
        self.draw_telemetry()

        # Здесь код рисунка

    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.raketa.to_left()
        elif key == arcade.key.RIGHT:
            self.raketa.to_right()
        elif key == arcade.key.UP:
            self.raketa.power_up()
        elif key == arcade.key.DOWN:
            self.raketa.power_down()

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        self.raketa.move()
        self.raketa.update()

    def get_telemetry(self):
        telemetry = 'высота: {}\n'.format(self.raketa.hight) + \
                    'скорость снижения: {}\n'.format(self.raketa.dy)
        return telemetry

    def draw_telemetry(self):
        arcade.draw_text(self.get_telemetry(), 10, 500, [200, 0, 0], 25)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()