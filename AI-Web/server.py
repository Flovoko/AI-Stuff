from flask import Flask, jsonify, render_template, request
from markupsafe import escape
import openai

msg = []

with open('secret.key', 'r') as secret_key:
    secret_key = secret_key.read()

openai.api_key = secret_key

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call_gpt')
def call_gpt():
    arg = request.args.get('arg', '')
    msg.append({"role": "user", "content": arg})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )

    new_span = escape(f'{completion.choices[0].message.content}')
    return jsonify({'element': str(new_span)})

if __name__ == '__main__':
    app.run(debug=True)