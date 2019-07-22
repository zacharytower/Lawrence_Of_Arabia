import location
import loa_map
import titlescreen
import player
import playerModPacket

import random
import copy
import os
'''                 TO DO
---The following components are used in your program---
[X] “About the Creators” paragraph in the beginning
[X] An If Statement
[X] A loop (while, do while, or for)
[X] Allows for user input at least 5 times
[ ] There might be some challenges you will have to incorporate… ;)
[X] One more tier
[X] 2 more secret inputs
[X] All pathways must be programmed

'''









helpString = """
	      ~COMMANDS~
Help - Displays possible commands
Get <object> - Picks up object
Use <object> - Uses object
Drop <object> - Drops object
Inventory - Displays all items in your inventory
Look - Provides description of the room you're in
Open <Object> - Opens object and reveals its contents
Inspect <Object> - Inspects object and provides a description
Talk <Person> - initiates a conversation with a person
N - Travels to the room that is North
E - Travels to the room that is East
S - Travels to the room that is South
W - Travels to the room that is West
Compass - Shows available rooms you can travel to
About - A paragraph about the developers
"""

RANDOM_NAMES = ['Lawrence', 'Mohammad', 'Smithers']
RANDOM_BOGUS_STRINGS = ['I don\'t understand that.','What?', 'That didn\'t make too much sense']
developer_paragraph="""
------------------------------------------------------------About The Devs------------------------------------------------------------

		We are three great friends who all take PLTW Computer Science Essentials together.

		Alex Reed is currently taking AP Computer Science A as well, and he has a passion for computer science in general. He has
		developed and published his own mobile game. He also hopes to create more in the future.

		Zach Tower is very logically oriented. He is taking AP Stats, BC Calculus, and loves pursuing his own
		personal projects on the side. His next step is to begin learning about cybersecurity.

		Lucas Bache has always loved computer science. He is very interested in cybersecurity, and would like
		a future job in that area.

		We all plan on furthering our education in the area of computer science at a university in the following year.


---------------------------------------------------------------------------------------------------------------------------------------
"""
# START GAME HERE
titlescreen.titlescreen()
os.system('clear')
 
direction_string_dict = {'n' : 'north',	'e' : 'east',	's' : 'south', 'w' : 'west'}
transitive_verbs = ['use','open','talk to','inspect']
movewords = ['go', 'move','travel']

developer_mode = False
alphanumeric = ''.join(chr(a) for a in range(ord('A'), ord('Z') + 1)) + '0123456789'

def caesar_string(key = 0):
	return(''.join(alphanumeric[(i + key) % 36] for i in range(36)))
	
def main():
	
	protagonist = player.Player() # player initialization  sequence
	os.system('clear')
	print(protagonist.location, '\n')
	print('> type \'help\' for available commands')
	while True:
		user_event = input(protagonist.flavor)
		user_phrase = user_event.lower().strip()
		keywords = user_phrase.split()
		
		if len(keywords) == 0:
			continue
		if user_phrase in protagonist.location.item_reactions.keys():
			modpack = protagonist.location.item_reactions[user_phrase](protagonist)
			if modpack != None:
				protagonist.acceptModPacket(modpack)
			
		elif keywords[0] in 'nesw':
			if protagonist.mobile:
				try:
					direction = keywords[0]
					protagonist.location = protagonist.location.connected_nodes[direction]
					print("You travel into the room that is "+ direction_string_dict[direction] + '.')
					print(protagonist.location)
				except KeyError:
					print('You cannot go ' + direction_string_dict[direction] + '.')
			else:
				print('You are immobile and cannot move right now.')
				if developer_mode:
					if input('(Developer mode cheat) Use force of will to become mobile? [Y/n] ').lower() == 'y':
						protagonist.mobile = True
				
				
		elif keywords[0] in ['help','h']:
			print(helpString)
		elif keywords[0] in ['look','l']: # looking around
			print(protagonist.location)
			
		elif user_phrase in ['use cipher', 'decrypt']:
			if 'cipher' in protagonist:
				while True:
					try:
						key = input('Enter the key: ')
						key = int(key)
						break
				
					except ValueError:
						print('Make sure your key value is numeric.')
				
				print('plain  (outside):' + alphanumeric)
				print('cipher (inside) :' + caesar_string(key))
				
			else:
				print('You cannot decrypt without a cipher.')
		
		elif keywords[0] in ['get','grab']: # retreiving item from environment
			item = keywords[1]
			try:
				if item in protagonist.location:
					protagonist.location.items.remove(item)
					protagonist.inventory.append(item)
					print ('You ' + keywords[0] + ' the ' + keywords[1] + '.')
				
				else:
					print('That is not at this location.')
					
			except IndexError:
				print('You didn\'t say what you want to pick up')
				
		elif keywords[0] in ['drop']: # retrieving item from environment
			item = keywords[1]
			try:
				if item in protagonist:
					protagonist.location.items.append(item)
					protagonist.inventory.remove(item) #remains in inventory for some reason
					print ('You ' + keywords[0] + ' the ' + item)
					
				else:
					print('You do not have ' + item + '.')
					
			except IndexError:
				print('You didn\'t say what you want to drop.')
		
		elif keywords[0] in ['use']:
			item = keywords[1]
			if item in protagonist.inventory: #Only call if player has item
				if item in protagonist.location.item_reactions.keys():
					modpack = protagonist.location.item_reactions[item](protagonist)
					if modpack != None:
						protagonist.acceptModPacket(modpack)
			else:
				print('You do not have that item') #if player does not posses item
		elif keywords[0] in ['eat']:
			item = keywords[1]
			if item in protagonist.inventory: #Only call if player has item	
				print('You eat the',item, '.\nYum!') # yum
				protagonist.inventory.remove(item)
			else:
				print('You do not have that item')
		elif keywords[0] in ['i','inventory']:
			if len(protagonist) == 0:
				print('You are holding nothing.')
			else:
				for i in protagonist:
					print(i)
		elif keywords[0] in ['whoami', 'name']:
			print('Your name is ' + protagonist.name + ', of course.')
			
		elif keywords[0] in ['whereami']:
			print ('You are in the ' + str(protagonist.location.title) + '.')
			
		elif keywords[0] == 'compass':
			try:
				north_title = protagonist.location.connected_nodes['n'].title
				
			except KeyError:
				north_title = '???	'
			try:
				east_title = protagonist.location.connected_nodes['e'].title
				
			except KeyError:
				east_title = '???	'
			try:
				south_title = protagonist.location.connected_nodes['s'].title
				
			except KeyError:
				south_title = '???	'
			try:
				west_title = protagonist.location.connected_nodes['w'].title
				
			except KeyError:
				west_title = '???	'
				
			current_location_title = protagonist.location.title
			for char in [north_title, 'N', '^', '|']:
				print('\t'*4 + char)
				
			print(west_title + '\tW <----------' + current_location_title + '----------> E\t' + east_title)
			for char in ['|', 'v','S', south_title]:
				print('\t'*4 + char)
		
		elif keywords[0]=='about':
			print(developer_paragraph)
		elif keywords[0]=='zmt':
				print(loa_map.ZMT.look_description)
				protagonist.location=loa_map.ZMT
				protagonist.mobile=True
		elif keywords[0]=='116':
				print(loa_map.room_116.look_description)
				protagonist.location=loa_map.room_116
				protagonist.mobile=True
		else: # bogus string
			print(random.choice(RANDOM_BOGUS_STRINGS))
			print('Type \'help\' for available commands')
		
if __name__ == '__main__':
	main()
	
			
