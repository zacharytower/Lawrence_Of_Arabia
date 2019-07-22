'''
Location object source code file

Zachary Tower, Alex Reed, Lucas Bache
'''
import collections

class Location:
	"""docstring for Location"""
	def __init__(self, 
		title = '',
		items = [],
		look_description = {},
		connected_nodes = {},
		item_reactions = [],
		location = []
		):
		self.title = title
		self.items = items
		self.look_description = look_description
		self.connected_nodes = connected_nodes
		self.item_reactions = item_reactions
		
	def __contains__(self, other):
		return other in self.items
		
	def __iter__(self):
		for item in self.items:
			yield item
	
	def __str__(self):
		if type(self.look_description) == str:
			return self.look_description
		
		elif type(self.look_description) in [type(collections.OrderedDict()), type(dict)]:
			s = ''
			for key in self.look_description.keys():
				if eval(key):
					s += self.look_description[key]
					
			return s
			
#	def load
		
