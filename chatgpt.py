import os
import openai

os.system('cls')

msg = []

with open('secret.key', 'r') as secret_key:
    secret_key = secret_key.read()

openai.api_key = secret_key

while True:
    msg_tmp = input('\x1b[1;32m' + 'DU > ' + '\x1b[1;32m')
    msg.append({"role": "user", "content": msg_tmp})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=msg
    )

    print('\x1b[1;34m\n' + "KI > " + completion.choices[0].message.content + '\x1b[1;34m\n')