import curses
import creatures as crt
import map_generation as map_gen



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




stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(False)
if curses.has_colors():
	curses.start_color()
stdscr.keypad(True)
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
stdscr.addstr("Welcome to my game!", curses.A_REVERSE)
stdscr.chgat(-1, curses.A_REVERSE)
stdscr.addstr(curses.LINES-1, 0, "Press 'q' to quit.")
window = curses.newwin(curses.LINES-2, curses.COLS, 1, 0)
text_window = window.subwin(curses.LINES-6, curses.COLS-4, 3, 2)
text_window.addstr("Waiting for input")
window.box()
stdscr.noutrefresh()
window.noutrefresh()
curses.doupdate()

def move_player(c):
	if c == ord('w'):
		crt.character.y -=1
	if c == ord('s'):
		crt.character.y +=1
	if c == ord('a'):
		crt.character.x -=1
	if c == ord('d'):
		crt.character.x +=1

def draw_player(x, y):
	text_window.addstr(y, x, crt.character.char)

	

def main():
	text_window.insstr(crt.character.x, crt.character.y, crt.character.char)
	stdscr.noutrefresh()
	window.noutrefresh()
	curses.doupdate()
	while True:
		text_window.clear()
		c = window.getch()
		move_player(c)
		draw_room()
		for x in range (0, 35):
			for y in range (0, 35):
				stdscr.addstr(y, x, dungeon.tiles_map[x][y])
		draw_player(crt.character.x, crt.character.y)
		text_window.refresh()

				
		
		if c == ord('q'):
			break

		else:
			continue

		stdscr.noutrefresh()
		window.noutrefresh()
		text_window.noutrefresh()
		curses.doupdate()

def finish():
	curses.nocbreak()
	curses.echo()
	curses.curs_set(True)
	curses.endwin()


if __name__ == "__main__":

	main()
	finish()

