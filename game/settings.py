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

TILE_SIZE = 64
PLAYER_SIZE = (TILE_SIZE, TILE_SIZE * 2)
WIDTH = len(level_data[0]) * TILE_SIZE
HEIGHT = len(level_data) * TILE_SIZE

FPS = 60


# Colors
colors = {
    'tomato': (255, 102, 102),
    'corn_flower': (51, 204, 255)
}
