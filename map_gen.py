map_size_x = 40
map_size_y = 40
max_features = 20
room_chance = 50

import random

class tiles:
	tiles_chars = {'stone': ' ', 'wall': '#', 'room': '.', 'stair': '>', 'door': '+'}
	tiles_id = {'stone': 0, 'wall': 1, 'room': 2, 'stair': 3, 'door': 4}

	def __init__(self, key, char):
		self.tiles[key] = char
 
	def get_shape(self, key):
		return self.tiles[key]
 
	def set_shape(self, key, char):
		self.tiles[key] = char


class dungeon:
	_map_size = (0, 0)
	tiles_map = []

	def __init__(self, map_size_x, map_size_y, max_features, room_chance):
		self._map_size = (map_size_x, map_size_y)
		for x in range (0, self._map_size[0]):
			self.tiles_map.append([])
			for y in range (0,  self._map_size[1]):
				self.tiles_map[x].append(tiles.tiles_id["stone"])

def draw_room(x=dungeon._map_size[0]/2, y=dungeon._map_size[1]/2, w=4, h=4):
	for col in range (x, x+w):
		for line in range (y, y+h):
			dungeon.tiles_map[line][col] = tiles.tiles_id["room"]


		
	
		

def main():
	dungeon(map_size_x, map_size_y, max_features, room_chance)
	draw_room()
#	direction = choose_direction()
#	feat = choose_feature()
#	if has_space(): # goto direction = choose_direction()
#		print('placeholder. has space')
#	add_feature()
#	# repeat direction - feat - if has_space - add_feature until completion or max_iter
#	add_stairs()
#	add_items()
#	add_monsters()

if __name__ == '__main__':
	main()
