from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from chatbot import ask_ai
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
model = load_model('disease_model.h5')
labels = open('labels.txt').read().splitlines()
def predict_disease(img_path):
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0
prediction = model.predict(img_array)
index = np.argmax(prediction)
confidence = float(np.max(prediction)) * 100
return labels[index], round(confidence, 2)
@app.route('/')
def home():
return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
if 'file' not in request.files:
return jsonify({'error': 'No file uploaded'})
file = request.files['file']
filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
file.save(filepath)
disease, confidence = predict_disease(filepath)
return jsonify({
'disease': disease,
'confidence': confidence
})
@app.route('/chat', methods=['POST'])
def chat():
user_message = request.json['message']
response = ask_ai(user_message)
return jsonify({'reply': response})
if __name__ == '__main__':
app.run(debug=True)
