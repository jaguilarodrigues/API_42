from flask import Flask
from flask_restful import Api
from resources.students import Students

app = Flask(__name__)
api = Api(app)

api.add_resource(Students, '/students')

if __name__ == '__main__':
	app.run(debug=True)
