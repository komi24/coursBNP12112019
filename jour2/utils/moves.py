def is_outside(pos):
    """
        return False if 0 <= pos < 10
    """
    return pos[0] < 0 or pos[0] >= 10 or pos[1] < 0 or pos[1] >= 10

def turn(car):
    """
        change la direction de car
    """
    car["direction"][0],car["direction"][1]= -car["direction"][1], car["direction"][0]

def move_cars(list_cars):
    for car in list_cars:
        new_position = [
            car["position"][0] + car["direction"][0],
            car["position"][1] + car["direction"][1]
        ]
        if is_outside(new_position):
            print("turn")
            turn(car)
        else:
            car["position"] = new_position