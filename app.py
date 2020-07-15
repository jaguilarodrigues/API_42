from flask import Flask
from flask_restful import Api
from resources.students import Students, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db' #pode modificar para qualquer outro banco
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def creat_base():
	base.create_all()

api.add_resource(Students, '/students')
api.add_resource(Student, '/students/<int:id>')

if __name__ == '__main__':
	from sql_alchemy import base #importação feita apenas na chamada de app
	base.init_app(app)
	app.run(debug=True)
