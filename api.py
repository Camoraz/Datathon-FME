from flask import Flask, request, jsonify
from flask_cors import CORS
from format_data import FormData


app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # Permite solo desde React

@app.route('/api', methods=['POST'])
def api_endpoint():
    data = request.get_json()
    
    response = FormData(data['years'], data['role'], data['challenge'], data['lang'], data['level'], data['age'], data['hackathons'])

    

    response = f'years: {data['years']}, role: {data['role']}, challenge: {data['challenge']}, lang: {data['lang']}, level: {data['level']}, age: {data['age']}, hackathons: {data['hackathons']}'

    return jsonify({"message": "Received", "data": response})

if __name__ == '__main__':
    app.run(debug=True)
