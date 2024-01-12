import random
import curses

# Window setup
cursor = curses.initscr()
curses.curs_set(0)
height, width = cursor.getmaxyx()
window = curses.newwin(height, width, 0, 0)
window.keypad(1)
window.timeout(100)

# Draw snake
snake_x = width / 4
snake_y = height / 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Draw fruit
food = [height/2, width/2]
window.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Controls
key = curses.KEY_RIGHT
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key
    # If snake hits itself, you lose
    if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    
    snake.insert(0, new_head)

    