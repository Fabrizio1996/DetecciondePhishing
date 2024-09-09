from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Cargar el modelo y el vectorizador entrenado
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        # Vectorizar la URL
        url_vectorized = vectorizer.transform([url])
        # Realizar la predicción
        prediction = model.predict(url_vectorized)
        result = 'Phishing' if prediction[0] == 1 else 'Not Phishing'
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)

