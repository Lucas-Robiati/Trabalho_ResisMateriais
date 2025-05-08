from modulos import *
from tkinter import ttk
from tkinter import messagebox
from placeHolder import EntPlaceHold

class Validate:
    def validate_float(self, text):

        value = 0

        if ((text == "ponto Ax") or
            (text == "ponto Bx") or
            (text == "ponto Cx") or
            (text == "ponto Ay") or
            (text == "ponto By") or
            (text == "ponto Cy") or
            (text == "raio") or
            (text == "base") or
            (text == "altura") or
            (text == "X:") or
            (text == "Y:") or
            (text == "X: 0") or
            (text == "Y: 0") or
            (text == "...")): return True 

        if ((text == "") or (text == "-")): return True
        try:
            value == float(text)
        except ValueError:
            return False
        return (0 <= value) or (0 >= value)

class Application(Validate):
    def __init__(self, root:'Tk'):
        self.root = root    #Define o bejeto Tk que será usado como janela principal
        self.list_shapes = AreaComposta()
        self.window()       #Cria a janela principal sub janelas e widgets
        root.mainloop()

    def window(self):
        self.root.title("Calculadora de Momento de Inercia")
        self.root.configure(background= Color.dark_blue.value)
        self.root.geometry("950x520")
        self.root.minsize(width=950, height=520)
        self.root.resizable(True,True)
        self.root.bind("<Configure>", self.On_resize)
        self.root.protocol('WM_DELETE_WINDOW', self.destroy_window)  # Vincula o evento de fechamento
        self.Validate_entry()
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
        
        global count,aux
        count = 0
        aux = 0

        #--------coordinates--------------
        self.label_coordinates = Label(
            self.frame_1, 
            text="Origem do sistema:", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 11)
            )
        self.label_coordinates.place(relx=0.005, rely=0.59)

        self.coordinate_x_entry = EntPlaceHold(self.frame_1, placeholder='X: 0')
        self.coordinate_x_entry.configure(validate= "key", validatecommand=self.val)

        self.coordinate_y_entry = EntPlaceHold(self.frame_1, placeholder='Y: 0')
        self.coordinate_y_entry.configure(validate= "key", validatecommand=self.val)

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
        self.treeview_list = ttk.Treeview(
            self.frame_1,
            height= 4,
            columns=("col1","col2","col3","col4")
            )
        self.treeview_list.place(relx=0.01, rely=0.15, relwidth=0.95, relheight=0.4)

        self.scroobar = Scrollbar(self.frame_1, orient='vertical')               # Define a svrool bar
        self.treeview_list.configure(yscroll=self.scroobar.set)                     # Eixo da scrool bar
        self.scroobar.place(relx=0.96, rely=0.15, relwidth=0.04, relheight=0.4)  # Posição da scrool bar

        # Refencia a coluna e seta o texto
        self.treeview_list.heading("#0", text="Forma")         
        self.treeview_list.heading("#1", text="X")             
        self.treeview_list.heading("#2", text="Y")             
        self.treeview_list.heading("#3", text="Área virtual")  

        # Define tamanho da coluna e alinha o texto ao centro
        self.treeview_list.column("#0", width=150, anchor=CENTER, stretch=True)  
        self.treeview_list.column("#1", width=55, anchor=CENTER, stretch=True)   
        self.treeview_list.column("#2", width=55, anchor=CENTER, stretch=True)   
        self.treeview_list.column("#3", width=130, anchor=CENTER, stretch=True)
        
        self.treeview_list.bind('<Motion>', 'break')   #Impede o redimensionamento das colunas da tabela        

        #exemplo aceita interiros floats(2.5) variaveis (self.alguma_coisa) e strings
        #self.treeview_list.insert(
        #    "", 
        #    END, 
        #    text="Triangulo", 
        #    values=(2.5, 3,"subtrair")
        #    ) 
        #lista de objetos a ser passada 

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
    
    def widgets_frame2(self):
        self.xmin, self.xmax, self.ymin, self.ymax = -5, 5, -5, 5
        self.ticks_frequency = 1

        self.fig, self.ax = plt.subplots()
        self.fig.patch.set_facecolor('#ffffff')

        self.ax.spines['bottom'].set_position('zero')
        self.ax.spines['left'].set_position('zero')

        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        self.ax.set_xlabel('$x$', size=10, labelpad=-24, x=1.05)
        self.ax.set_ylabel('$y$', size=10, labelpad=-21, y=1.02, rotation=0)
        
        plt.text(0.49, 0.49, r"$O$", ha='right', va='top',
            transform=self.ax.transAxes,
                horizontalalignment='center', fontsize=8)
        
        self.Auto_Resize_Matplotlib()

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
            situações de orientação quarto de circulo
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
  
    def Auto_Resize_Matplotlib(self):
        self.ax.set(xlim=(self.xmin-1, self.xmax+1), ylim=(self.ymin-1, self.ymax+1), aspect='equal')
        
        self.x_ticks = np.arange(self.xmin, self.xmax+1, self.ticks_frequency)
        self.y_ticks = np.arange(self.ymin, self.ymax+1, self.ticks_frequency)
        
        self.ax.set_xticks(self.x_ticks[self.x_ticks != 0])
        self.ax.set_yticks(self.y_ticks[self.y_ticks != 0])

    def valid_source_plan(self):
        global aux
        if((self.coordinate_x_entry.get() == 'X: 0') and (self.coordinate_y_entry.get() == 'Y: 0') and (aux == 0)):
            # definir na horigem
            self.coordinate_x_entry.configure(state='disabled')
            self.coordinate_y_entry.configure(state='disabled')
            aux = 1
            msg = "A origem do sistema foi definida em (0,0), pois não foi passado como parametro"
            messagebox.showinfo("Info", msg, parent=self.insert)
            return 1
        else:
            try:
                entry_validate = float(self.coordinate_x_entry.get())
                entry_validate = float(self.coordinate_y_entry.get())
            except ValueError:
                if(aux == 0):
                    msg = "Origem do sistema está incompleta"
                    messagebox.showwarning("Error", msg, parent=self.insert)
                    return -1

    def add_record(self):

        entry_validate = 0

        if(self.valid_source_plan() == -1):
            return

        if(self.subare_entry.get()): 
            try:
                entry_validate = float(self.coordinate_center_x_entry.get())
                entry_validate = float(self.coordinate_center_y_entry.get())
                entry_validate = float(self.dimensions_a_px_entry.get())
                if(self.geometric_form_entry.get() == "Triangulo" or self.geometric_form_entry.get() == "Retangulo"):
                    entry_validate = float(self.dimensions_b_px_entry.get())
                    if(self.geometric_form_entry.get() == "Triangulo"):
                        entry_validate = float(self.dimensions_c_px_entry.get())

            except ValueError:
                msg = "Campo não preenchido ou invalido"
                messagebox.showerror("Error", msg, parent=self.insert)
                return
        else:
            msg = "Campo não preenchido ou invalido"
            messagebox.showerror("Error", msg, parent=self.insert)
            return

        self.add_object()


    def verify_subare(self):
        if(self.subare_entry.get() == "Subtrair"):
            return True
        return False

    def add_object(self):
        global count

        if(self.geometric_form_entry.get() == "Triangulo"):
            #new_form = Triangulo(Ponto2D(0,0), Ponto2D(4,0), Ponto2D(0,3), forma_virtual=False)
            pass

        if(self.geometric_form_entry.get() == "Circunferencia"):
            new_form = Circulo(float(self.dimensions_a_px_entry.get()), Ponto2D(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get())), self.verify_subare())
            self.list_shapes.append(new_form)
            
            self.treeview_list.insert(parent='', index='end', iid=count, 
                text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
            count += 1
            
        if(self.geometric_form_entry.get() == "Semi Circulo"):
            #new_form = SemiCirculo(raio=float(self.dimensions_a_px_entry), origem=Ponto2D(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get())), forma_virtual=self.verify_subare())
            #self.list_shapes.append(new_form)
            #
            #self.treeview_list.insert(parent='', index='end', iid=count, 
            #    text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
            #count += 1
            pass

        if(self.geometric_form_entry.get() == "Quarto de Circulo"):
            pass
        if(self.geometric_form_entry.get() == "Retangulo"):
            pass

    def Select_Form(self, event):
        if(self.geometric_form_entry.get() == "Triangulo"):

            self.dimensions_a_px_entry.place(relx=0.005, rely=0.17, relwidth=0.45, relheight=0.05)
            self.dimensions_b_px_entry.place(relx=0.005, rely=0.23, relwidth=0.45, relheight=0.05)
            self.dimensions_c_px_entry.place(relx=0.005, rely=0.295, relwidth=0.45, relheight=0.05)

            self.dimensions_a_py_entry.place(relx=0.48, rely=0.17, relwidth=0.5, relheight=0.05)
            self.dimensions_b_py_entry.place(relx=0.48, rely=0.23, relwidth=0.5, relheight=0.05)
            self.dimensions_c_py_entry.place(relx=0.48, rely=0.295, relwidth=0.5, relheight=0.05)

            self.dimensions_a_px_entry.delete('0', 'end')
            self.dimensions_a_px_entry.insert(0, 'ponto Ax')
            self.dimensions_a_px_entry.bind("<FocusIn>", lambda args: self.dimensions_a_px_entry.delete('0', 'end'))

            self.dimensions_b_px_entry.delete('0', 'end')
            self.dimensions_b_px_entry.insert(0, 'ponto Bx')
            self.dimensions_b_px_entry.bind("<FocusIn>", lambda args: self.dimensions_b_px_entry.delete('0', 'end'))
            
            self.dimensions_c_px_entry.delete('0', 'end')
            self.dimensions_c_px_entry.insert(0, 'ponto Cx')
            self.dimensions_c_px_entry.bind("<FocusIn>", lambda args: self.dimensions_c_px_entry.delete('0', 'end'))

            #self.dimensions_a_py_entry.delete('0', 'end')
            #self.dimensions_a_py_entry.insert(0, 'ponto Ay')
            self.dimensions_a_py_entry.bind("<FocusIn>", lambda args: self.dimensions_a_py_entry.delete('0', 'end'))

            #self.dimensions_b_py_entry.delete('0', 'end')
            #self.dimensions_b_py_entry.insert(0, 'ponto By')
            self.dimensions_b_py_entry.bind("<FocusIn>", lambda args: self.dimensions_b_py_entry.delete('0', 'end'))
            
            #self.dimensions_c_py_entry.delete('0', 'end')
            #self.dimensions_c_py_entry.insert(0, 'ponto Cy')
            self.dimensions_c_py_entry.bind("<FocusIn>", lambda args: self.dimensions_c_py_entry.delete('0', 'end'))

            self.label_coordinates_center.place_forget()
            self.coordinate_center_x_entry.place_forget()
            self.coordinate_center_y_entry.place_forget()

        if( (self.geometric_form_entry.get() == "Circunferencia") or 
            (self.geometric_form_entry.get() == "Semi Circulo") or
            (self.geometric_form_entry.get() == "Quarto de Circulo") ):
            
            self.dimensions_a_px_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)
            
            self.dimensions_a_px_entry.delete('0', 'end')
            self.dimensions_a_px_entry.insert(0, 'raio')
            self.dimensions_a_px_entry.bind("<FocusIn>", lambda args: self.dimensions_a_px_entry.delete('0', 'end'))

            self.dimensions_b_px_entry.delete('0', 'end')
            self.dimensions_b_px_entry.place_forget()
            
            self.dimensions_c_px_entry.delete('0', 'end')
            self.dimensions_c_px_entry.place_forget()

            self.dimensions_a_py_entry.place_forget()
            self.dimensions_b_py_entry.place_forget()
            self.dimensions_c_py_entry.place_forget()
            
            self.label_coordinates_center.place(relx=0.005, rely=0.5)
            self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
            self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)

        if(self.geometric_form_entry.get() == "Retangulo"): 

            self.dimensions_a_px_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)
            self.dimensions_b_px_entry.place(relx=0.005, rely=0.23, relwidth=0.95, relheight=0.05)
            
            self.dimensions_a_px_entry.delete('0', 'end')
            self.dimensions_a_px_entry.insert(0, 'base')
            self.dimensions_a_px_entry.bind("<FocusIn>", lambda args: self.dimensions_a_px_entry.delete('0', 'end'))

            self.dimensions_b_px_entry.delete('0', 'end')
            self.dimensions_b_px_entry.insert(0, 'altura')
            self.dimensions_b_px_entry.bind("<FocusIn>", lambda args: self.dimensions_b_px_entry.delete('0', 'end'))
            
            self.dimensions_c_px_entry.delete('0', 'end')
            self.dimensions_c_px_entry.place_forget()

            self.dimensions_a_py_entry.place_forget()
            self.dimensions_b_py_entry.place_forget()
            self.dimensions_c_py_entry.place_forget()
            
            self.label_coordinates_center.place(relx=0.005, rely=0.5)
            self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
            self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)
        
    def Validate_entry(self):
        self.val = (self.root.register(self.validate_float), '%P')

    def On_resize(self, event):
    
        if (event.width <= 950 and event.height <= 520):
            self.coordinate_x_entry.place(relx=0.33, rely=0.58, relwidth=0.25, relheight=0.05)
            self.coordinate_y_entry.place(relx=0.6, rely=0.58, relwidth=0.25, relheight=0.05)
        else:
            self.coordinate_x_entry.place(relx=0.23, rely=0.58, relwidth=0.3, relheight=0.04)
            self.coordinate_y_entry.place(relx=0.55, rely=0.58, relwidth=0.3, relheight=0.04)

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

        self.geometric_form_entry = ttk.Combobox(
            self.frame_insert,
            state= "readonly", 
            values=["Triangulo", "Circunferencia", "Quarto de Circulo", "Semi Circulo", "Retangulo"]
            )
        self.geometric_form_entry.config(
            foreground= Color.black.value, 
            background= Color.light_gray.value,
            )
        self.geometric_form_entry.place(relx=0.005, rely=0.045, relwidth=0.95, relheight=0.05)

        self.geometric_form_entry.bind("<<ComboboxSelected>>", self.Select_Form)
        self.geometric_form_entry.set("Triangulo")

        #-----------dimensions------------
        self.label_dimensions = Label(
            self.frame_insert, 
            text="Dimensões", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_dimensions.place(relx=0.005, rely=0.13)
        
        #---Entry eixo x dos pontos do triangulo------
        self.dimensions_a_px_entry = EntPlaceHold(self.frame_insert, placeholder='ponto Ax')
        self.dimensions_a_px_entry.config(state="normal", validate= "key", validatecommand=self.val)
        self.dimensions_a_px_entry.place(relx=0.005, rely=0.17, relwidth=0.45, relheight=0.05)

        self.dimensions_b_px_entry = EntPlaceHold(self.frame_insert, placeholder='ponto Bx')
        self.dimensions_b_px_entry.config(state="normal", validate= "key", validatecommand=self.val)
        self.dimensions_b_px_entry.place(relx=0.005, rely=0.23, relwidth=0.45, relheight=0.05)

        self.dimensions_c_px_entry = EntPlaceHold(self.frame_insert, placeholder='ponto Cx')
        self.dimensions_c_px_entry.config(state="normal", validate= "key", validatecommand=self.val)
        self.dimensions_c_px_entry.place(relx=0.005, rely=0.295, relwidth=0.45, relheight=0.05)
        
        #---Entry eixo y dos pontos do triangulo------
        self.dimensions_a_py_entry = EntPlaceHold(self.frame_insert, placeholder='ponto Ay')
        self.dimensions_a_py_entry.config(state="normal", validate= "key", validatecommand=self.val)
        self.dimensions_a_py_entry.place(relx=0.48, rely=0.17, relwidth=0.5, relheight=0.05)

        self.dimensions_b_py_entry = EntPlaceHold(self.frame_insert, placeholder='ponto By')
        self.dimensions_b_py_entry.config(state="normal", validate= "key", validatecommand=self.val)
        self.dimensions_b_py_entry.place(relx=0.48, rely=0.23, relwidth=0.5, relheight=0.05)

        self.dimensions_c_py_entry = EntPlaceHold(self.frame_insert, placeholder='ponto Cy')
        self.dimensions_c_py_entry.config(state="normal", validate= "key", validatecommand=self.val)
        self.dimensions_c_py_entry.place(relx=0.48, rely=0.295, relwidth=0.5, relheight=0.05)

        #--------centroid coordinates---------
        self.label_coordinates_center = Label(
            self.frame_insert, 
            text="Coordenada do centróide", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_coordinates_center.place_forget()

        self.coordinate_center_x_entry = EntPlaceHold(self.frame_insert, placeholder='X:')
        self.coordinate_center_x_entry.configure(validate= "key", validatecommand=self.val)
        self.coordinate_center_x_entry.place_forget()

        self.coordinate_center_y_entry = EntPlaceHold(self.frame_insert, placeholder='Y:')
        self.coordinate_center_y_entry.configure(validate= "key", validatecommand=self.val)
        self.coordinate_center_y_entry.place_forget()

        #-----------sub-are--------------
        self.label_subare = Label(
            self.frame_insert, 
            text="Subárea adicionada", 
            bg= Color.gray.value,
            fg= Color.white.value,
            font= ('David', 10)
            )
        self.label_subare.place(relx=0.005, rely=0.38)

        self.subare_entry = ttk.Combobox(
            self.frame_insert, 
            state="readonly", 
            values=["Subtrair", "Adicionar"]
            )
        self.subare_entry.config(foreground= Color.black.value, background= Color.light_gray.value)
        self.subare_entry.place(relx=0.005, rely=0.42, relwidth=0.95, relheight=0.05)

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
