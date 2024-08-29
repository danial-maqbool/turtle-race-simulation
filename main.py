import turtle
import random
from typing import List, Any

WIDTH, HEIGHT = 750, 1000
MIN_RACERS, MAX_RACERS = 2, 6
COLORS = ['VioletRed', 'Gold', 'Chartreuse', 'MediumTurquoise', 'PowderBlue', 'DarkOrchid']
SHAPES = ['arrow', 'circle', 'classic', 'square', 'triangle', 'turtle']


def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')
    return screen


def get_racer_quantity() -> int:
    racers = 0
    while True:
        user_input = input('Enter number of Racers (' + str(MIN_RACERS) + ' - ' + str(MAX_RACERS) + '): ')
        if user_input.isdigit():
            racers = int(user_input)
            if MIN_RACERS <= racers <= MAX_RACERS:
                return racers
            else:
                print('Please enter a value between', MIN_RACERS, '-', MAX_RACERS, '!')
                continue
        else:
            print('Please enter only numeric values!')


def create_racers(quantity) -> list:
    list_of_racers = []

    random.shuffle(COLORS)
    random.shuffle(SHAPES)

    colors = COLORS[:quantity]
    shapes = SHAPES[:quantity]

    factor_x_gap = WIDTH // (quantity + 1)
    space_y = -HEIGHT // 2 + 20

    for i in range(quantity):
        space_x = -WIDTH // 2 + (i + 1) * factor_x_gap

        racer = turtle.Turtle()
        racer.color(colors[i])
        racer.shape(shapes[i])
        racer.left(90)
        racer.penup()
        racer.setpos(space_x, space_y)
        racer.pendown()
        list_of_racers.append(racer)

    return list_of_racers


def start_race(racers):
    while True:
        for racer in racers:
            extra_distance = lucky_boost()
            if extra_distance != 0:
                print(f'{COLORS[racers.index(racer)]} {SHAPES[racers.index(racer)]} got an extra boost of {extra_distance}')
            distance = random.randrange(1, 20) + extra_distance
            racer.forward(distance)

            x, y = racer.pos()
            extra_distance = 0
            if y >= HEIGHT // 2 - 15:
                return COLORS[racers.index(racer)], SHAPES[racers.index(racer)]


def lucky_boost():
    boost = 0
    if random.randint(1, 200) == 200:
        boost = random.randrange(15, 30)

    return boost


number_of_racers = get_racer_quantity()
window = init_screen()
racers = create_racers(number_of_racers)
winner_color, winner_shape = start_race(racers)

print(f'The winner is {winner_color} {winner_shape}')

window.exitonclick()
