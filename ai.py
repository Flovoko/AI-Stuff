import openai
import os

os.system('cls')

with open('secret.key', 'r') as secret_key:
    secret_key = secret_key.read()

def questions(question):
    result = openai.Completion.create(
        model='text-davinci-003',
        prompt=question,
        max_tokens=2048,
        api_key=secret_key
    )
    answer = result.choices[0].text
    return answer

if __name__ == '__main__':
    while(question := input('\x1b[1;32m' + '> ' + '\x1b[1;32m')) != 'X':
        answer = questions(question)
        print('\x1b[1;34m' + answer + '\x1b[1;34m')