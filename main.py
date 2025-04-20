#fazer botão tela cheia
#self.root.attributes('-fullscreen', True)

#cinza '#5e5c64'

from tkinter import *
from enum import Enum

from Formas import Retangulo
from Formas import Ponto2D

class Color(Enum):
    gray = "#5e5c64"
    dark_blue = "#18304a"

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.window()
        self.window_frame()
        root.mainloop()

    def window(self):
        self.root.title("Calculadora de Momento de Inercia")
        self.root.configure(background= Color.dark_blue.value)
        self.root.geometry("950x520")
        self.root.minsize(width=700, height=500)
        self.root.resizable(True,True)

    def window_frame(self):
        self.main_frame = Frame(self.root)
        self.main_frame.place(relx=0.1, rely=0.1, relwidth=0.5, relheight=0.9)
        self.main_frame.configure(background= Color.gray.value)

Application()
