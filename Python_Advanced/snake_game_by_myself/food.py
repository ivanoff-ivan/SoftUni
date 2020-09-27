import config
import snake

x = (random(0, config.WINDOW_LENGTH) // config.SCALE) * config.SCALE
y = (random(0, config.WINDOW_HEIGTH) // config.SCALE) * config.SCALE
food_position = [x, y]


def show():
    fill(255,0,0)
    rect(food_position[0], food_position[1], config.SCALE, config.SCALE)
    
    
def reset():
    x = (random(0, config.WINDOW_LENGTH) // config.SCALE) * config.SCALE
    y = (random(0, config.WINDOW_HEIGTH) // config.SCALE) * config.SCALE
    food_position[0] = x
    food_position[1] = y
    
