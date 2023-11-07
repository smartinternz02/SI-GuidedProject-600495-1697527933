# Flask app code (app.py)
from flask import Flask, request, render_template, jsonify
from keras.models import load_model
model = load_model('model.h5')
app = Flask(__name__)

# Defining make_prediction function
def make_prediction(age, physical_score):
    input_data = [[age, physical_score]]
    prediction = model.predict(input_data)
    return int(prediction[0][0])  # Convert prediction to an integer

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = request.form
        age = float(data['age'])
        physical_score = float(data['physical_score'])
        prediction = make_prediction(age, physical_score)
        return render_template('predict.html', prediction=prediction, age=age, physical_score=physical_score)

    return render_template('predict.html')


@app.route('/feedback', methods=['GET'])
def feedback_form():
    return render_template('feedback.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        feedback = request.form.get('feedback')

        return "Feedback submitted successfully."

if __name__ == '__main__':
    app.run(debug=True)


