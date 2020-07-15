from sql_alchemy import base

class StudentModel(base.Model):
	__tablename__ = 'students'
	id = base.Column(base.String, primary_key=True)
	name = base.Column(base.String(80))
	intra_id = base.Column(base.String(80))
	# projects = base.Column(base.String(40))

	def __init__(selft, id, name, intra_id):
		selft.id = id
		selft.name = name
		selft.intra_id = intra_id
		#selft.projects

	def json(self):
		return {
			'id': self.id,
			'name': self.name,
			'intra_id': self.intra_id
			#'projects':
		}

	@classmethod
	def find_student(cls, id):
		student = cls.query.filter_by(id=id).first()
		if student:
			return student
		return None

	def save_student(self):
		base.session.add(self)
		base.session.commit()

	def update_student(self, name, intra_id):
		self.name = name
		self.intra_id = intra_id
		# self.projects = projects

	def delete_student(self):
		base.session.delete(self)
		base.session.commit()
