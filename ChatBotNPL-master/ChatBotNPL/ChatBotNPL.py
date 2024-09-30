import json
import nltk
from nltk.corpus import wordnet as wn
from nltk.metrics import edit_distance
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def ask(ask):
    # Leer el archivo JSON
    with open('ChatBotNPL/braind/archivo.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Preparar los datos
    X = [item['question'] for item in data]
    y = [item['answer'] for item in data]

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear un pipeline con TfidfVectorizer y LinearSVC
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])

    # Entrenar el modelo
    pipeline.fit(X_train, y_train)

    # Hacer predicciones en el conjunto de prueba
    predictions = pipeline.predict(X_test)

    # Calcular la precisión del modelo
    accuracy = accuracy_score(y_test, predictions)
    print(f'Accuracy: {accuracy}')

    predicted_answer = pipeline.predict([ask])

    return predicted_answer[0]
