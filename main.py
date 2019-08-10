import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

img_background = arcade.load_texture('img/background.jpg')
img_raketa = arcade.load_texture('img/racketa.png')

class Raketa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.dir = 0

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, 40, 80, img_raketa)

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
        self.raketa = Raketa(200, 300)
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.background.draw()
        self.raketa.draw()
        # Здесь код рисунка

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()