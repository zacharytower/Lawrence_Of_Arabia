import item
import random
import copy
import loa_map
import sys

RANDOM_NAMES = ['Lawrence', 'Mohammad', 'Smithers']
class Player:
	
	def __init__(self): 
		
		self.mobile = False # at the beginning
		self.inventory = []
		self.name = input('What is your name: ')
		if	(
			self.name == '' or
			self.name.isspace() or 
			self.name.lower() in ['idk', 'dontcare','lol']
			):
			
			self.name = random.choice(RANDOM_NAMES)
			
		'''self.flavor = input('What is your preferred cursor flavor: ')
		if (
			self.flavor == '' or
			self.flavor.isspace() or
			self.flavor.lower() in ['idk','meme']
			):'''
		
		self.flavor = '>'
		
		self.location = loa_map.D0 #CHANGE THIS FOR DEBUGGING
		self.dungeon_combo = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(3)) + str(random.randint(10,99))
		self.unlockD1 = False
		self.unlockD2 = False
		self.dead = False
		self.goblins = ''
		self.cipher = random.randint(1, 25)
		
	def __contains__(self, item):
		return item in self.inventory
	def __iter__(self):
		for item in self.inventory:
			yield item
	
	def __len__(self):
		return len(self.inventory)
	
	def acceptModPacket(self, modpack):
		for key, value in modpack:
			if key == 'mobile':
				self.mobile = value
				
			elif key == 'name':
				self.name = value
				
			elif key == 'location':
				self.location = value
			elif key == 'inventory remove':
				try:
					self.inventory.remove(value)
					
				except ValueError:
					pass
			elif key == 'inventory add':
				self.inventory.append(value)
				
			elif key == 'dead':
				print('Game over!')
				sys.exit()
			elif key == 'unlockD1':
				self.unlockD1 = value
			elif key == 'unlockD2':
				self.unlockD2 = value
				
			elif key == 'goblins':
				self.goblins += value
			
	'''def __iadd__(self, other):
		
		assert other not in self.inventory, 'Item {} already in inventory.'.format(other)
		self.inventory.append(other)
	def __isubr__(self, other):
		
		assert other in self.inventory, 'Item {} not in inventory.'.format(other)
		self.inventory.remove(other)'''
	
		
		
	