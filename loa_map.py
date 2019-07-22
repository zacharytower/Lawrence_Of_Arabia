from location import *
import collections
import playerModPacket
import random
import time
import sys

alphanumeric = ''.join(chr(a) for a in range(ord('A'), ord('Z') + 1)) + '0123456789'

def convert_to_caesar(key, string):
	
	normal = caesar_string(0)
	caesar = caesar_string(key)
	sol = str()
	for char in string:
		ind = normal.index(char)
		sol += caesar[(ind) % 36]
		
	return sol
	

def caesar_string(key = 0):
	return(''.join(alphanumeric[(i + key) % 36] for i in range(36)))
	
def _D0_usekey(_):
	print('You unlock yourself.\nYou can now move around.')
	return playerModPacket.PlayerModPacket({'mobile': 'true', 'inventory remove':'key'})

def _D1_inspect_table(_):
	print('The table is small and grimy and has an unlocked drawer.')
	
def _D1_open_drawer(player):
	
	print("""
		You find a few parchment scrolls with Arabic semicursive on it.
		Juxtaposed with the Arabic, you spot some Latin characters:
		``. *		`.*`		,,`
			{}, key 16		``.`
			.`	..`  `.* """.format(player.dungeon_combo)
	)
	
def _D2_useladder(_):
	print('You prop the ladder against the hole in the ceiling. You may move north.')
	D2.connected_nodes['n'] = B2
	del D2.item_reactions['n']
	return playerModPacket.PlayerModPacket({'unlockD2':True})
	
def _D1_move_east(player):
	
	if player.unlockD1:
		return None # it is already unlocked
	
	user_try = input("""
	You see a door made of stone to your east.
	About twice as wide as you are, it appears to be made out of unrefined
	granite.
	In its center, there is a series of five large stone knobs which
	can evidently be twisted into different positions.
	The first three are letters, and the last two are numerals.
	Enter a combination, or type 'exit' to return to the room:
	
	""").lower().strip()
	
	if user_try == 'exit':
		print('You slowly back away, and return to looking around the room')
		
	elif user_try == convert_to_caesar(16, player.dungeon_combo).lower().strip():
		time.sleep(2)
		print("""
		BOOM! The door falls through the floor. You can now move east.		""")
		D1.connected_nodes['e'] = D2
		del D1.item_reactions['e']
		return playerModPacket.PlayerModPacket({'unlockD1':True})
		
	else:
		time.sleep(2)
		print('The combo does not work! Arrows fly towards you, shooting from the wheel. You die!')
		return playerModPacket.PlayerModPacket({'dead':True})
		
		
	
def _D2_move_north(player):
	if player.unlockD2:
		return None # it is already unlocked
	print("You jump up to reach the hole. You are not nearly tall enough.")

def _D2_hidden(_):
	
	print("""
	Underneath the rug, you find a hidden cubby!
	In it is a piece of parchment that says:
		\" Red, then red,
		but first green,
		but very first blue
		then, at last, the first.\"
	
	""") # it's blue, green, red, red, blue

def _B1_move_north(player):
	print("""
	You try at the hatch, but it will not budge.
	You hear a voice deep within the bowels of the basement
	walls echo
	\"hOW QUICKLY WE MAKE HASTE! bEFORE YOU LEAVE THIS
	SEWER, FIRST YOU MUST SOLVE ITS RIDDLE.\"
	""")

def _talkGreenGoblin(player):
	print('\"Ahoy! I am the green goblin\" says the goblin.')
	return playerModPacket.PlayerModPacket({'goblins':'G'})
	
def _talkBlueGoblin(player):
	print('\"Ahoy! I am the blue goblin\" says the goblin.')
	
	if 'bgrrb' in (player.goblins + 'b').lower():
		print("""
				You hear a voice above you say
				\"wELL dONE! yOUR CLEVERNESS HAS SAVED YOU FROM
				A BASEMENTY FATE.\"
				The hatch springs open. Your vision is flooded with light.
			""")
		del B1.item_reactions['n']
	else:
		return playerModPacket.PlayerModPacket({'goblins':'B'})
	

def _talkRedGoblin(player):
	print('\"Ahoy! I am the red goblin\" says the goblin.')
	return playerModPacket.PlayerModPacket({'goblins':'R'})
def _G0_move_north(player):
	if 'guard' in G0.items or 'guard' in player.inventory:
		if 'sword' in player.inventory:
			print('You get past the guard using your sword. You may now move north.')
			G0.connected_nodes['n'] = M0
			del G0.item_reactions['n']
			del G0.items[1]
		else:
			print('you try sneaking past the guard. He awakes, and stabs you in the heart. You die!')
			return playerModPacket.PlayerModPacket({'dead':True})
	else:
		print('You have consumed the guard, allowing you to move north.')
		print(M0.look_description)
		G0.connected_nodes['n'] = M0
		del G0.item_reactions['n']
		return playerModPacket.PlayerModPacket({'location':M0})
D0 = Location(
	title = 'dungeon jail cell',
	items = ['key'],
	look_description = collections.OrderedDict([('True', """
	You find yourself in the jail cell of a dungeon.
	There is sand on the cellar stone floor.
	There is a door to the east.
	You are chained to the wall, free to move
	around but unable to walk in one direction
	for any more than a few feet.\n"""),
	('\'key\' in self.items','\tThere is a key near your feet.')]),
	item_reactions = {
		'key' : _D0_usekey
	}
	
	)
	
D1 = Location(
	title = 'prison anteroom',
	items = ['cipher'],
	look_description = """
	You are in an empty room with a table with a drawer.
	There is a door to the west, and a door to the east.
	The door on the east is made of stone, and appears to be locked.
	You see a small trinket on the ground;  it appears to be a cipher.
	""",
	item_reactions = {
		'inspect table': _D1_inspect_table,
		'look at table': _D1_inspect_table,
		'open table' : _D1_open_drawer,
		'open drawer': _D1_open_drawer,
		'e': _D1_move_east
	}
	)
D2 = Location(
	title = 'ladder room',
	items = ['ladder'],
	look_description = """
	You enter a room with nothing but a ladder and a rug.
	The walls are drab and gray. 
	There is a noticable hole in the ceiling, 
	and you notice a skull in the corner. 
	A chill goes down your spine.
	There is a door to the west.""", # wow, what a poet!
	item_reactions = {
		'ladder' : _D2_useladder,
		'n': _D2_move_north,
		'inspect rug': _D2_hidden,
		'check rug': _D2_hidden
	}
	)
B0 = Location(
	title = 'storage room',
	items = [],
	look_description = """
	You walk into the room, noticing that it is used for storage.
	There are various foodstuffs in the barrels in front of you,
	including meat, an apple, and some water. You are not sure why,
	but the number 116 is engraved into every barrel.
	There is a door the the east.
	There is a blue goblin here!""", 
	item_reactions = {
		'talk goblin' :_talkBlueGoblin
	}
	)
B1 = Location(
	title = 'trash room',
	items = [],
	look_description = """
	A pungent smell hits you as you enter the room.
	It is filled with trash. Piles of useless
	items tower over you. You want to get out
	as soon as you can. You know that there is
	nothing worthwhile here.
	There is a door to the east, and a door to the west.
	There is a hatch here leading north, but it
	is locked.
	
	There is a green goblin here!""",
	item_reactions = {
		'talk goblin': _talkGreenGoblin,
		'n' : _B1_move_north
	}
	)
B2 = Location(
	title = 'basement main room',
	items = ['torch'],
	look_description ="""
	You walk into what appears to be a basement.
	There are weird stains on the ground and walls.
	There is a door to the west, and a ladder to the south.
	There is a red goblin here!""" ,
	item_reactions = {
		'talk goblin' : _talkRedGoblin
	}
	)
G0 = Location(
	title = 'staircase flight',
	items = ['sword', 'guard'],
	look_description = collections.OrderedDict({'True':"""
	You enter a room with a staircase leading up. The stairs
	are grimy, there are rats scurrying over the floor, and 
	odd stains scattering the room. Blood, probably. 
	There is a staircase north and a door to the east.""",
	'\'guard\' in self':"""
	You notice a guard sleeping by the stairwell.
	You are extra quiet to keep him from waking."""}), 
	item_reactions = {
		'n' : _G0_move_north
	}
	)
G1 = Location(
	title = 'anteroom',
	items = [],
	look_description = """
	The room is competely empty, devoid of any life. 
	There is a door to the east and a door to the west.""",
	
	item_reactions = {

	}
	)
def _G2_use_lamp(player):
	if 'lamp' in player.inventory:
		response = input("""You rub the lamp and the blue Will Smith flows from the lamp.
		\"I am Will Smith, the Genie,\" he says, \"and I will grant you one wish.
		Shall I use your wish to open the door? [y/n] """)
		if response == 'y':
			print("The door is unlocked! You are finally free, ",player.name,"!")
			G2.connected_nodes['e']=G3
	else:
		print("You do no have that item")
G2 = Location(
	title = 'chest room',
	items = ['chest', 'sword', 'cup', 'table'],
	look_description = collections.OrderedDict({'True':"""
	You enter a room filled with useless items. Cups, plates,
	shelves, tables, chairs. Old dining equipment. There is a door in the back of the room
	with light peeking out from under it. The door is covered in locks and chains and a semicolon is carved into the door.
	""",
	'\'chest\' in self.items':'You notice a chest on the floor with a silver sword lying next to it.'}), 
	item_reactions = {
		'wish': _G2_use_lamp,
		'rub lamp': _G2_use_lamp,
		'use lamp': _G2_use_lamp
	}
	)
G3 = Location(
	title = 'escape room',
	items = [],
	look_description = """
	You've done it. You have finally escaped from the hellish castle. Sunlight washes over you,
	and you finally feel free. You bask in your happiness.
""",
	
	item_reactions = {

	}
	)
M0 = Location(
	title = 'window room',
	items = [],
	look_description = """
	The room you enter is dark, the only source of light is coming through a small, barred window on the wall.
	There is a door to the east, and a staircase downwards south.
""",
	
	item_reactions = {
	
	}
	)
	
def _M1_move_east(_):
	print("""You immediately come face to face with several guards. You have entered the barracks.
	They all look at you and draw their weapons. You know this is the end.
	You died!""")
	sys.exit()

def _M1_move_north(player):
	response = input("""
	There is a python in the room. You step back, startled. The python says to you,\"David's father has three sons : Snap, Crackle and _____ ? \"
	Your Response: """)
	
	if response.strip().lower() == 'david':
		print('\"Very good',player.name, '! Very very good... You may proceed.\" says the snake. It slithers away, and you can move.')
		print(F1.look_description)
		return playerModPacket.PlayerModPacket({'location': F1})
	else:
		print("\"Wrong answer! Now you DIE!!!\" says the snake. You try to get away, but it pounces and kills you on the spot!\nGame over!")
		return playerModPacket.PlayerModPacket({'dead': True})
		
	
	
M1 = Location(
	title = 'stairwell middle',
	items = [],
	look_description = """
	There is a stairwell north, a door to the west, and a door to the east. 
	The door to the east has some voices coming from it. 
	The room is eerie and cold. You shiver.
""",
	
	item_reactions = {
		'e': _M1_move_east,
		'n': _M1_move_north
	}
	
	)
M2 = Location(
	title = 'barracks',
	items = [],
	look_description = '',
	
	item_reactions = {

	}
	)
F1 = Location(
	title = 'riddle room',
	items = [],
	look_description = 'There is a staircase south and a staircase north',
	
	item_reactions = {
	
	}
	)

F2 = Location(
	title = 'genie room',
	items = ['genie', 'lamp'],
	look_description = """
	You open the door to the room, only to be greeted to the smiling face 
	of Will Smith wearing only a loin cloth and a fez. He is painted entirely blue.
	He claims to have emerged from the lamp to his left. It has a lampshade on it. 
	He says he may grant you freedom, all you have to do is ask for it. You wonder if you are hallucinating. 
	There is a staircase south.
""",
	
	item_reactions = {
	}
	)
	
ZMT = Location(
	title = 'The Zach Room',
	items = [],
	look_description = """
	You suddenly find yourself in a room surrounded by doors.
	Each door has the face of Zachary Tower on it.
	Good luck getting out.
""",
	
	item_reactions = {
	}
	)
room_116 = Location(
	title = 'Room 116',
	items = [],
	look_description = """
	You walk into a room filled to the ceiling in laptops.
	You are told to construct an omniscent robot
	using Scratch and a ball of paperclip and Strings.
""",
	
	item_reactions = {
	}
	)
D0.connected_nodes = {'e':D1}
D1.connected_nodes = {'w':D0}
D2.connected_nodes = {'w':D1, 'n':B2}
B0.connected_nodes = {'e':B1}
B1.connected_nodes = {'w':B0, 'e':B2, 'n':G1}
B2.connected_nodes = {'w':B1,'s':D2}
G0.connected_nodes = {'e':G1, 'n':M0}
G1.connected_nodes = {'e': G2, 'w':G0}
G2.connected_nodes = {'w':G1}
M0.connected_nodes = {'e':M1, 's':G0}
M1.connected_nodes = {'w':M0, 'e':M2, 'n':F1}
F1.connected_nodes = {'n':F2, 's':M1}
F2.connected_nodes = {'s':F1}
ZMT.connected_nodes = {'n':ZMT, 'e': ZMT, 's': ZMT, 'w':ZMT}
room_116.connected_nodes = {'n':G3 }