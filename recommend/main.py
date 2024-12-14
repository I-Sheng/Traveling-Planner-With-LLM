from flask import Flask, request, jsonify
from recommended_module import main

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend_site():
    data = request.get_json()
    day = data.get("day", 0)
    preference = data.get('preference', '')
    result = main(day, preference)
    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


