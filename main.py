import tkinter as tk

from Formas import Retangulo
from Formas import Ponto2D


janela = tk.Tk()
janela.title("Minha Janela Tkinter")
janela.geometry("300x100+20+20")

msg = tk.Label(janela, text="test")
msg.pack()
janela.mainloop()

retangulo = Retangulo()