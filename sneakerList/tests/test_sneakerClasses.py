
import pytest
import sys
#sys.path.append("..")
from src.sneakerList.SneakerClasses import Sneaker, SneakerList

class TestSneakerClass:

	def test_sneaker_data(self):
		snkr1 = Sneaker('Nike', 'Jordan1', 9, 150, 'M')
		assert snkr1.get_brand() == 'Nike'
		assert snkr1.get_model() == 'Jordan1'
		assert snkr1.get_size() == 9
		assert snkr1.get_price() == 150
		assert snkr1.get_gender() == 'M'

	def test_sneaker_list(self):
		snkr_list = SneakerList()
		snkr_list_items_to_add = [
			Sneaker('Nike', 'Jordan1 Retro High OG Starfish', 9, 120, 'M'),
			Sneaker('Reebok', 'Shaq Attaq Orlando (2022)', 10.5, 210, 'M'),
			Sneaker('Puma', 'LaMelo Ball MB.01 Galaxy', 4.5, 164, 'W'),
			Sneaker('Adidas', 'Campus 80s South Park Towelie', 3, 129, 'W'),
			Sneaker('Nike', 'Dunk Low Medium Olive', 3.5, 168, 'W'),
			Sneaker('Converse', 'Run Star Motion White Black Gum', 10.5, 85, 'M'),
			Sneaker('Nike', 'Jordan4 Retro SE Black Canvas', 12, 296, 'M'),
			Sneaker('Reebok', 'Pump Omni Zone II Celtics', 4.5, 102, 'W'),
			Sneaker('Adidas', 'Samba Vegan White Gum', 13.5, 108, 'M'),
			Sneaker('Puma', 'RS-X Rick and Morty', 9, 102, 'M'),
			Sneaker('Nike', 'Dunk Low Safari Mix', 4, 126, 'W'),
			Sneaker('Puma', 'Suede Rhuigi Villasenor', 8.5, 84, 'M')
		]

		for item in snkr_list_items_to_add:
			snkr_list.add_sneaker(item)

		assert snkr_list.get_number_of_sneakers() == 12
		
		brand_list = snkr_list.filter_sneaker_by_brand("Nike")
		assert len(brand_list) == 4

		brand_list = snkr_list.filter_sneaker_by_brand("Under Armour")
		assert len(brand_list) == 0

		model_list = snkr_list.filter_sneaker_by_model("Dunk Low Safari Mix")
		assert len(model_list) == 1

		model_list = snkr_list.filter_sneaker_by_model("UA Charger Vantage 2")
		assert len(model_list) == 0

		size_list = snkr_list.filter_sneaker_by_size(9)
		assert len(size_list) == 2

		size_list = snkr_list.filter_sneaker_by_size(9.5)
		assert len(size_list) == 0

		price_list = snkr_list.filter_sneaker_by_price(102)
		assert len(price_list) == 2

		price_list = snkr_list.filter_sneaker_by_price(100)
		assert len(price_list) == 0

		gender_list = snkr_list.filter_sneaker_by_gender("W")
		assert len(gender_list) == 5

		gender_list = snkr_list.filter_sneaker_by_gender("M")
		assert len(gender_list) == 7

		attr_list = snkr_list.filter_sneaker_by_attributes([('brand', ''), ('model', ''), ('size', ''), ('price', ''), ('gender', '')])
		assert attr_list == "Filter list is empty!"

		attr_list = snkr_list.filter_sneaker_by_attributes([('brand', 'Under Armour'), ('model', ''), ('size', ''), ('price', ''), ('gender', '')])
		assert attr_list == "No matches were found"

		attr_list = snkr_list.filter_sneaker_by_attributes([('brand', ''), ('model', 'Samba Vegan White Gum'), ('size', ''), ('price', ''), ('gender', '')])
		assert len(attr_list) == 1

		attr_list = snkr_list.filter_sneaker_by_attributes([('brand', ''), ('model', ''), ('size', 9), ('price', ''), ('gender', 'M')])
		assert len(attr_list) == 2

if __name__ == "__main__":
	pytest.main()