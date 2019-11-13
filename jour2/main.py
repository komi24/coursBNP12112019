import os
from time import sleep

from utils.display import display_cars


list_cars = [[2,4],[5,2],[1,6]]

"""
    Faire une fonction move_cars(list_cars)
    qui déplace toutes les voitures d'une case
    vers la droite
"""
for i in range(20): # Pendant 20 tours
    os.system("cls")
    display_cars(list_cars)
    sleep(1)