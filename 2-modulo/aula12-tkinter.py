import tkinter as tk

#1 Criando a janela
window = tk.Tk()
window.geometry = ("300x150")
window.title("Gerenciador de Frases")

#2 Adicionando o Frame
frame = tk.Frame()
frame.pack(padx=10, pady=10, fill='x', expand=True)

#Adicionando o lable
label = tk.Label(frame, text="Hello world")
label.pack(fill='x', expand=True)

#4 Adicionando o input text
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frase_lab)
frase_inp.pack(fill='x', expand=True)

#5 Função para alterar o label
def click():
    label.config(text=frase_inp.get())

#6 Adicionando botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


window.mainloop()
