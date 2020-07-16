from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId

app = Flask(__name__)

app.secret_key = "secretkey"

app.config['MONGO_DBNAME'] = 'SelectionProcess'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/SelectionProcess'

mongo = PyMongo(app)

@app.route('/students')
def students():
	if "projects" in request.args:
		project = request.args['projects']
		student_fil = mongo.db.student.find({'projects': project})
		resp = dumps(student_fil)
		return resp
	students = mongo.db.student.find()
	resp = dumps(students)
	return resp


@app.route('/students/<id>')
def student(id):
	student = mongo.db.student.find_one({'_id': ObjectId(id)})
	resp = dumps(student)
	return resp

@app.route('/students', methods=['POST'])
def add_student():
	_json = request.json
	_name = _json['name']
	_intra_id = _json['intra_id']
	_projects = _json['projects']

	id = mongo.db.student.insert_one({'name':_name, 'intra_id': _intra_id, 'projects': _projects}).inserted_id
	student = mongo.db.student.find_one({'_id': id})
	resp = dumps(student)

	return resp, 201

@app.route('/students/:<id>', methods=['DELETE'])
def del_student(id):
	mongo.db.student.delete_one({'_id': ObjectId(id)})
	student = mongo.db.student.find_one({'_id': id})
	if not student:
		resp = dumps({})
	return resp

@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
	_id = id
	_json = request.json
	_name = _json['name']
	_intra_id = _json['intra_id']
	_projects = _json['projects']

	mongo.db.student.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'name': _name, 'intra_id': _intra_id, 'projects': _projects}})
	resp = jsonify('Student updated successfully!')
	resp.status_code = 200
	return resp

if __name__ == "__main__":
	# app.run(host='0.0.0.0', port=3000)
	app.run(debug=True)
