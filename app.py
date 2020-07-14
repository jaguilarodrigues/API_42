from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

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

api.add_resource(Students, '/students')

if __name__ == '__main__':
	app.run(debug=True)
