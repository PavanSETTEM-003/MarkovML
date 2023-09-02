from flask import Flask, render_template, request, jsonify
# from utils import model_predictions
from preprocess import preprocess_text

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/test.html', methods=['GET'])
def test():
    return render_template("test_page.html")

@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # Extract answers from the form
        answer1 = preprocess_text( request.form['answer1'].lower() )
        answer2 = preprocess_text( request.form['answer2'].lower() )
        answer3 = preprocess_text( request.form['answer3'].lower() )
        # Convert answers into a list

        answers_list = [answer1, answer2, answer3]
        # print(answers_list)

        # # Perform sentiment classification
        # classification_output = model_predictions(answers_list)
        # print(classification_output)

        # # Return the classification result as JSON
        # return jsonify({"classification": classification_output})

    return render_template('test_page.html')

if __name__ == '__main__':
    app.run(debug=True)
