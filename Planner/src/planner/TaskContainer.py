from Task import Task

class TaskContainer:
	def __init__(self, start_date, finish_date):
		task_list = []
		self.start_date = start_date
		self.finish_date = finish_date

	def add_task(self, task):
		self.task_list.append(task)

	def remove_task(self, task):
		if len(task_list) > 0:
			self.task_list.remove(task)

	def list_all_tasks(self):
		for i in task_list:
			print(i)

	def get_number_tasks(self):
		return len(task_list)