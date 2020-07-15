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

	id = mongo.db.student.insert_one({'name':_name, 'intra_id': _intra_id, 'projects': _projects})

	resp = jsonify("Student create sucessfuly")
	resp.status_code = 201

	return resp

@app.route('/students/<id>', methods=['DELETE'])
def del_student(id):
	mongo.db.student.delete_one({'_id': ObjectId(id)})
	resp = jsonify("Student deleted sucessfuly")
	resp.status_code = 200
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
	app.run(debug=True)
