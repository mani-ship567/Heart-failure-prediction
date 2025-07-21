from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        prediction = model.predict([np.array(features)])
        output = 'Yes 😞' if prediction[0] == 1 else 'No 😊'
        return render_template('index.html', prediction_text=f'Death Event Predicted: {output}')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
