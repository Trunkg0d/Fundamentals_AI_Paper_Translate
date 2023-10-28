BOUND = 15
A = 25 # edge length of node
A1 = 1 # the space between 2 bricks (don't mind it)
COLS, ROWS = 30, 22
RES = WIDTH, HEIGHT = 750+2*BOUND + (COLS-1)*A1, 550+2*BOUND + (ROWS-1)*A1

GREY = (100, 100, 100)
WHITE = (255, 255, 255) # path
YELLOW = (200, 200, 0)  # current node
RED = (200, 0, 0)  # discovered node
BLUE = (30, 144, 255)  # completed node (item of closed set)
PURPLE = (138, 43, 226) # goal
ORANGE = (255,165,0) # start
GREEN = (54, 179, 72)
BLACK = (0, 0, 0) # brick