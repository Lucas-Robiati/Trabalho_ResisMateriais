#https://www.youtube.com/watch?v=rtR5wHXPKZ4
#fazer botão tela cheia
#self.root.attributes('-fullscreen', True)

#criar botão de reste, ainda não sei onde
#self.bt_reset = Button(self.frame_1, text="Reset")
#self.bt_reset.place(relx=, rely=, relwidth=, relheight=)

from modulos import *
from tkinter import ttk
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
        root.protocol('WM_DELETE_WINDOW', self.destroy_window)  # Vincula o evento de fechamento
        self.window_frame()

    def destroy_window(self):
    # Função para tratar o fechamento da janela
        plt.close(self.fig)  # Fecha a figura do Matplotlib
        root.destroy()   # Destroi a janela do Tkinter

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

        self.widgets_frame2()

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

        self.label_table = Label(
            self.frame_1, 
            text="__________Tabela de Figuras__________", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_table.place(relx=0.25, rely=0.01, relwidth=0.5, relheight=0.25)

        #======table==============
        self.list_forms = ttk.Treeview(
            self.frame_1,
            height= 4,
            columns=("col1","col2","col3","col4")
            )
        self.list_forms.place(relx=0.01, rely=0.15, relwidth=0.95, relheight=0.4)
        
        self.scroobar = Scrollbar(self.frame_1, orient='vertical')
        self.list_forms.configure(yscroll=self.scroobar.set)
        self.scroobar.place(relx=0.96, rely=0.15, relwidth=0.04, relheight=0.4)

        self.list_forms.heading("#0", text="Forma")
        self.list_forms.heading("#1", text="X")
        self.list_forms.heading("#2", text="Y")
        self.list_forms.heading("#3", text="Aréa virtual")

        self.list_forms.column("#0", width=150, minwidth=150, anchor=CENTER)
        self.list_forms.column("#1", width=55,  minwidth=55, anchor=CENTER)
        self.list_forms.column("#2", width=55,  minwidth=55, anchor=CENTER)
        self.list_forms.column("#3", width=130,  minwidth=130, anchor=CENTER)

        #exemplo aceita interiros floats(2.5) variaveis (self.alguma_coisa) e strings
        #self.list_forms.insert(
        #    "", 
        #    END, 
        #    text="Triangulo", 
        #    values=(2.5, 3,"subtrair")
        #    ) 
        #lista de objetos a ser passada
        data = [ 
            ["Quadrado", 2, 4, "adicionar"],
            ["Triangulo", 2.5, 3, "subtrai"] 
            ]
        
        global count
        count=0
        for record in data:
            #if count % 2 == 0:
            self.list_forms.insert(parent='', index='end', iid=count, 
                text=record[0], values=(record[1],record[2],record[3])) 
            count += 1
        
        #=========style==============
        style_table = ttk.Style()#  Classe de configuração de estilo da tabela
        style_table.theme_use("clam")#  Tema da tabela
        style_table.configure(
            "Treeview", 
            background= Color.light_gray.value, 
            foreground= Color.black.value,
            fieldbackground= Color.gray.value,
            font=("Arial", 10))
        
        
        style_table.map("Treeview",
           background=[('selected', Color.light_blue.value)],
           foreground=[('selected', Color.white.value)])

        #style_table.tag_configure('oddrow', background= Color.gray.value)
        #style_table.tag_configure('evenrow', background= Color.light_gray.value)
    
    def widgets_frame2(self):
        xmin, xmax, ymin, ymax = -5, 5, -5, 5
        ticks_frequency = 1
        self.fig, self.ax = plt.subplots()
        self.fig.patch.set_facecolor('#ffffff')

        self.ax.set(xlim=(xmin-1, xmax+1), ylim=(ymin-1, ymax+1), aspect='equal')

        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')

        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        self.ax.set_xlabel('$x$', size=10, labelpad=-24, x=1.05)
        self.ax.set_ylabel('$y$', size=10, labelpad=-21, y=1.02, rotation=0)
        
        plt.text(0.49, 0.49, r"$O$", ha='right', va='top',
            transform=self.ax.transAxes,
                horizontalalignment='center', fontsize=8)
        
        x_ticks = np.arange(xmin, xmax+1, ticks_frequency)
        y_ticks = np.arange(ymin, ymax+1, ticks_frequency)
        self.ax.set_xticks(x_ticks[x_ticks != 0])
        self.ax.set_yticks(y_ticks[y_ticks != 0])
        
        # Alterar tamanho dos números dos eixos
        self.ax.tick_params(axis='x', labelsize=8)
        self.ax.tick_params(axis='y', labelsize=8)  # Tamanho 8

        self.ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

        # Create Canvas
        canvas = FigureCanvasTkAgg(self.fig, master=self.frame_2)  
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        retangulo = Rectangle(
            xy=(-2, -2),       # Canto inferior esquerdo
            width=4,           # Largura
            height=4,          # Altura
            edgecolor='black', # Borda
            facecolor='blue',  # Preenchimento
            zorder=1           # Ordem
        )
        plt.gca().add_patch(retangulo)

        circulo = Circle(
            xy=(0.5, 0.5),     # Centro do círculo
            radius=0.4,        # Raio
            edgecolor='black', # Cor da borda
            facecolor='white', # Cor de preenchimento
            zorder=2           # Ordem
        )
        plt.gca().add_patch(circulo)
        
        """
            situações de orientação meio_circulo
            orientação 0: 0-180
            orientação 1: 90-270
            orientação 2: 180-0
            orientacao 3: 270-90
        """

        meio_circulo = Wedge(
            center=(-0.5, 0.5), # Centro
            r=0.4,              # Raio
            theta1=0,         # Ângulo inicial (graus)
            theta2=180,           # Ângulo final (graus)
            edgecolor='black',  # Cor da borda
            facecolor='white',  # Cor de preenchimento
            zorder=2            # Ordem
        )
        plt.gca().add_patch(meio_circulo)

        """
            situações de orientação meio_circulo
            orientação 0: 0-90
            orientação 1: 90-180
            orientação 2: 180-270
            orientacao 3: 270-0
        """

        quarto_circulo = Wedge(
            center=(-0.5, -0.5), # Centro
            r=0.4,               # Raio
            theta1=90,            # Ângulo inicial (graus)
            theta2=180,           # Ângulo final (graus)
            edgecolor='black',   # Cor da borda
            facecolor='white',   # Cor de preenchimento
            zorder=2             # Ordem
        )
        plt.gca().add_patch(quarto_circulo)

        triangulo = Polygon(
            xy=[(1, 1), (2, 2), (1, 2)],              # Vértices (x, y)
            closed=True,                              # Fechar o polígono
            edgecolor='black',                        # Cor da borda
            facecolor='white',                        # Cor de preenchimento
            zorder=2                                  # Ordem
        )
        plt.gca().add_patch(triangulo)

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

    def add_record(self):
        global count
        self.list_forms.insert(parent='', index='end', iid=count, 
            text=self.geometric_form_entry.get(), values=(self.coordinate_x_entry.get(),self.coordinate_y_entry.get(),self.subare_entry.get()))
        count += 1     

    
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

        self.coordinate_center_x_entry = EntPlaceHold(self.frame_insert, 'X:')
        self.coordinate_center_x_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)

        self.coordinate_center_y_entry = EntPlaceHold(self.frame_insert, 'Y:')
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
            text="Origem do sistema", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_coordinates.place(relx=0.005, rely=0.65)

        self.coordinate_x_entry = EntPlaceHold(self.frame_insert, 'X:')
        self.coordinate_x_entry.place(relx=0.005, rely=0.69, relwidth=0.95, relheight=0.05)

        self.coordinate_y_entry = EntPlaceHold(self.frame_insert, 'Y:')
        self.coordinate_y_entry.place(relx=0.005, rely=0.75, relwidth=0.95, relheight=0.05)

        #======Buttons===========
        self.bt_acept = Button(
            self.frame_insert, 
            text="Inserir",
            font=('David', 10),
            bd= 0,
            command= self.add_record,
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
