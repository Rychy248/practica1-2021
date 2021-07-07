#MY CODE FOR MAZE
def turn_right():
    for i in range(3):
        turn_left()
        
def turn_behaind():
    turn_left()
    turn_left()
        
def wall_behaind():
    turn_left()
    turn_left()
    is_wall = False
    if wall_in_front():
        is_wall = True
    turn_left()
    turn_left()
    return is_wall

def wall_on_left():
    turn_left()
    is_wall = False
    if wall_in_front():
        is_wall = True  
    turn_right()
    return is_wall

sound(True)
while not(at_goal()):
    if right_is_clear() and wall_on_left():
        print("derecha1 libre izquierda no")
        turn_right()
        move()
    elif front_is_clear():
        print("Frente libre")
        move()
    elif right_is_clear():
        print("derecha libre ")
        turn_right()
        move()
    elif not(wall_on_left()):
        print("izquierda libre")
        turn_left()
        move()
    elif not(wall_behaind()):
        print("atras libre")
        turn_behaind()
        move()
