import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

img_background = arcade.load_texture('img/background.jpg')
img_raketa = arcade.load_texture('img/racketa.png')
img_platform = arcade.load_texture('img/platform.png')


class meteor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 1


class Raketa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = -1
        self.fuel = 100
        self.fuel_comp = 0.3
        self.wind_speed = 0
        self.speed = self.dy
        self.dir = 0
        self.hight = 580 # нужно перевести в метры (сейчас в пиксилях)

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y, 40, 80, img_raketa)

    def update(self):
        self.hight = self.y * 10 - 20
        self.wind_speed += (random.random() - 0.5) / 1.5
        self.fuel -= self.fuel_comp
        if self.fuel <= 0:
            self.dy = - 10

    def get_state(self):
        if 300 < self.x < 500:
            if 40 < self.y < 60:
                if abs(self.dy) < 1:
                    return 'down_good'
                else:
                    return 'cruch'
        elif 0 < self.y < 40:
            return 'cruch'

    def move(self):
        if 0 <= self.x <= SCREEN_HEIGHT:
            self.x += self.dx + self.wind_speed
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
            if self.y > SCREEN_HEIGHT:
                self.y = SCREEN_HEIGHT

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
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, 0, 200, 40, img_platform)


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
            arcade.draw_text('разбился!', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 , [200, 0, 0], 30,
                             width=300, align="center", anchor_x="center", anchor_y="center")
        elif self.state == 'win':
            arcade.draw_text('Успешная посадка', SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 , [200, 0, 0], 30,
                             width=300, align="center", anchor_x="center", anchor_y="center")
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
            elif self.raketa.get_state() == 'cruch':
                self.state = 'game_over'

        elif self.state == 'game_over':
            pass
        elif self.state == 'win':
            pass

    def get_telemetry(self):
        telemetry = 'высота: {}\n'.format(round(self.raketa.hight, 2)) + \
                    'топливо: {} %\n'.format(round(self.raketa.fuel, 2)) + \
                    'скорость снижения: {}\n'.format(round(self.raketa.dy,2)) + \
                    'dx: {} dy: {}\n'.format(round(self.raketa.dx, 2), round(self.raketa.dy, 2)) + \
                    'ветер: {}\n'.format(round(self.raketa.wind_speed, 2)) + \
                    'x: {} y: {}\n'.format(round(self.raketa.x, 2), round(self.raketa.y, 2))

        return telemetry

    def draw_telemetry(self):
        x = 15
        y = 480
        # arcade.draw_point(x, y, [200, 100, 0], 10)
        arcade.draw_text(self.get_telemetry(), 15, 460, [200, 0, 0], 20, anchor_x="left", anchor_y="top")


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
