from flask import Flask, jsonify, request
from flasgger import Swagger
from flasgger import swag_from
import api_doc_specs.specs as const
import json
from shMongoDBLogic import ShMongoDBLogic as db

app = Flask(__name__)
swagger = Swagger(app)
# driver = ShMongoDBLogic.get_connection()

@app.route('/getUser/<user_email>/')
@swag_from(const.user_dict, methods=['GET'])
def getUser(user_email):
    """endpoint returning user information
    ---
 
    """
    result = db.getUserByEmail(user_email)
    del result["_id"] 
    print(result)
    pprint(result)
    return jsonify(result)

@app.route('/addUser', methods = ['PUT'])
@swag_from(const.products)
def productsPost():
    json = request.json
    pprint(json)
    if len(json) > 0:
        # {"Name":"Stephanie Miranda","Email":"smirand6@asu.edu",
        #"Favorite_Color":"425caa","Superpower":"levitation",
        #"Field":"software engineering","Favorite_Hobby":"doodling"}
        result = db.addUser(json["Name"], json["Email"], json["Favorite_Color"], json["Superpower"], json["Field"], json["Favorite_Hobby"])
        return jsonify({"PUT" : result})
    return jsonify({"PUT" : "failed"})

def pprint(py_dict):
	print(json.dumps(py_dict, sort_keys=True,indent=4, separators=(',', ': ')))

pprint(const.user_dict)

app.run(debug=True)