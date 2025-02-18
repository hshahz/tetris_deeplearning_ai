RED = (255, 0, 0)
GREEN = (0, 230, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
LIGHT_GRAY = (192, 192, 192)
DARK_GRAY = (64, 64, 64)
PINK = (255, 175, 175)
ORANGE = (204, 80, 0)
PURPLE = (102, 0, 153)
PINK = (255, 105, 180)

colors = [BLACK, RED, GREEN, CYAN, MAGENTA, BLUE, ORANGE, YELLOW, BLUE, (0, 237, 165), (22, 172, 237)]
cmap = dict()
for i in range(17):
    if i < len(colors):
        cmap[i] = colors[i]
    else:
        cmap[i] = ORANGE
