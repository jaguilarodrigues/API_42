from flask_restful import Resource, reqparse
from models.student import StudentModel


class Students(Resource):
	def get(self):
		return {'students': [student.json() for student in StudentModel.query.all()]}

class Student(Resource):

	st_arg = reqparse.RequestParser()
	st_arg.add_argument('name')
	st_arg.add_argument('intra_id')
	# st_arg.add_argument('projects')

	def find_student(id):
		for student in students:
			if student['id'] == id:
				return student
		return None

	def get(self, id):
		student_found = StudentModel.find_student(id)
		if student_found:
			return student_found.json(), 200
		return {'messsage': 'Student Not found'}, 404

	def post(self, id):
		if StudentModel.find_student(id):
			return {'messsage': 'Student alredy exists.'}, 401
		data = Student.st_arg.parse_args()
		new_student =  StudentModel(id, **data)
		try:
			new_student.save_student()
		except:
			return {'message': 'An internal error ocurred trying to save student.'}, 500
		return  new_student.json(), 201

	def put(self, id):
		data = Student.st_arg.parse_args()
		student_found = StudentModel.find_student(id)
		if student_found:
			student_found.update_student(**data)
			try:
				student_found.save_student()
			except:
				return {'message': 'An internal error ocurred trying to save student.'}, 500
			return  student_found.json(), 200
		new_student = { 'id': id, **data }
		try:
			student_found.save_student()
		except:
			return {'message': 'An internal error ocurred trying to save student.'}, 500
		return new_student.json(), 201

	def delete(self, id):
		student_found = StudentModel.find_student(id)
		if student_found:
			try:
				student_found.delete_student()
			except:
				return {'message': 'An internal error ocurred trying to save student.'}, 500
			return {'message': 'student deleted.'}
		return {'message': 'student not found.'}, 404
