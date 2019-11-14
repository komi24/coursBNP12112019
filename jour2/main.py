import os
from time import sleep

from utils.display import display_cars
from utils.moves import move_cars


list_positions = [[2,4],[5,2],[1,6]]
# list_positions.remove([2,4])
# list_positions.pop(1)
list_cars = [
    {"marque": "Mercedes", "position": pos, "direction": [0,1]}
    for pos in list_positions
]

"""
    Dans utils.moves
    Faire une fonction move_cars(list_cars)
    qui déplace toutes les voitures d'une case
    vers la droite
"""
for i in range(20): # Pendant 20 tours
    os.system("cls")
    display_cars(list_cars)
    move_cars(list_cars)
    sleep(1)