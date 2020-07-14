from flask_restful import Resource, reqparse

students = [
    {
        'id': 1,
        'name': "Gustavo Belfort",
        'intra_id': "gus",
        'projects': [
            "42cursus_libft",
            "42cursus_get-next-line",
            "42cursus_ft-printf",
        ]
    },
    {
        'id': 2,
        'name': "Guilhemar Caixeta",
        'intra_id': "guiga",
        'projects': [
            "cub3d",
        ]
    }
]

class Students(Resource):
	def get(self):
		return students

class Student(Resource):

	st_arg = reqparse.RequestParser()
	st_arg.add_argument('name')
	st_arg.add_argument('intra_id')
	# st_arg.add_argument('projects')


	def get(self, id):
		for student in students:
			if student['id'] == id:
				return student
		return {'messsage': 'Student Not found'}, 404

	def post(self, id):
		data = Student.st_arg.parse_args()

		new_student = {'id':id, **data}

		students.append(new_student)
		return new_student, 201

	
