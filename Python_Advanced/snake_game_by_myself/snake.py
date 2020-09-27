import config
import food
from copy import deepcopy


snake_position = [[config.SCALE * i, 0] for i in range(config.SEGMENTS_COUNT)]

def show():
    for segment in snake_position:
        fill(0,255,0)
        rect(segment[0], segment[1], config.SCALE, config.SCALE)
        

def check_edges():
    if snake_position[-1][0] < 0:
        snake_position[-1][0] = config.WINDOW_LENGTH
    elif snake_position[-1][0] >= config.WINDOW_LENGTH:
        snake_position[-1][0] = 0
    elif snake_position[-1][1] < 0:
        snake_position[-1][1] = config.WINDOW_HEIGTH
    elif snake_position[-1][1] >= config.WINDOW_HEIGTH:
        snake_position[-1][1] = 0

        
def move():
    current_changes = config.DIRECTIONS[config.CURRENT_DIRECTION]
    
    snake_copy = deepcopy(snake_position)
    snake_position[-1][0] += current_changes[0]
    snake_position[-1][1] += current_changes[1]
    
    for i in range(len(snake_position) - 2,-1,-1):
        snake_position[i] = snake_copy[i+1]
    check_edges()
    
    
def eats_itself():
    return any([segment == snake_position[-1] for segment in snake_position[:-1]])
    
            
def touches_food():
    return snake_position[-1] == food.food_position
        
        
def eat_food():
    snake_position.insert(0, snake_position[0])
        



            
