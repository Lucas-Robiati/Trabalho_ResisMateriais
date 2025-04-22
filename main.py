#fazer botão tela cheia
#self.root.attributes('-fullscreen', True)

#criar botão de reste, ainda não sei onde
#self.bt_reset = Button(self.frame_1, text="Reset")
#self.bt_reset.place(relx=, rely=, relwidth=, relheight=)

from tkinter import *
from enum import Enum

from Formas import Retangulo
from Formas import Ponto2D

class Color(Enum):
    gray = "#5e5c64"
    light_gray = "#868687"
    dark_blue = "#18304a"
    white = "#e8e8ed"

class Application():
    def __init__(self, root:'Tk'):
        self.root = root
        self.window()
        root.mainloop()

    def window(self):
        self.root.title("Calculadora de Momento de Inercia")
        self.root.configure(background= Color.dark_blue.value)
        self.root.geometry("950x520")
        self.root.minsize(width=700, height=500)
        self.root.resizable(True,True)
        self.window_frame()

    def window_frame(self):
        self.frame_1 = Frame(
            self.root, 
            bd=4, bg=Color.gray.value,
            highlightbackground= Color.light_gray.value, 
            highlightthickness= 4
            )
        self.frame_1.place(relx=0.015, rely=0.025, relwidth=0.45, relheight=0.95)
        
        self.frame_2 = Frame(
            self.root, 
            bd=4, 
            bg=Color.gray.value, 
            highlightbackground= Color.light_gray.value, 
            highlightthickness= 4
            )
        self.frame_2.place(relx=0.485, rely=0.025, relwidth=0.5, relheight=0.95)

        self.widgets_frame1()

    def widgets_frame1(self):
        #------geometric form--------
        self.label_geometric_form = Label(
            self.frame_1, 
            text="Selecionar forma geométrica", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 12)
            )
        self.label_geometric_form.place(relx=0.005, rely=0.01)

        self.geometric_form_entry = Entry(self.frame_1)
        self.geometric_form_entry.place(relx=0.005, rely=0.045, relwidth=0.5, relheight=0.05)
        
        #--------centroid coordinates---------
        self.label_coordinates_center = Label(
            self.frame_1, 
            text="Coordenada do centróide", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 12)
            )
        self.label_coordinates_center.place(relx=0.005, rely=0.13)

        self.coordinate_center_x_entry = Entry(self.frame_1)
        self.coordinate_center_x_entry.place(relx=0.005, rely=0.17, relwidth=0.5, relheight=0.05)

        self.coordinate_center_y_entry = Entry(self.frame_1)
        self.coordinate_center_y_entry.place(relx=0.005, rely=0.23, relwidth=0.5, relheight=0.05)

        #-----------dimensions------------
        self.label_dimensions = Label(
            self.frame_1, 
            text="Dimensões", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 12)
            )
        self.label_dimensions.place(relx=0.005, rely=0.3)

        self.dimensions_a_entry = Entry(self.frame_1)
        self.dimensions_a_entry.place(relx=0.005, rely=0.35, relwidth=0.5, relheight=0.05)

        self.dimensions_b_entry = Entry(self.frame_1)
        self.dimensions_b_entry.place(relx=0.005, rely=0.4, relwidth=0.5, relheight=0.05)  

        self.dimensions_c_entry = Entry(self.frame_1)
        self.dimensions_c_entry.place(relx=0.005, rely=0.45, relwidth=0.5, relheight=0.05)

        #-----------sub-are--------------
        self.label_subare = Label(
            self.frame_1, 
            text="Subárea adicionada", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 12)
            )
        self.label_subare.place(relx=0.005, rely=0.55)

        self.subare_entry = Entry(self.frame_1)
        self.subare_entry.place(relx=0.005, rely=0.6, relwidth=0.5, relheight=0.05)

        #--------coordinates--------------
        self.label_coordinates = Label(
            self.frame_1, 
            text="Coordenada do centróide", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 12)
            )
        self.label_coordinates.place(relx=0.005, rely=0.75)

        self.coordinate_x_entry = Entry(self.frame_1)
        self.coordinate_x_entry.place(relx=0.005, rely=0.82, relwidth=0.5, relheight=0.05)

        self.coordinate_y_entry = Entry(self.frame_1)
        self.coordinate_y_entry.place(relx=0.005, rely=0.86, relwidth=0.5, relheight=0.05)

root = Tk()
Application(root)


ret = Retangulo(1, 1)