#fazer botão tela cheia
#self.root.attributes('-fullscreen', True)

#criar botão de reste, ainda não sei onde
#self.bt_reset = Button(self.frame_1, text="Reset")
#self.bt_reset.place(relx=, rely=, relwidth=, relheight=)

from modulos import *
from placeHolder import EntPlaceHold

class Application():
    def __init__(self, root:'Tk'):
        self.root = root
        self.window()
        root.mainloop()

    def window(self):
        self.root.title("Calculadora de Momento de Inercia")
        self.root.configure(background= Color.dark_blue.value)
        self.root.geometry("950x520")
        self.root.minsize(width=950, height=520)
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
        
        self.widgets_frame1()

        self.frame_2 = Frame(
            self.root, 
            bd=4, 
            bg=Color.gray.value, 
            highlightbackground= Color.light_gray.value, 
            highlightthickness= 4
            )
        self.frame_2.place(relx=0.465, rely=0.12, relwidth=0.52, relheight=0.855)

        self.frame_3 = Frame(
            self.root, 
            bd=4, 
            bg=Color.gray.value, 
            highlightbackground= Color.light_gray.value, 
            highlightthickness= 4
            )
        self.frame_3.place(relx=0.015, rely=0.025, relwidth=0.97, relheight=0.1)

        self.widgets_frame3()

    def widgets_frame1(self):
        self.bt_calc = Button(
            self.frame_1, 
            text="Calcular",
            font=('David', 10),
            bd= 0,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_calc.place(relx=0.79, rely=0.92, relwidth=0.2, relheight=0.07)
    
    def widgets_frame2(self):
        print("grafico")

    def widgets_frame3(self):
        self.bt_reset = Button(
            self.frame_3, 
            text="Redefinir tudo",
            font=('David', 10),
            bd= 0,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_reset.place(relx=0.88, rely=0.15, relwidth=0.11, relheight=0.8)
        
        self.bt_add = Button(
            self.frame_3, 
            text="Inserir Forma",
            font=('David', 10),
            bd= 0, 
            command=self.Insert_window,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_add.place(relx=0.01, rely=0.15, relwidth=0.11, relheight=0.8)

        self.bt_remove = Button(
            self.frame_3, 
            text="Remover Forma",
            font=('David', 10),
            bd= 0,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_remove.place(relx=0.13, rely=0.15, relwidth=0.12, relheight=0.8)
        
        self.bt_atualize = Button(
            self.frame_3, 
            text="Modificar Forma",
            font=('David', 10),
            bd= 0,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_atualize.place(relx=0.26, rely=0.15, relwidth=0.12, relheight=0.8)
    
    def Destroy_Insert_window(self):
        self.insert.destroy()
    
    def Insert_window(self):
        self.insert = Toplevel()
        self.insert.title("Inserir Forma Geométrica")
        self.insert.configure(background= Color.dark_blue.value)
        self.insert.geometry("300x500")
        self.insert.resizable(False, False)
        self.insert.transient(self.root)
        self.insert.focus_force()
        self.insert.grab_set()

        self.frame_insert = Frame(
            self.insert, 
            bd=4, bg=Color.gray.value,
            highlightbackground= Color.light_gray.value, 
            highlightthickness= 4
            )
        self.frame_insert.place(relx=0.024, rely=0.025, relwidth=0.95, relheight=0.95)

        #------geometric form--------
        self.label_geometric_form = Label(
            self.frame_insert, 
            text="Selecionar forma geométrica", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_geometric_form.place(relx=0.005, rely=0.01)

        self.geometric_form_entry = Entry(self.frame_insert)
        self.geometric_form_entry.place(relx=0.005, rely=0.045, relwidth=0.95, relheight=0.05)

        #--------centroid coordinates---------
        self.label_coordinates_center = Label(
            self.frame_insert, 
            text="Coordenada do centróide", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_coordinates_center.place(relx=0.005, rely=0.13)

        self.coordinate_center_x_entry = EntPlaceHold(self.frame_insert, 'x:')
        self.coordinate_center_x_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)

        self.coordinate_center_y_entry = EntPlaceHold(self.frame_insert, 'y:')
        self.coordinate_center_y_entry.place(relx=0.005, rely=0.23, relwidth=0.95, relheight=0.05)

        #-----------dimensions------------
        self.label_dimensions = Label(
            self.frame_insert, 
            text="Dimensões", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_dimensions.place(relx=0.005, rely=0.3)

        self.dimensions_a_entry = Entry(self.frame_insert)
        self.dimensions_a_entry.place(relx=0.005, rely=0.34, relwidth=0.95, relheight=0.05)

        self.dimensions_b_entry = Entry(self.frame_insert)
        self.dimensions_b_entry.place(relx=0.005, rely=0.4, relwidth=0.95, relheight=0.05)  

        self.dimensions_c_entry = Entry(self.frame_insert)
        self.dimensions_c_entry.place(relx=0.005, rely=0.46, relwidth=0.95, relheight=0.05)

            #-----------sub-are--------------
        self.label_subare = Label(
            self.frame_insert, 
            text="Subárea adicionada", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_subare.place(relx=0.005, rely=0.535)

        self.subare_entry = Entry(self.frame_insert)
        self.subare_entry.place(relx=0.005, rely=0.575, relwidth=0.95, relheight=0.05)

        #--------coordinates--------------
        self.label_coordinates = Label(
            self.frame_insert, 
            text="Coordenada do centróide", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_coordinates.place(relx=0.005, rely=0.65)

        self.coordinate_x_entry = Entry(self.frame_insert)
        self.coordinate_x_entry.place(relx=0.005, rely=0.69, relwidth=0.95, relheight=0.05)

        self.coordinate_y_entry = Entry(self.frame_insert)
        self.coordinate_y_entry.place(relx=0.005, rely=0.75, relwidth=0.95, relheight=0.05)

        #======Buttons===========
        self.bt_acept = Button(
            self.frame_insert, 
            text="Inserir",
            font=('David', 10),
            bd= 0,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_acept.place(relx=0.2, rely=0.9, relwidth=0.25, relheight=0.08)

        self.bt_quit = Button(
            self.frame_insert, 
            text="Cancelar",
            font=('David', 10),
            bd= 0,
            command= self.Destroy_Insert_window,
            activebackground= Color.white.value,
            activeforeground= Color.black.value,
            bg= Color.gray.value,
            fg= Color.white.value
            )
        self.bt_quit.place(relx=0.55, rely=0.9, relwidth=0.25, relheight=0.08)


root = Tk()
Application(root)
