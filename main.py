import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

img_background = arcade.load_texture('img/background.jpg')
img_raketa = arcade.load_texture('img/racketa.png')

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
        self.hight = 580 # нужно перевести в метры (сейчас в пиксилях)

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, 40, 80, img_raketa)

    def update(self):
        self.hight = self.y * 10 - 20

    def get_state(self):
        if 35 < self.y < 50 and 300 < self.x < 500:
            return 'down_good'

    def move(self):
        if 0 <= self.x <= SCREEN_HEIGHT:
            self.x += self.dx
        else:
            if self.x < 0:
                self.x = 0
            if self.x > SCREEN_WIDTH:
                self.x = SCREEN_WIDTH - 1

        if self.y >= 40:
            self.y += self.dy
        else:
            if self.y < 40:
                self.y = 40
            # if self.y > SCREEN_HEIGHT:
            #     self.y = SCREEN_HEIGHT - 1

    def to_left(self):
        self.dx -= 0.3

    def to_right(self):
        self.dx += 0.3

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, 40, 80, img_raketa)

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
        self.state = 'run'  # 'game_over', 'win'
        self.background = Background()
        self.raketa = Raketa(400, 580)
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        self.background.draw()
        self.raketa.draw()
        self.draw_telemetry()
        if self.state == 'run':
            pass
        elif self.state == 'game_over':
            pass
        elif self.state == 'win':
            arcade.draw_text('Успешная посадка', 400, 450, [200, 0, 0], 30)
        # Здесь код рисунка

    def on_key_press(self, key: int, modifiers: int):
        if self.state == 'run':
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
        if self.state == 'run':
            self.raketa.move()
            self.raketa.update()
            if self.raketa.get_state() == 'down_good':
                self.state = 'win'

        elif self.state == 'game_over':
            pass
        elif self.state == 'win':
            pass

    def get_telemetry(self):
        telemetry = 'высота: {}\n'.format(round(self.raketa.hight, 2)) + \
                    'скорость снижения: {}\n'.format(round(self.raketa.dy,2)) + \
                    'dx: {} dy: {}\n'.format(round(self.raketa.dx, 2), round(self.raketa.dy, 2)) + \
                    'x: {} y: {}\n'.format(round(self.raketa.x, 2), round(self.raketa.y, 2))

        return telemetry

    def draw_telemetry(self):
        arcade.draw_text(self.get_telemetry(), 10, 450, [200, 0, 0], 20)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()