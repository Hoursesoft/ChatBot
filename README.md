# ChatBotNPL - Procesamiento de Lenguaje Natural Chatbot

## Descripción
Este código implementa un chatbot basado en procesamiento de lenguaje natural (NLP) utilizando la biblioteca NLTK (Natural Language Toolkit) y scikit-learn. El chatbot se entrena con datos almacenados en un archivo JSON que contiene preguntas y respuestas. El modelo de clasificación utilizado es un pipeline que combina el vectorizador TF-IDF (Term Frequency-Inverse Document Frequency) con un clasificador de máquinas de soporte vectorial (LinearSVC).

## Requisitos
- Python 3.x
- NLTK
- scikit-learn

## Instalación
1. Asegúrate de tener Python 3.x instalado en tu sistema.
2. Instala las bibliotecas necesarias ejecutando el siguiente comando en tu terminal:
   ```bash
   pip install nltk scikit-learn
Descarga los recursos adicionales de NLTK ejecutando el siguiente código en tu entorno Python:
python
Copy code
import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
Uso
Coloca el archivo JSON con los datos de entrenamiento en la ruta 'ChatBotNPL/braind/archivo.json'.
Ejecuta el código proporcionado.
El modelo se entrenará automáticamente y mostrará la precisión alcanzada en el conjunto de prueba.
Luego, puedes interactuar con el chatbot utilizando la función ask(ask) pasando tu pregunta como argumento.
Ejemplo de Uso
python
Copy code
import json
from tu_modulo import ask

# Realiza una pregunta al chatbot
pregunta_usuario = "¿Cuál es la capital de Francia?"
respuesta_chatbot = ask(pregunta_usuario)

# Imprime la respuesta del chatbot
print(respuesta_chatbot)
Notas Adicionales
Asegúrate de proporcionar datos de entrenamiento relevantes y variados para mejorar la precisión del modelo.
Puedes ajustar los parámetros del vectorizador y el clasificador en el pipeline para optimizar el rendimiento según tus necesidades.
Este proyecto es un punto de partida para desarrollar chatbots basados en NLP y puede ser ampliado y personalizado según los requisitos específicos del usuario. ¡Disfruta interactuando con tu chatbot!