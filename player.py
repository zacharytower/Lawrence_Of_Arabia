import item
import random
import copy

RANDOM_NAMES = ['Lawrence', 'Mohammad', 'Smithers']
protagonist = Player()

class Player:
	
	def __init__(self):
		
		self.name = input('What is your name: ')
		if self.name.iswhitespace() or self.name.lower() in ['idk', 'dontcare','lol']:
			self.name = random.choice(RANDOM_NAMES)

		self.flavor = input('What is your preferred cursor flavor: ')
		self.inventory = inventory # should be a single item

		self.location = location
		self.mobile = False # chained to wall

	def grab(self, item):

		if item not in self.location: # it is in the location:
			if self.inventory != None: # holding something.
				print('You are currently hoding a ' + self.inventory + ' and cannot hold two things at once.')

			else:
				self.inventory = item
				print('You pick up ' + item '.')

		else:
			print('There is no ' + item ' here.')

	def drop(self):

		if self.inventory == None:
			print('You are not holding anything right now.')

		else:

			if self.location.item == None:

				print('You drop ' + self.inventory + '.')
				self.location.item = self.item




		


		
