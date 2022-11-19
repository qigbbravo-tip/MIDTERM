from flask import Flask, jsonify, request
app = Flask(__name__)

heartid = [
    {
        "Patient_Name" :["Marcus Howard"]
        "heart_id" : "1",
        "date" : ["11-19-22"],
        "heart_rate" : [ "110"]
    },
    {
        "Patient_Name" :["Iyanne Corpuz"]
        "heart_id" : "2",
        "date" : ["11-18-22"],
        "heart_rate" : [ "100"]
    }
]
@app.route ('/hearts', methods=['GET'])
def getHearts():
    return jsonify(heartid)
@app.route('/hearts', methods=['POST'])
def addheart():
    hearts = request.get_json()
    heartid.append(hearts)
    return {'id': len(heartid)},200

@app.route('/hearts/<int:index>', methods=['DELETE'])
def deleteHeart(index):
    heartid.pop(index)
    return ' The heart ID was successfully deleted' , 200

if __name__ ==  '__main__':
    app.run()