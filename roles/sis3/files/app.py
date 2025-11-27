from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/flights')
def flights():
    return jsonify([
        {"from": "ALA", "to": "AST", "price": 20000},
        {"from": "ALA", "to": "MOW", "price": 85000}
    ])

app.run(host="0.0.0.0", port=5000)
