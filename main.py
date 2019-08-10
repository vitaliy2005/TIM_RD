import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Raketa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 3
        self.dir = 0

    def draw(self):
        arcade.draw_ellipse_filled(self.x, self.y, 40, 60, [200, 0, 0])

class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        # Настроить игру здесь
        self.raketa = Raketa(200, 300)
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
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