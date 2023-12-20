level_data = [
    '                ',
    '     xx         ',
    '          xx    ',
    '  x      x      ',
    '   xp     xx    ',
    '    xx        x ',
    '        xx   x  ',
    'xxxxxxxxxxxxxxxx',
]

# Sizes
TILE_SIZE = 64
PLAYER_SIZE = (TILE_SIZE, TILE_SIZE)

# Scree dimensions
WIDTH = len(level_data[0]) * TILE_SIZE
HEIGHT = len(level_data) * TILE_SIZE

# Gravity constant
G = 0.8
MAX_G = 16

# Frame per seconds, Delta time
FPS = 60

# Colors
colors = {
    'tomato': (255, 102, 102),
    'corn_flower': (51, 204, 255)
}
