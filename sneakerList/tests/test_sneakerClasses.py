
import pytest
import sys
sys.path.append('/home/gnicolas/Programming/Python/ZeroToHero/sneakerList/src/sneakerList')
from SneakerClasses import Sneaker

class TestSneakerClass:

	def test_sneaker_data(self):
		snkr1 = Sneaker('Nike', 'Jordan1', 9, 150)
		assert snkr1.get_brand() == 'Nike'
		assert snkr1.get_model() == 'Jordan1'
		assert snkr1.get_size() == 9
		assert snkr1.get_price() == 150

if __name__ == "__main__":
	pytest.main()