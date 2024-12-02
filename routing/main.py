from flask import Flask, request, jsonify
from distance_matrix import travel_time
from routing import main

app = Flask(__name__)

@app.route('/routing', methods=['POST'])
def routing_path():
    data = request.get_json()
    day:int = data.get("day", 1)
    sites:str = data.get("sites", '')
    result = main(day, sites)
    return jsonify({'result': result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
