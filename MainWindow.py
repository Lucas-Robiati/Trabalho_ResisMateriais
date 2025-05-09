from Modules import *

class Application(Validate):
  def __init__(self, root:'Tk'):
    self.root = root                            # Define o bejeto Tk que será usado como janela principal
    self.composite_figure =  ICCompositeFigure()     # Lista de Obejetos
    self.dict_shapes = {}
    self.system_origin = ICPoint2D()            # Variavel que define a origem do sistema
    self.window()                               # Cria a janela principal sub janelas e widgets
    root.mainloop()                             # Loop da janela

  def window(self):
    self.root.title("InerCalc")                                  # Nome do software
    self.root.configure(background= Color.dark_blue.value)       # Background da janela principal
    self.root.geometry("950x520")                                # Geometria da janela 
    self.root.minsize(width=950, height=520)                     # Tamanho minimo da janela 
    self.root.resizable(True,True)                               # Software pode redimensionar 
    self.root.bind("<Configure>", self.on_resize)                # Sinal para acionar a função de redimencionamento
    self.root.protocol('WM_DELETE_WINDOW', self.destroy_window)  # Vincula o evento de fechamento
    self.validate_entry()                                        # Chamada do validador dos entry
    self.window_frame()                                          # Cria os frames que conterão os widgets

  def destroy_window(self):
  # Função para tratar o fechamento da janela
    plt.close(self.fig)   # Fecha a figura do Matplotlib
    root.destroy()        # Destroi a janela do Tkinter

  # Cria os frames dentro da janela principal
  def window_frame(self):
    self.frame_1 = Frame(
      self.root, 
      bd=4, bg=Color.gray.value,
      highlightbackground= Color.light_gray.value, 
      highlightthickness= 4
      )
    self.frame_1.place(relx=0.015, rely=0.025, relwidth=0.45, relheight=0.95)

    # Cria e define os elementos contidos no frame 1
    self.widgets_frame1()

    self.frame_2 = Frame(
      self.root, 
      bd=4, 
      bg=Color.gray.value, 
      highlightbackground= Color.light_gray.value, 
      highlightthickness= 4
      )
    self.frame_2.place(relx=0.465, rely=0.12, relwidth=0.52, relheight=0.855)
    
    # Cria e define os elementos contidos no frame 2
    self.widgets_frame2()

    self.frame_3 = Frame(
      self.root, 
      bd=4, 
      bg=Color.gray.value, 
      highlightbackground= Color.light_gray.value, 
      highlightthickness= 4
      )
    self.frame_3.place(relx=0.015, rely=0.025, relwidth=0.97, relheight=0.1)

    # Cria e define os elementos contidos no frame 3
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

    # Classe persobalizada EntPlaceHold para modificar o Entry adicona uma string como parametro para um "place Holder" 
    self.coordinate_x_entry = EntPlaceHold(self.frame_1, placeholder='X: 0')
    # Captura a entrada de caracteres da entrada e aplica a função de validação conforme o sinal
    self.coordinate_x_entry.configure(validate= "key", validatecommand=self.val)

    # Classe persobalizada EntPlaceHold para modificar o Entry adicona uma string como parametro para um "place Holder" 
    self.coordinate_y_entry = EntPlaceHold(self.frame_1, placeholder='Y: 0')
    # Captura a entrada de caracteres da entrada e aplica a função de validação conforme o sinal
    self.coordinate_y_entry.configure(validate= "key", validatecommand=self.val)

    # Cria o Botão Calcular
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

    # Lable que da nome pra tabela
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

    # Cria a barra de srool lateral 
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

    #=========style==============
    style_table = ttk.Style()#  Classe de configuração de estilo da tabela
    style_table.theme_use("clam")#  Tema da tabela
    style_table.configure(
      "Treeview", 
      background= Color.light_gray.value, 
      foreground= Color.black.value,
      fieldbackground= Color.gray.value,
      font=("Arial", 10)
      )
      
    style_table.map("Treeview",
      background=[('selected', Color.light_blue.value)],
      foreground=[('selected', Color.white.value)]
      )
  
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
      horizontalalignment='center', fontsize=8
      )
    
    self.auto_resize_matplotlib()
    
    # Alterar tamanho dos números dos eixos
    self.ax.tick_params(axis='x', labelsize=8)
    self.ax.tick_params(axis='y', labelsize=8)  # Tamanho 8

    self.ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Create Canvas
    canvas = FigureCanvasTkAgg(self.fig, master=self.frame_2)  
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

  def widgets_frame3(self):
    self.bt_reset = Button(
      self.frame_3, 
      text="Redefinir tudo",
      font=('David', 10),
      bd= 0,
      command=self.ICreset,
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
      command=self.insert_window,
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
      command=self.remove_item,
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
      command=self.Modify_object,
      activebackground= Color.white.value,
      activeforeground= Color.black.value,
      bg= Color.gray.value,
      fg= Color.white.value
      )
    self.bt_atualize.place(relx=0.26, rely=0.15, relwidth=0.12, relheight=0.8)

  def insert_window(self):
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
      values=["Triangulo", "Circunferencia", "Quadrante", "Semicirculo", "Retangulo"]
      )
    self.geometric_form_entry.config(
      foreground= Color.black.value, 
      background= Color.light_gray.value,
      )
    self.geometric_form_entry.place(relx=0.005, rely=0.045, relwidth=0.95, relheight=0.05)

    self.geometric_form_entry.bind("<<ComboboxSelected>>", self.select_form)
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

    self.dimensions_b_px_entry = EntPlaceHold(self.frame_insert, placeholder='ponto Ay')
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

    self.rad_entry = EntPlaceHold(self.frame_insert, placeholder='raio')
    self.rad_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.rad_entry.place_forget()

    self.base_entry = EntPlaceHold(self.frame_insert, placeholder='base')
    self.base_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.base_entry.place_forget()

    self.height_entry = EntPlaceHold(self.frame_insert, placeholder='altura')
    self.height_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.height_entry.place_forget()

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

    self.label_combobox_orientation = Label(self.frame_insert, 
      text="Orientação", 
      bg= Color.gray.value,
      fg= Color.white.value,
      font= ('David', 10)
      )
    self.label_combobox_orientation.place_forget()

    self.combobox_orientation = ttk.Combobox(self.frame_insert,
      state= "readonly",
      justify="center",
      font= ('David', 10), 
      values=["◴", "◷", "◵", "◶"]
      )
    self.combobox_orientation.place_forget()

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
      command= self.destroy_insert_window,
      activebackground= Color.white.value,
      activeforeground= Color.black.value,
      bg= Color.gray.value,
      fg= Color.white.value
      )
    self.bt_quit.place(relx=0.55, rely=0.9, relwidth=0.25, relheight=0.08)
  
  # Foi necessario criar uma nova janela para atualizar as formas geometricas
  # pois a janela de insert carrega algumas interações especificas
  #------janela de update da forma---------
  def update_window(self, text:str):
    self.update_window = Toplevel()
    self.update_window.title("Atualizar Forma Geometrica")
    self.update_window.configure(background= Color.dark_blue.value)
    self.update_window.geometry("300x500")
    self.update_window.resizable(False, False)
    self.update_window.transient(self.root)
    self.update_window.focus_force()
    self.update_window.grab_set()

    self.frame_update = Frame(
      self.update_window, 
      bd=4, bg=Color.gray.value,
      highlightbackground= Color.light_gray.value, 
      highlightthickness= 4
      )
    self.frame_update.place(relx=0.024, rely=0.025, relwidth=0.95, relheight=0.95)

    #------geometric form--------
    self.label_geometric_form = Label(
      self.frame_update, 
      text="Forma a ser atualizada", 
      bg= Color.gray.value,
      fg= Color.white.value,
      font= ('David', 10)
      )
    self.label_geometric_form.place(relx=0.005, rely=0.01)

    self.geometric_form_entry = ttk.Combobox(
      self.frame_update,
      state= "normal", 
      values=["Triangulo", "Circunferencia", "Quadrante", "Semicirculo", "Retangulo"]
      )
    self.geometric_form_entry.config(
      foreground= Color.black.value, 
      background= Color.light_gray.value,
      )
    self.geometric_form_entry.place(relx=0.005, rely=0.045, relwidth=0.95, relheight=0.05)

    self.geometric_form_entry.bind("<<ComboboxSelected>>", self.select_form)
    # ver como fazer
    self.geometric_form_entry.set(text)
    self.geometric_form_entry.configure(state="disabled")

    #-----------dimensions------------
    self.label_dimensions = Label(
      self.frame_update, 
      text="Dimensões", 
      bg= Color.gray.value,
      fg= Color.white.value,
      font= ('David', 10)
      )
    self.label_dimensions.place(relx=0.005, rely=0.13)
    
    #---Entry eixo x dos pontos do triangulo------
    self.dimensions_a_px_entry = EntPlaceHold(self.frame_update, placeholder='ponto Ax')
    self.dimensions_a_px_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.dimensions_a_px_entry.place_forget()

    self.dimensions_b_px_entry = EntPlaceHold(self.frame_update, placeholder='ponto Ay')
    self.dimensions_b_px_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.dimensions_b_px_entry.place_forget()

    self.dimensions_c_px_entry = EntPlaceHold(self.frame_update, placeholder='ponto Cx')
    self.dimensions_c_px_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.dimensions_c_px_entry.place_forget()
    
    #---Entry eixo y dos pontos do triangulo------
    self.dimensions_a_py_entry = EntPlaceHold(self.frame_update, placeholder='ponto Ay')
    self.dimensions_a_py_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.dimensions_a_py_entry.place_forget()

    self.dimensions_b_py_entry = EntPlaceHold(self.frame_update, placeholder='ponto By')
    self.dimensions_b_py_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.dimensions_b_py_entry.place_forget()

    self.dimensions_c_py_entry = EntPlaceHold(self.frame_update, placeholder='ponto Cy')
    self.dimensions_c_py_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.dimensions_c_py_entry.place_forget()

    self.rad_entry = EntPlaceHold(self.frame_update, placeholder='raio')
    self.rad_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.rad_entry.place_forget()

    self.base_entry = EntPlaceHold(self.frame_update, placeholder='base')
    self.base_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.base_entry.place_forget()

    self.height_entry = EntPlaceHold(self.frame_update, placeholder='altura')
    self.height_entry.config(state="normal", validate= "key", validatecommand=self.val)
    self.height_entry.place_forget()
    
    #--------centroid coordinates---------
    self.label_coordinates_center = Label(
      self.frame_update, 
      text="Coordenada do centróide", 
      bg= Color.gray.value,
      fg= Color.white.value,
      font= ('David', 10)
      )
    self.label_coordinates_center.place_forget()

    self.coordinate_center_x_entry = EntPlaceHold(self.frame_update, placeholder='X:')
    self.coordinate_center_x_entry.configure(validate= "key", validatecommand=self.val)
    self.coordinate_center_x_entry.place_forget()

    self.coordinate_center_y_entry = EntPlaceHold(self.frame_update, placeholder='Y:')
    self.coordinate_center_y_entry.configure(validate= "key", validatecommand=self.val)
    self.coordinate_center_y_entry.place_forget()

    #-----------sub-are--------------
    self.label_subare = Label(
      self.frame_update, 
      text="Subárea adicionada", 
      bg= Color.gray.value,
      fg= Color.white.value,
      font= ('David', 10)
      )
    self.label_subare.place(relx=0.005, rely=0.38)

    self.subare_entry = ttk.Combobox(
      self.frame_update, 
      state="readonly", 
      values=["Subtrair", "Adicionar"]
      )
    self.subare_entry.config(foreground= Color.black.value, background= Color.light_gray.value)
    self.subare_entry.place(relx=0.005, rely=0.42, relwidth=0.95, relheight=0.05)

    self.label_combobox_orientation = Label(self.frame_update, 
      text="Orientação", 
      bg= Color.gray.value,
      fg= Color.white.value,
      font= ('David', 10)
      )
    self.label_combobox_orientation.place_forget()

    self.combobox_orientation = ttk.Combobox(
      self.frame_update,
      state= "readonly",
      justify="center",
      font= ('David', 10), 
      values=["◴", "◷", "◵", "◶"]
      )
    self.combobox_orientation.place_forget()

    self.Decision_form()

    #======Buttons===========
    self.bt_acept = Button(
      self.frame_update, 
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
      self.frame_update, 
      text="Cancelar",
      font=('David', 10),
      bd= 0,
      command= self.destroy_insert_window,
      activebackground= Color.white.value,
      activeforeground= Color.black.value,
      bg= Color.gray.value,
      fg= Color.white.value
      )
    self.bt_quit.place(relx=0.55, rely=0.9, relwidth=0.25, relheight=0.08)

  def destroy_insert_window(self):
    self.insert.destroy()

  def ICreset(self): 
    global aux
    # Remove todos os itens da Treeview
    for item in self.treeview_list.get_children():
        self.treeview_list.delete(item)
        
    for item in range(len(self.composite_figure.components)):
      self.composite_figure.drop(item)
      figure = self.dict_shapes[self.composite_figure.components[item]]
      figure.remove()
    # Limpa o dicionário de formas gráficas
    self.dict_shapes.clear()
    # Redesenha o gráfico vazio
    self.auto_resize_matplotlib()
    plt.draw()
    aux = 0
    self.coordinate_x_entry.configure(state='normal')
    self.coordinate_y_entry.configure(state='normal')

      # Remove as formas da tabela e da lista de objetos
  def remove_item(self):
    select = self.treeview_list.selection()[0]
    if(select):
      index = self.treeview_list.index(select)
      print(index)
      self.treeview_list.delete(select)
      figure = self.dict_shapes[self.composite_figure.components[index]]
      figure.remove()
      self.dict_shapes.pop(self.composite_figure.components[index])            
      self.composite_figure.drop(index)
      plt.draw()
  
  def Modify_object(self):

    select = self.treeview_list.selection()
    if(select):
        data = self.treeview_list.item(select[0])
        index = self.treeview_list.index(select)
        iid = select[0]
        _str = data['text']
        values = self.treeview_list.item(iid, "values") 
        self.update_window(_str)
        
    if(_str == "Triangulo"):
      self.dimensions_a_px_entry.delete('0', 'end')
      self.dimensions_a_px_entry.insert(0,self.composite_figure.components[index].Pa.x)
      self.dimensions_b_px_entry.delete('0', 'end')
      self.dimensions_b_px_entry.insert(0,self.composite_figure.components[index].Pb.x)
      self.dimensions_c_px_entry.delete('0', 'end')
      self.dimensions_c_px_entry.insert(0,self.composite_figure.components[index].Pc.x)
      self.dimensions_a_py_entry.delete('0', 'end')
      self.dimensions_a_py_entry.insert(0,self.composite_figure.components[index].Pa.y)
      self.dimensions_b_py_entry.delete('0', 'end')
      self.dimensions_b_py_entry.insert(0,self.composite_figure.components[index].Pb.y)
      self.dimensions_c_py_entry.delete('0', 'end')
      self.dimensions_c_py_entry.insert(0,self.composite_figure.components[index].Pc.y)
        
      self.subare_entry.set(values[2])          
          
    if(_str == "Circunferencia"):
      self.rad_entry.delete('0', 'end')
      self.rad_entry.insert(0, self.composite_figure.components[index].radius)
        
      self.coordinate_center_x_entry.delete('0', 'end')
      self.coordinate_center_x_entry.insert(0, self.composite_figure.components[index].centroid.x)
        
      self.coordinate_center_y_entry.delete('0', 'end')
      self.coordinate_center_y_entry.insert(0, self.composite_figure.components[index].centroid.y)
        
      self.subare_entry.set(values[2])

    if(_str == "Quadrante"):
      self.rad_entry.delete('0', 'end')
      self.rad_entry.insert(0, self.composite_figure.components[index].radius)

      self.combobox_orientation.set(self.Quadrante_combobox_orientation(self.composite_figure.components[index].orientation))
          
      self.coordinate_center_x_entry.delete('0', 'end')
      self.coordinate_center_x_entry.insert(0, self.composite_figure.components[index].origin.x)

      self.coordinate_center_y_entry.delete('0', 'end')
      self.coordinate_center_y_entry.insert(0, self.composite_figure.components[index].origin.y)

      self.subare_entry.set(values[2])
      
    if(_str == "Semicirculo"):
      self.rad_entry.delete('0', 'end')
      self.rad_entry.insert(0, self.composite_figure.components[index].radius)

      self.combobox_orientation.set(self.Semicirculo_combobox_orientation(self.composite_figure.components[index].orientation))

      self.coordinate_center_x_entry.delete('0', 'end')
      self.coordinate_center_x_entry.insert(0, self.composite_figure.components[index].origin.x)

      self.coordinate_center_y_entry.delete('0', 'end')
      self.coordinate_center_y_entry.insert(0, self.composite_figure.components[index].origin.y)

      self.subare_entry.set(values[2])
        
    if(_str == "Retangulo"):
      self.base_entry.delete('0', 'end')
      self.base_entry.insert(0, self.composite_figure.components[index].width)
          
      self.height_entry.delete('0', 'end')
      self.height_entry.insert(0, self.composite_figure.components[index].height)

      self.subare_entry.set(values[2])

      self.coordinate_center_x_entry.delete('0', 'end')
      self.coordinate_center_x_entry.insert(0, self.composite_figure.components[index].centroid.x)

      self.coordinate_center_y_entry.delete('0', 'end')
      self.coordinate_center_y_entry.insert(0, self.composite_figure.components[index].centroid.y)
          

      

  def valid_source_plan(self):
    global aux
    if((self.coordinate_x_entry.get() == 'X: 0') and (self.coordinate_y_entry.get() == 'Y: 0') and (aux == 0)):
      # definir na horigem
      self.coordinate_x_entry.configure(state='disabled')
      self.coordinate_y_entry.configure(state='disabled')
      aux = 1
      msg = "A origem do sistema foi definida em (0,0), pois não foi passado como parametro"
      messagebox.showinfo("Info", msg, parent=self.insert)
        
    if(aux == 0):
      try:
        entry_validate = float(self.coordinate_x_entry.get())
        entry_validate = float(self.coordinate_y_entry.get())
      except ValueError:
        if(aux == 0):
          msg = "Origem do sistema está incompleta"
          messagebox.showwarning("Error", msg, parent=self.insert)
          return -1
      
      self.coordinate_x_entry.configure(state='disabled')
      self.coordinate_y_entry.configure(state='disabled')
      self.system_origin.x = float(self.coordinate_x_entry.get())
      self.system_origin.y = float(self.coordinate_y_entry.get())
    return 1

  # Valida e chama as funções de inserir objetos 
  def add_record(self):
    entry_validate = 0
    if(self.valid_source_plan() == -1):
      return

    if(self.subare_entry.get()): 
      try:
        if(self.geometric_form_entry.get() == "Triangulo"):
          entry_validate = float(self.dimensions_a_px_entry.get())
          entry_validate = float(self.dimensions_b_px_entry.get())
          entry_validate = float(self.dimensions_c_px_entry.get())
          entry_validate = float(self.dimensions_a_py_entry.get())
          entry_validate = float(self.dimensions_b_py_entry.get())
          entry_validate = float(self.dimensions_c_py_entry.get())
        
        if((self.geometric_form_entry.get() == "Circulo") or (self.geometric_form_entry.get() == "Semicirculo") or (self.geometric_form_entry.get() == "Quadrante")):
          entry_validate = float(self.rad_entry.get())
        
        if(self.geometric_form_entry.get() == "Retangulo"):
          entry_validate = float(self.base_entry.get())
          entry_validate = float(self.height_entry.get())
                  
      except ValueError:
        msg = "Campo não preenchido ou invalido"
        messagebox.showerror("Error", msg, parent=self.insert)
        return
    else:
      msg = "Campo não preenchido ou invalido"
      messagebox.showerror("Error", msg, parent=self.insert)
      return

    figureCF = self.add_object()
    figureMPL = self.add_figure_matplotlib()

    self.dict_shapes |= {figureCF: figureMPL}
    return None

  # Identifica o tipo de objeto inserido e o adiciona na tabela e na lista de objetos
  def add_object(self):
    global count

    if(self.geometric_form_entry.get() == "Triangulo"):
      new_form = ICTriangle(Pa=ICPoint2D(float(self.dimensions_a_px_entry.get()),float(self.dimensions_a_py_entry.get())), Pb=ICPoint2D(float(self.dimensions_b_px_entry.get()),float(self.dimensions_b_py_entry.get())), Pc=ICPoint2D(float(self.dimensions_c_px_entry.get()),float(self.dimensions_c_py_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare()) 
      if(new_form.valido() == -1):
        msg = "Triangulo Invalido: os pontos não formam um triangulo"
        messagebox.showerror("Error", msg, parent=self.insert)
        return
      self.composite_figure.append(new_form)

      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form

    if(self.geometric_form_entry.get() == "Circunferencia"):
      new_form =  ICCircle(radius=float(self.rad_entry.get()),  centroid=ICPoint2D(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)
      
      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form
        
    if(self.geometric_form_entry.get() == "Semicirculo"):
      new_form = ICSemicircle(orientation=self.relation_combobox_orientation(),radius=float(self.rad_entry.get()), origin=ICPoint2D(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)

      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form

    if(self.geometric_form_entry.get() == "Quadrante"):
      new_form = ICQuadrant(orientation=self.relation_combobox_orientation(),radius=float(self.rad_entry.get()), origin=ICPoint2D(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)
      
      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form

    if(self.geometric_form_entry.get() == "Retangulo"):
      new_form = ICRectangle(width=float(self.base_entry.get()), height=float(self.height_entry.get()), centroid=ICPoint2D(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)
      
      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form
  
  def add_figure_matplotlib(self) -> None:
    if(self.verify_subare()):
      subarea = 2     # Subtrair (Fica a frente)
      edgeclr='black' # Cor da borda
      faceclr='white' # Cor de preenchimento
    else:
      subarea = 1     # Adicionar (Fica atras)
      edgeclr='black' # Borda
      faceclr='blue'  # Preenchimento

    if(self.geometric_form_entry.get() == "Triangulo"):
      figure = Polygon(
        xy=[(float(self.dimensions_a_px_entry.get()),float(self.dimensions_a_py_entry.get())),  # Ponto A Vértices (x, y)
            (float(self.dimensions_b_px_entry.get()),float(self.dimensions_b_py_entry.get())),  # Ponto B Vértices (x, y)
            (float(self.dimensions_c_px_entry.get()),float(self.dimensions_c_py_entry.get()))], # Ponto C Vértices (x, y)
        closed=True,                              # Fechar o polígono
        edgecolor=edgeclr,                        # Cor da borda
        facecolor=faceclr,                        # Cor de preenchimento
        zorder=subarea                            # Ordem
      )

    if(self.geometric_form_entry.get() == "Circunferencia"):
      figure = Circle(
        xy=(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get())),     # Centro do círculo
        radius=float(self.rad_entry.get()),        # Raio
        edgecolor=edgeclr, # Cor da borda
        facecolor=faceclr, # Cor de preenchimento
        zorder=subarea           # Ordem
      )

    if(self.geometric_form_entry.get() == "Semicirculo"):
      figure = Wedge(
        center=(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), # Centro
        r=float(self.rad_entry.get()),              # Raio
        theta1=0,         # Ângulo inicial (graus)
        theta2=180,           # Ângulo final (graus)
        edgecolor=edgeclr,  # Cor da borda
        facecolor=faceclr,  # Cor de preenchimento
        zorder=subarea            # Ordem
      )
      """
        situações de orientação meio_circulo
        orientação 0: 0-180
        orientação 1: 90-270
        orientação 2: 180-0
        orientacao 3: 270-90
      """
    
    if(self.geometric_form_entry.get() == "Quadrante"):
      figure = Wedge(
        center=(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), # Centro
        r=float(self.rad_entry.get()),               # Raio
        theta1=90,            # Ângulo inicial (graus)
        theta2=180,           # Ângulo final (graus)
        edgecolor=edgeclr,   # Cor da borda
        facecolor=faceclr,   # Cor de preenchimento
        zorder=subarea             # Ordem
      )
      """
        situações de orientação quarto de circulo
        orientação 0: 0-90
        orientação 1: 90-180
        orientação 2: 180-270
        orientacao 3: 270-0
      """

    if(self.geometric_form_entry.get() == "Retangulo"):
      figure = Rectangle(
        xy=((float(self.coordinate_center_x_entry.get()) - (float(self.base_entry.get()) / 2)),
            (float(self.coordinate_center_y_entry.get()) - (float(self.height_entry.get()) / 2))),       # Canto inferior esquerdo
        width=float(self.base_entry.get()),           # Largura
        height=float(self.height_entry.get()),          # Altura
        edgecolor=edgeclr, # Borda
        facecolor=faceclr,  # Preenchimento
        zorder=subarea           # Ordem
      )

    plt.gca().add_patch(figure)
    plt.draw()
    return figure

  # Encapsulamento necessario devido a update
  def select_form(self, event):
    self.Decision_form()
    
  def Decision_form(self):
    if(self.geometric_form_entry.get() == "Triangulo"):
      self.dimensions_a_px_entry.place(relx=0.005, rely=0.17, relwidth=0.45, relheight=0.05)
      self.dimensions_b_px_entry.place(relx=0.005, rely=0.23, relwidth=0.45, relheight=0.05)
      self.dimensions_c_px_entry.place(relx=0.005, rely=0.295, relwidth=0.45, relheight=0.05)

      self.dimensions_a_py_entry.place(relx=0.48, rely=0.17, relwidth=0.5, relheight=0.05)
      self.dimensions_b_py_entry.place(relx=0.48, rely=0.23, relwidth=0.5, relheight=0.05)
      self.dimensions_c_py_entry.place(relx=0.48, rely=0.295, relwidth=0.5, relheight=0.05)

      # Eventos para apagar a escrita do placeholder ponto Ax.Bx.Cx e reescrver o novo texto dos Entry
      self.dimensions_a_px_entry.delete('0', 'end')
      self.dimensions_a_px_entry.insert(0, 'ponto Ax')
      self.dimensions_a_px_entry.bind("<FocusIn>", lambda args: self.dimensions_a_px_entry.delete('0', 'end'))

      self.dimensions_b_px_entry.delete('0', 'end')
      self.dimensions_b_px_entry.insert(0, 'ponto Bx')
      self.dimensions_b_px_entry.bind("<FocusIn>", lambda args: self.dimensions_b_px_entry.delete('0', 'end'))
      
      self.dimensions_c_px_entry.delete('0', 'end')
      self.dimensions_c_px_entry.insert(0, 'ponto Cx')
      self.dimensions_c_px_entry.bind("<FocusIn>", lambda args: self.dimensions_c_px_entry.delete('0', 'end'))

      # Eventos para apagar a escrita do placeholder ponto Ay.By.Cy
      self.dimensions_a_py_entry.bind("<FocusIn>", lambda args: self.dimensions_a_py_entry.delete('0', 'end'))
      self.dimensions_b_py_entry.bind("<FocusIn>", lambda args: self.dimensions_b_py_entry.delete('0', 'end'))
      self.dimensions_c_py_entry.bind("<FocusIn>", lambda args: self.dimensions_c_py_entry.delete('0', 'end'))

      # Oculta as lables e Entrys desnecessarios
      self.rad_entry.place_forget()
      self.base_entry.place_forget()
      self.height_entry.place_forget()
      self.combobox_orientation.place_forget()
      self.label_coordinates_center.place_forget()
      self.coordinate_center_x_entry.place_forget()
      self.coordinate_center_y_entry.place_forget()
      self.combobox_orientation.place_forget()
      self.label_combobox_orientation.place_forget()

    if((self.geometric_form_entry.get() == "Circunferencia")):
      self.rad_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)
      
      self.rad_entry.delete('0', 'end')
      self.rad_entry.insert(0, 'raio')
      self.rad_entry.bind("<FocusIn>", lambda args: self.rad_entry.delete('0', 'end'))

      self.base_entry.place_forget()
      self.height_entry.place_forget()
      self.dimensions_a_px_entry.place_forget()
      self.dimensions_b_px_entry.place_forget()
      self.dimensions_c_px_entry.place_forget()
      self.dimensions_a_py_entry.place_forget()
      self.dimensions_b_py_entry.place_forget()
      self.dimensions_c_py_entry.place_forget()
      self.combobox_orientation.place_forget()
      self.label_combobox_orientation.place_forget()
      
      self.label_coordinates_center.config(text="Coordenada do centróide")
      self.label_coordinates_center.place(relx=0.005, rely=0.5)
      self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
      self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)

    if(self.geometric_form_entry.get() == "Semicirculo"):
      self.rad_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)
      
      self.rad_entry.delete('0', 'end')
      self.rad_entry.insert(0, 'raio')
      self.rad_entry.bind("<FocusIn>", lambda args: self.rad_entry.delete('0', 'end'))

      # Reposiciona a lable de origem 
      self.label_combobox_orientation.place(relx=0.005, rely=0.25, relwidth=0.45, relheight=0.05)

      # Reposiciona a selecao da origem
      self.combobox_orientation.place(relx=0.005, rely=0.295, relwidth=0.45, relheight=0.05)
      self.combobox_orientation['values'] = ["◗","◖","◒","◓"]

      self.base_entry.place_forget()
      self.height_entry.place_forget()
      self.dimensions_a_px_entry.place_forget()
      self.dimensions_b_px_entry.place_forget()
      self.dimensions_c_px_entry.place_forget()
      self.dimensions_a_py_entry.place_forget()
      self.dimensions_b_py_entry.place_forget()
      self.dimensions_c_py_entry.place_forget()
      
      self.label_coordinates_center.config(text="Origem")
      self.label_coordinates_center.place(relx=0.005, rely=0.5)
      
      self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
      self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)
      
    if(self.geometric_form_entry.get() == "Quadrante"):
      
      self.rad_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)
      
      self.rad_entry.delete('0', 'end')
      self.rad_entry.insert(0, 'raio')
      self.rad_entry.bind("<FocusIn>", lambda args: self.rad_entry.delete('0', 'end'))

      # Reposiciona a lable de origem 
      self.label_combobox_orientation.place(relx=0.005, rely=0.25, relwidth=0.45, relheight=0.05)

      # Reposiciona a selecao da origem
      self.combobox_orientation.place(relx=0.005, rely=0.295, relwidth=0.45, relheight=0.05)
      self.combobox_orientation['values'] = ["◴", "◷", "◵", "◶"]

      self.base_entry.place_forget()
      self.height_entry.place_forget()
      self.dimensions_a_px_entry.place_forget()
      self.dimensions_b_px_entry.place_forget()
      self.dimensions_c_px_entry.place_forget()
      self.dimensions_a_py_entry.place_forget()
      self.dimensions_b_py_entry.place_forget()
      self.dimensions_c_py_entry.place_forget()
      
      self.label_coordinates_center.config(text="Origem")
      self.label_coordinates_center.place(relx=0.005, rely=0.5)
      
      self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
      self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)

    if(self.geometric_form_entry.get() == "Retangulo"): 
      self.base_entry.place(relx=0.005, rely=0.17, relwidth=0.95, relheight=0.05)
      self.height_entry.place(relx=0.005, rely=0.23, relwidth=0.95, relheight=0.05)
      
      self.base_entry.delete('0', 'end')
      self.base_entry.insert(0, 'base')
      self.base_entry.bind("<FocusIn>", lambda args: self.base_entry.delete('0', 'end'))

      self.height_entry.delete('0', 'end')
      self.height_entry.insert(0, 'altura')
      self.height_entry.bind("<FocusIn>", lambda args: self.height_entry.delete('0', 'end'))

      self.label_combobox_orientation.place_forget()
      self.combobox_orientation.place_forget()
      self.rad_entry.place_forget()
      self.dimensions_a_px_entry.place_forget()
      self.dimensions_b_px_entry.place_forget()
      self.dimensions_c_px_entry.place_forget()
      self.dimensions_a_py_entry.place_forget()
      self.dimensions_b_py_entry.place_forget()
      self.dimensions_c_py_entry.place_forget()
      
      self.label_coordinates_center.config(text="Coordenada do centróide")
      self.label_coordinates_center.place(relx=0.005, rely=0.5)
      self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
      self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)  
  
  def validate_entry(self):
    self.val = (self.root.register(self.validate_float), '%P')

  # Verifica se o objeto será subtraido ou adicionado
  def verify_subare(self):
    if(self.subare_entry.get() == "Subtrair"):
      return True
    return False

  def relation_combobox_orientation(self):
    if(self.combobox_orientation.get() == "◷") or (self.combobox_orientation.get() == "◓"):
      return 0
    if(self.combobox_orientation.get() == "◴") or (self.combobox_orientation.get() == "◖"):
      return 1
    if(self.combobox_orientation.get() == "◵") or (self.combobox_orientation.get() == "◒"):
      return 2
    if(self.combobox_orientation.get() == "◶") or (self.combobox_orientation.get() == "◗"):
      return 3
  
  def Semicirculo_combobox_orientation(self, ori):
    if(ori == 0):
      return "◓"

    if(ori == 1):
      return "◖"

    if(ori == 2):
      return "◒"

    if(ori == 3):
      return "◗"

  def Quadrante_combobox_orientation(self, ori):
    if(ori == 0):
      return "◷"

    if(ori == 1):
      return "◴"

    if(ori == 2):
      return "◵"

    if(ori == 3):
      return "◶"

  def on_resize(self, event):
    if (event.width <= 950 and event.height <= 520):
      self.coordinate_x_entry.place(relx=0.33, rely=0.58, relwidth=0.25, relheight=0.05)
      self.coordinate_y_entry.place(relx=0.6, rely=0.58, relwidth=0.25, relheight=0.05)
    else:
      self.coordinate_x_entry.place(relx=0.23, rely=0.58, relwidth=0.3, relheight=0.04)
      self.coordinate_y_entry.place(relx=0.55, rely=0.58, relwidth=0.3, relheight=0.04)
  
  def auto_resize_matplotlib(self):
    self.ax.set(xlim=(self.xmin-1, self.xmax+1), ylim=(self.ymin-1, self.ymax+1), aspect='equal')
    
    self.x_ticks = np.arange(self.xmin, self.xmax+1, self.ticks_frequency)
    self.y_ticks = np.arange(self.ymin, self.ymax+1, self.ticks_frequency)
    
    self.ax.set_xticks(self.x_ticks[self.x_ticks != 0])
    self.ax.set_yticks(self.y_ticks[self.y_ticks != 0])

root = Tk()
Application(root)
