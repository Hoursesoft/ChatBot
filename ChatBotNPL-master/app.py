from flask import Flask, render_template, request, jsonify
from ChatBotNPL import ask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/bot', methods=['POST'])
def bot_response():
    user_message = request.form.get('user_message')

    bot_response = ask(user_message)
    
    return jsonify({'bot_response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
