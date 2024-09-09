import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Cargar datos
data = pd.read_csv('phishing_data.csv')  # Asegúrate de tener este archivo
X = data['url']
y = data['label']

# Preprocesar datos
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = MultinomialNB()
model.fit(X_train, y_train)

# Guardar modelo y vectorizador
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
with open('vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)
