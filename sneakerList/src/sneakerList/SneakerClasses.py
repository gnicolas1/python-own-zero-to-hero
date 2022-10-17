class Sneaker:
	"""Sneaker list object that contains a list of sneakers"""
	def __init__(self, brand, model, size, price, gender):
		self.brand = brand
		self.model = model
		self.size = size
		self.price = price
		self.gender = gender

	def get_brand(self):
		return self.brand

	def get_model(self):
		return self.model

	def get_size(self):
		return self.size

	def get_price(self):
		return self.price

	def get_gender(self):
		return self.gender

	def __repr__(self):
		return 'Sneaker({}, {}, {}, {})'.format(self.brand, self.model, self.size, self.price, self.gender)

class SneakerList:
	"""List of sneakers"""
	def __init__(self):
		self.sneaker_list = []

	def add_sneaker(self, sneaker):
		self.sneaker_list.append(sneaker)

	def remove_sneaker(self, sneaker):
		self.sneaker_list.remove(sneaker)

	def filter_sneaker_by_brand(self, brand):
		return [item for item in self.sneaker_list if item.brand == brand]

	def filter_sneaker_by_model(self, model):
		return [item for item in self.sneaker_list if item.model == model]

	def filter_sneaker_by_size(self, size):
		return [item for item in self.sneaker_list if item.size == size]

	def filter_sneaker_by_price(self, price):
		return [item for item in self.sneaker_list if item.price == price]

	def filter_sneaker_by_gender(self, gender):
		return [item for item in self.sneaker_list if item.gender == gender]

	def filter_sneaker_by_attributes(self, attributes_list):
		if (attributes_list[0][1] != '') or (attributes_list[1][1] != '') or (attributes_list[2][1] != '') or (attributes_list[3][1] != '') or (attributes_list[4][1] != ''):
			attr_filter = []
			if attributes_list[0][1] != '':
				brand_f = attributes_list[0][1]
				brand_l = self.filter_sneaker_by_brand(brand_f)
				if len(brand_l) > 0:
					attr_filter.append(brand_l)
			
			if attributes_list[1][1] != '':
				model_f = attributes_list[1][1]
				model_l = self.filter_sneaker_by_model(model_f)
				if len(model_l) > 0:
					attr_filter.append(model_l)	
			
			if attributes_list[2][1] != '':
				size_f = attributes_list[2][1]
				size_l = self.filter_sneaker_by_size(size_f)
				if len(size_l) > 0:
					attr_filter.append(size_l)
			
			if attributes_list[3][1] != '':
				price_f = attributes_list[3][1]
				price_l = self.filter_sneaker_by_price(price_f)
				if len(price_l) > 0:
					attr_filter.append(price_l)
			
			if attributes_list[4][1] != '':
				gender_f = attributes_list[4][1]
				gender_l = self.filter_sneaker_by_gender(gender_f)
				if len(gender_l) > 0:
					attr_filter.append(gender_l)

			if len(attr_filter) == 0:
				return "No matches were found"
				
			if len(attr_filter) == 1:
				return attr_filter[0]

			else:
				set_attr = set(attr_filter[0])
				for i in range(len(attr_filter) - 1):
					set_attr &= set(attr_filter[i+1])

				return [i for i in set_attr]
		else:
			return "Filter list is empty!"

	def get_number_of_sneakers(self):
		return len(self.sneaker_list)

	def __repr__(self):
		return "Sneaker List: {}".format(self.sneaker_list)