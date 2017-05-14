import libtcodpy as libtcod
import Object
import Tile

# Initializing global dimensions
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20
MAP_WIDTH = 80
MAP_HEIGHT = 45
color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)


def handle_keys():
	global playerx, playery

	key = libtcod.console_wait_for_keypress(True)
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	elif key.vk == libtcod.KEY_ESCAPE:
		return True

	if libtcod.console_is_key_pressed(libtcod.KEY_UP):
		player.move(0, -1)

	elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
		player.move(0, 1)

	elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
		player.move(-1, 0)

	elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
		player.move(1, 0)

	elif libtcod.console_is_key_pressed(libtcod.KEY_SPACE):
		pass

def make_map():
	global map

	map = [[Tile.Tile(False) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

	map[30][22].blocked = True
	map[30][22].block_sight = True


def render_all():
	global color_light_wall
	global color_light_ground

	for y in range(MAP_HEIGHT):
		for x in range(MAP_WIDTH):
			wall = map[x][y].block_sight
			if wall:
				libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET)
			else:
				libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET)

	for object in objects:
		object.draw()

	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)


# Set up buffer console
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

# Set up the root console
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

# Set up initial objects
player = Object.Thing(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, '@', libtcod.white, con)
npc = Object.Thing(SCREEN_WIDTH / 2 + 5, SCREEN_HEIGHT / 2, '@', libtcod.dark_yellow, con)
objects = [npc, player]

make_map()

# Main game loop
while not libtcod.console_is_window_closed():
	render_all()

	libtcod.console_flush()

	for object in objects:
		object.clear()
	npc.move(0,1)
	exit = handle_keys()
	if exit:
		break
