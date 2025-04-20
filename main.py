#fazer botão tela cheia
#self.root.attributes('-fullscreen', True)

from tkinter import *

from Formas import Retangulo
from Formas import Ponto2D

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.window()
        root.mainloop()

    def window(self):
        self.root.title("Calculadora de Momento de Inercia")
        self.root.configure(background='#5e5c64')
        self.root.geometry("700x500")
        self.root.resizable(True,True)

Application()
