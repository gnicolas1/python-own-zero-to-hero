from datetime import date

class Task: 
	"""Create task"""
	def __init__(self, start_date, finish_date, status, responsible):
		if finish_date >= start_date:
			self.start_date = start_date
			self.finish_date = finish_date
			self.status = status
			self.responsible = responsible
		else:
			raise ValueError('finished date should be greater or equal to started date')

	def get_start_date(self):
		return self.start_date

	def get_finish_date(self):
		return self.finish_date

	def get_status(self):
		return self.status

	def get_responsible(self):
		return self.responsible

	def update_start_date(self, new_start_date):
		if new_start_date <= self.finish_date:
			self.start_date = new_start_date
		else:
			raise ValueError('started date should be less or equal to finished date')

	def update_finish_date(self, new_finish_date):
		if new_finish_date >= self.start_date:
			self.finish_date = new_finish_date
		else:
			raise ValueError('finished date should be greater or equal to started date')

	def update_status(self, new_status):
		self.status = new_status

	def update_responsible(self, new_responsible):
		self.responsible = new_responsible
	
	def __str__(self):
		return 'Task is scheduled from {} to {} with status: {} will be done by {} '.format(self.start_date, self.finish_date, self.status, self.responsible)

	def __repr__(self):
		return 'Task({}, {})'.format(self.start_date, self.finish_date)
