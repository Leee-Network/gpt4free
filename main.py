from flask import Flask, request, jsonify
import g4f

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    messages = data.get('messages', [])
    chat = g4f.ChatCompletion.create(model='gpt-4', provider=g4f.Provider.Bing, messages=messages, stream=False)
    return chat

if __name__ == '__main__':
    app.run()
