from crypt import methods
from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb+srv://admin:admin@cluster0.oy3jqmv.mongodb.net/test'

mongo = PyMongo(app)


@app.route('/mangas', methods=['POST'])
def create_mangas():
    nombre = request.json['nombre']
    autor = request.json['autor']
    volumenes = request.json['volumenes']
    if nombre and autor and volumenes:
        id = mongo.db.mangas.insert_one({
            'nombre': nombre, 'autor': autor, 'volumenes': volumenes
        }
        ).inserted_id
        response = jsonify({
            '_id': str(id),
            'nombre': nombre,
            'autor': autor,
            'volumenes': volumenes
        })
        response.status_code = 201
        return response
    else:
        return not_found()


@app.route('/mangas', methods=['GET'])
def get_mangas():
    mangas = mongo.db.mangas.find()
    response = json_util.dumps(mangas)
    return Response(response, mimetype="application/json;charset=UTF-8")


@app.route('/mangas/<id>', methods=['GET'])
def get_manga(id):
    print(id)
    manga = mongo.db.mangas.find_one({'_id': ObjectId(id), })
    response = json_util.dumps(manga)
    return Response(response, mimetype="application/json")


@app.route('/mangas/<id>', methods=['DELETE'])
def delete_manga(id):
    mongo.db.mangas.delete_one({'_id': ObjectId(id)})
    response = jsonify({'message': 'Manga ' + id + ' Borrado exitosamente'})
    response.status_code = 200
    return response


@app.route('/mangas/<_id>', methods=['PUT'])
def update_manga(_id):
    nombre = request.json['nombre']
    autor = request.json['autor']
    volumenes = request.json['volumenes']
    if nombre and autor and volumenes:
        mongo.db.mangas.update_one(
            {'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)}, {'$set': {'nombre': nombre, 'autor': autor, 'volumenes': volumenes}})
        response = jsonify({'message': 'Manga ' + _id +
                           ' Actualizado Satisfactoriamente'})
        response.status_code = 200
        return response
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return


if __name__ == "__main__":
    app.run(debug=True, port=5000)
