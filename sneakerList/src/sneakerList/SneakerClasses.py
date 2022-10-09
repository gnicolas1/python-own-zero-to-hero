
class Sneaker:
	"""Sneaker objet: brand, model, size, price"""
	def __init__(self, brand, model, size, price):
		self.brand = brand
		self.model = model
		self.size = size
		self.price = price

	def get_brand(self):
		return self.brand

	def get_model(self):
		return self.model

	def get_size(self):
		return self.size

	def get_price(self):
		return self.price

	def __str__(self):
		pass

	def __repr__(self):
		return 'Sneaker({}, {}, {}, {})'.format(self.brand, self.model, self.size, self.price)

class SneakerList:

	def __init__(self):
		pass
	def add_sneaker(self, sneaker):
		pass
	def remove_sneaker(self, sneaker):
		pass
	def find_sneaker_by_brand(self, brand):
		pass
	def find_sneaker_by_model(self, model):
		pass
	def find_sneaker_by_size(self, model):
		pass
	def find_sneaker_by_price(self, model):
		pass
	def __str__(self):
		pass
	def __repr__(self):
		pass