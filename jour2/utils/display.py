def display_car(position):
    """
        Affiche une map 10x10 avec un 'x'
        sur la coordonnée position et des points
        sur les autres coordonnées
        
        :Example:
        >>> display_car([4,1])
        ..........
        ....x.....
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........
        ..........        
    """
    for i in range(10):
        line = []
        for j in range(10):
            if [i,j] == position:
                line.append('x')
            else:
                line.append('.')
        print("".join(line))
    
def is_car(position_to_test, list_cars):
    for car in list_cars:
        if position_to_test == car["position"]:
            return True
    return False
    
def display_cars(list_cars):
    for i in range(10):
        line = []
        for j in range(10):
            if is_car([i,j], list_cars):
                line.append('x')
            else:
                line.append('.')
        print("".join(line))

if __name__ == "__main__":
    display_cars([[2,4],[5,2],[1,6]])