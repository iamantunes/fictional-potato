map_size_x = 40
map_size_y = 40
max_features = 20
room_chance = 50

import random


class tiles:
    tiles_chars = {'stone': ' ', 'wall': '#', 'floor': '.', 'stair': '>', 'door': '+'}
    tiles_id = {'stone': 0, 'wall': 1, 'floor': 2, 'stair': 3, 'door': 4}

    def __init__(self, key, char):
        self.tiles[key] = char

    def get_shape(self, key):
        return self.tiles[key]

    def set_shape(self, key, char):
        self.tiles[key] = char


class dungeon:
    _map_size = (40, 40)
    tiles_map = []

    def __init__(self, map_size_x, map_size_y, max_features, room_chance):
        self._map_size = (map_size_x, map_size_y)
        for x in range(0, self._map_size[0]):
            self.tiles_map.append([])
            for y in range(0, self._map_size[1]):
                self.tiles_map[x].append(tiles.tiles_id["stone"])


def draw_room(id = 0, x=dungeon._map_size[0] / 2, y=dungeon._map_size[1] / 2, w=4, h=4):
    x, y = round(x), round(y)

    for col in range(x, x + w):
        for line in range(y, y + h):
            #dungeon.tiles_map[line][col] = tiles.tiles_id["floor"]
            if dungeon.tiles_map[line][col] > 1:
                pass
            else:
                dungeon.tiles_map[round(y+(h/2))][round(x+(w/2))] = id+100
                dungeon.tiles_map[line][col] = id


def where(tiles, id):
    for line in range(len(tiles)):
        for col in range(len(tiles[0])):
            if dungeon.tiles_map[line][col] == id:
                x, y = col, line
            else:
                pass
    return x, y


def draw_corridor(tiles):
    for id in range(101, 120):

        x1, y1 = where(tiles, id)
        x2, y2 = where(tiles, id+1)
        for line in range(y1, y2):
            dungeon.tiles_map[line][x1] = 50
        for col in range(x1, x2):
            dungeon.tiles_map[y2][col] = 50




def choose_direction():
    direction = random.randint(1, 4)  # Clockwise starting from north
    return direction


def choose_feature():
    indicator = random.randint(0, 100)
    print('Percentage: {}'.format(indicator))
    if indicator in range(0, 25):
        feature = 'corridor'
    elif indicator in range(25, 50):
        feature = 'round room'
    elif indicator in range(50, 100):
        feature = 'square room'
    length = random.randint(1, 12)
    width = random.randint(4, 10)
    height = random.randint(4, 10)
    return feature, length, width, height


def has_space(feat, length, width, height):
    print('has no space. correct the has_space function')


def main():
    dungeon(map_size_x, map_size_y, max_features, room_chance)
    iteration = 0
    while iteration < 20:
        iteration +=1
        draw_room(id = iteration, x=random.randint(1, 32), y=random.randint(1, 32), w=random.randint(4,8), h=random.randint(4,8))  # while number of tries < n keep trying to add new random rooms
    # direction = choose_direction()
    dir = choose_direction()
    feat, length, width, height = choose_feature()
    print('Direction: {}'.format(dir))
    print('Feature: {}'.format(feat))
    draw_corridor(dungeon.tiles_map)
    for col in range(0, 40):
        for line in range(0, 40):
            cels = dungeon.tiles_map
            if dungeon.tiles_map[line][col] > 100:
                dungeon.tiles_map[line][col] = 'X'
            elif dungeon.tiles_map[line][col] == 0:
                dungeon.tiles_map[line][col] = '#'
            else:
                dungeon.tiles_map[line][col] = ' '









    # if has_space(): # goto direction = choose_direction()
    # 	print('placeholder. has space')
    # add_feature()
    # # repeat direction - feat - if has_space - add_feature until completion or max_iter
    # add_stairs()
    # add_items()
    # add_monsters()

if __name__ == '__main__':
    main()

    for l in range(40):
    	print(dungeon.tiles_map[l])
