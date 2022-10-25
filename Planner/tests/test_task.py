import pytest
import sys
from datetime import date
from src.planner.Task import Task

class TestTaskClass:

	def test_task_data(self):
		task1 = Task(date(2022, 12, 3), date(2022, 12, 10), 'Not started', 'Alice')
		assert task1.get_responsible() == 'Alice'
		assert task1.get_status() == 'Not started'
		assert task1.get_start_date() == date(2022, 12, 3)
		assert task1.get_finish_date() == date(2022, 12, 10)
		with pytest.raises(ValueError):
			task2 = Task(date(2022, 12, 10), date(2022, 12, 3), 'Not started', 'Alice')

	def test_task_updates(self):
		task1 = Task(date(2022, 12, 3), date(2022, 12, 10), 'Not started', 'Alice')
		task1.update_responsible('Mary')
		task1.update_status('In progress')
		task1.update_start_date(date(2022, 12, 5))
		task1.update_finish_date(date(2022, 12, 15)) 
		assert task1.get_responsible() == 'Mary'
		assert task1.get_status() == 'In progress'
		assert task1.get_start_date() == date(2022, 12, 5)
		assert task1.get_finish_date() == date(2022, 12, 15)
		with pytest.raises(ValueError):
			task1.update_start_date(date(2022, 12, 17))
		with pytest.raises(ValueError):
			task1.update_finish_date(date(2022, 12, 1))

if __name__ == "__main__":
	pytest.main()