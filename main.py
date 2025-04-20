#fazer botão tela cheia
#self.root.attributes('-fullscreen', True)

#cinza '#5e5c64'

from tkinter import *
from enum import Enum

from Formas import Retangulo
from Formas import Ponto2D

class Color(Enum):
    gray = "#5e5c64"
    light_gray = "#868687"
    dark_blue = "#18304a"

class Application():
    def __init__(self, root:'Tk'):
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
        self.frame_1 = Frame(self.root, bd=4, bg=Color.gray.value,
        highlightbackground= Color.light_gray.value, highlightthickness= 4)
        self.frame_1.place(relx=0.015, rely=0.025, relwidth=0.45, relheight=0.95)
        
        self.frame_2 = Frame(self.root, bd=4, bg=Color.gray.value, 
        highlightbackground= Color.light_gray.value, highlightthickness= 4)
        self.frame_2.place(relx=0.485, rely=0.025, relwidth=0.5, relheight=0.95)


root = Tk()
Application(root)
