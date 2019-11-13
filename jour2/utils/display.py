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
    
def is_car(position_to_test, list_position):
    for pos in list_position:
        if position_to_test == pos:
            return True
    return False
    
def display_cars(positions):
    for i in range(10):
        line = []
        for j in range(10):
            if is_car([i,j], positions):
                line.append('x')
            else:
                line.append('.')
        print("".join(line))

display_cars([[2,4],[5,2],[1,6]])