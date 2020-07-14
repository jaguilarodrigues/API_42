from flask import Flask
from flask_restful import Api
from resources.students import Students, Student

app = Flask(__name__)
api = Api(app)

api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)
