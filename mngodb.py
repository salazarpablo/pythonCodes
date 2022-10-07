from flask import Flask, request, json, Response
from pymongo import MongoClient

# initialized the Flask APP
app = Flask(__name__)

class CrudAPI:  # MongoDB Model for ToDo CRUD Implementation
    def __init__(self, data):   # Fetchs the MongoDB, by making use of Request Body
        self.client = MongoClient("mongodb://localhost:27017/")
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def insert_data(self, data):    # Create - (1) explained in next section
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def read(self):                 # Read - (2) explained in next section
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def update_data(self):          # Update - (3) explained in next section
        filter = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filter, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete_data(self, data):    # Delete - (4) explained in next section
        filter = data['Filter']
        response = self.collection.delete_one(filter)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output

# Achieving CRUD through API - '/crudapi'
@app.route('/crudapi', methods=['GET'])     # Read MongoDB Document, through API and METHOD - GET
def read_data():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    read_obj = CrudAPI(data)
    response = read_obj.read()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/crudapi', methods=['POST'])    # Create MongoDB Document, through API and METHOD - POST
def create():
    data = request.json
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    create_obj = CrudAPI(data)
    response = create_obj.insert_data(data)
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')

@app.route('/crudapi', methods=['PUT'])     # Update MongoDB Document, through API and METHOD - PUT
def update():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    update_obj = CrudAPI(data)
    response = update_obj.update_data()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/crudapi', methods=['DELETE'])   # Delete MongoDB Document, through API and METHOD - DELETE
def delete():
    data = request.json
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    delete_obj = CrudAPI(data)
    response = delete_obj.delete_data(data)
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
