from flask import Flask, jsonify, request
from flask_cors import CORS

from model import run_experiments

app = Flask(__name__)
CORS(app)

@app.route("/trigger_model", methods=["POST"])
def home():
    try:
        parameters = {}
        #{'model_name': 'testing #3', 'Epochs': '1', 'Batch_size': '32', 'optimizer_name': 'adam', 'Loss': 'Categorical cross-entropy'}
    
        for key in request.form:
            parameters[key] = request.form[key]
            
        conclusion, comments = run_experiments(parameters)
        if(conclusion):
            print(comments)
            return { "status": "True"}
        
        else:
            print("failed bro")
            print(comments)
            return { "status": "False"}

    except Exception as error:
        print(error)
    
        return { "status": "False"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
