import tkinter as tk
import openai

dark_mode = True

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

root = tk.Tk()
root.title("Chat")

input_field = tk.Entry(root)
messages = tk.Text(root)

input_field.pack()
messages.pack()

def send_message(event=None):
  message = input_field.get()
  answer = questions(message)
  print("[LOG], [INPUT] ", message)
  print("[LOG], [OUTPUT] ", answer)

  messages.insert(tk.END, answer)
  
  input_field.delete(0, tk.END)

root.bind("<Return>", send_message)

input_field.config(font=("Arial", 14))
messages.config(font=("Arial", 14))
input_field.config(bg="#eee")
input_field.config(bd=1, relief=tk.SUNKEN)
messages.config(bg="#eee")
messages.config(bd=1, relief=tk.SUNKEN)
input_field.config(fg="#333")
messages.config(bg="#fff")
messages.config(fg="#333")

def toggle_dark_mode():
  global dark_mode
  dark_mode = not dark_mode

  if dark_mode:
    root.config(bg="#333")
    input_field.config(bg="#333", fg="#fff")
    messages.config(bg="#333", fg="#fff")
    dark_mode_button.config(bg="#333", fg="#fff")
  else:
    root.config(bg="#fff")
    input_field.config(bg="#eee", fg="#333")
    messages.config(bg="#eee", fg="#333")
    dark_mode_button.config(bg="#eee", fg="#333")

dark_mode_button = tk.Button(root, text="Dunkelmodus", command=toggle_dark_mode)
dark_mode_button.pack()

root.mainloop()