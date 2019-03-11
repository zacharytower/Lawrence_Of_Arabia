'''
Location object source code file

Zachary Tower, Alex Reed, Lucas Bache
'''

class Location(object):
	"""docstring for Location"""
	def __init__(self, 
		title,
		items,
		look_description,
		connected_nodes = {},
		item_reactions = []
		):
		
		self.items = items
		self.look_description = look_description
		self.connected_nodes = connected_nodes
		self.item_reactions = item_reactions


