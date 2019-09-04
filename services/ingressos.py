from flask import jsonify

class IngressoService:

    def getAll(dbObject):
        jsonArray = []
        for ingresso in dbObject.find({}, {'_id': 0}).sort("id"):
            jsonArray.append(ingresso) 
        return jsonify(jsonArray)

    def getOne(dbObject, id):
        ingresso = dbObject.find_one({"id": id}, {"_id": 0})
        if ingresso:
            return jsonify(ingresso)
        else:
            return {}

    def insert(dbObject, request):
        ingresso_id = dbObject.insert(request.json)
        new_ingresso = dbObject.find_one({"_id": ingresso_id}, {"_id": 0})
        return jsonify(new_ingresso)
    
    def update(dbObject, request, id):
        new_ingresso = {"$set": request.json}
        dbObject.update_one({"id": id}, new_ingresso)
        ingresso = dbObject.find_one({"id": id}, {"_id": 0})
        return jsonify(ingresso)

    def delete(dbObject, id):
        dbObject.delete_one({"id": id})
        return jsonify({"result": "Deleted"})