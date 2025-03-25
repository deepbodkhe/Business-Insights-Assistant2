from flask import Flask, render_template, request, jsonify
from app.core import BusinessInsightsEngine
import os

app = Flask(__name__, template_folder=os.path.abspath('app/templates'))
engine = BusinessInsightsEngine()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        query = request.json.get('query', '').strip()
        if not query:
            return jsonify({"error": "Empty query"}), 400
            
        response = engine.process_query(query)
        return jsonify({"response": response})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)