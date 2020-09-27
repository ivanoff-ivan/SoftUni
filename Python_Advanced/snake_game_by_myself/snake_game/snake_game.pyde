import config
import snake
import food


def end_screen():
    background(150)
    fill(255)
    textSize(64)
    text(config.GAME_OVER_MESSAGE, config.WINDOW_LENGTH / 2 - len(config.GAME_OVER_MESSAGE) * 20,
         config.WINDOW_HEIGTH / 2)

def setup():
    size(config.WINDOW_LENGTH, config.WINDOW_HEIGTH)
    frameRate(10)
    
    
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
    
    if snake.eats_itself():
        end_screen()
        noLoop()

        
def keyPressed():
    if keyCode == UP and config.CURRENT_DIRECTION != "down":
        config.CURRENT_DIRECTION = "up"
    elif keyCode == RIGHT and config.CURRENT_DIRECTION != "left":
        config.CURRENT_DIRECTION = "right"
    elif keyCode == DOWN and config.CURRENT_DIRECTION != "up":
        config.CURRENT_DIRECTION = "down"
    elif keyCode == LEFT and config.CURRENT_DIRECTION != "right":
        config.CURRENT_DIRECTION = "left"
        
