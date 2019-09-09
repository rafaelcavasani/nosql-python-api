from flask import jsonify

class IngressoService:

    def getAll(dbObject):
        jsonArray = []
        for ingresso in dbObject.find({}, {'_id': 0}).sort("id_ingresso"):
            jsonArray.append(ingresso) 
        return jsonify(jsonArray)

    def getOne(dbObject, id_ingresso):
        ingresso = dbObject.find_one({"id_ingresso": id_ingresso}, {"_id": 0})
        if ingresso:
            return jsonify(ingresso)
        else:
            return {}

    def insert(dbObject, request):
        ingresso_id = dbObject.insert(request.json)
        new_ingresso = dbObject.find_one({"_id": ingresso_id}, {"_id": 0})
        return jsonify(new_ingresso)
    
    def update(dbObject, request, id_ingresso):
        new_ingresso = {"$set": request.json}
        dbObject.update_one({"id_ingresso": id_ingresso}, new_ingresso)
        ingresso = dbObject.find_one({"id_ingresso": id_ingresso}, {"_id": 0})
        return jsonify(ingresso)

    def delete(dbObject, id_ingresso):
        dbObject.delete_one({"id_ingresso": id_ingresso})
        return jsonify({"result": "Deleted"})