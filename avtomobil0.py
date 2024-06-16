'''from random import random

time = 50
car_positions = [1, 1, 1]

while time:
    # decrease time
    time -= 1

    print('')
    for i in range(len(car_positions)):
        # move car
        if random() > 0.3:
            car_positions[i] += 1

        # draw car
        print('-' * car_positions[i])
'''
from random import random

def initialize_simulation(time_length, num_cars):
    time = time_length
    car_positions = [1] * num_cars
    return time, car_positions

def update_positions(car_positions):
    for i in range(len(car_positions)):
        if random() > 0.3:
            car_positions[i] += 1
    return car_positions

def display_positions(car_positions):
    for position in car_positions:
        print('-' * position)

def display_winner(car_positions):
    max_position = max(car_positions)
    winners = [i + 1 for i, pos in enumerate(car_positions) if pos == max_position]
    if len(winners) == 1:
        print(f"\nПобедитель - автомобиль номер {winners[0]} с позицией {max_position}!")
    else:
        print(f"\nПобедители - автомобили номера {', '.join(map(str, winners))} с позицией {max_position}!")

def run_simulation():
    time_length = 15
    num_cars = 5
    time, car_positions = initialize_simulation(time_length, num_cars)
    while time:
        time -= 1
        car_positions = update_positions(car_positions)
        print('')
        display_positions(car_positions)
    display_winner(car_positions)

if __name__ == '__main__':
    run_simulation()

