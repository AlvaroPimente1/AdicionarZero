import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os

def adicionar_numero():
    arquivo_selecionado = filedialog.askopenfilename()
    if arquivo_selecionado:
        try:
            with open(arquivo_selecionado, 'r+') as arquivo:
                linhas = arquivo.readlines()
                arquivo.seek(0)
                for linha in linhas:
                    if linha.strip():
                        nova_linha = "000" + linha
                        arquivo.write(nova_linha)
                    else:
                        continue
                arquivo.truncate()
        except Exception as e:
            messagebox.showerror("Erro ao escrever no arquivo", str(e))

try:
    janela = tk.Tk()
    label = tk.Label(janela, text="Suba o arquivo e feche o programa para atualizar")
    label.pack()
    botao_upload = tk.Button(janela, text="upload arquivo", width=15, font=("Arial", 12), bg="grey", fg="white", command=adicionar_numero)
    botao_upload.pack(pady=10)

    janela.mainloop()
except Exception as e:
    messagebox.showerror("Erro", str(e))
