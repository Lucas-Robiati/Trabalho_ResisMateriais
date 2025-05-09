from Modules import *

class Application(Validate):
  def __init__(self, root:'Tk'):
    self.root = root                            # Define o bejeto Tk que será usado como janela principal
    self.composite_figure =  ICCompositeFigure()     # Lista de Obejetos
    self.dict_shapes = {}
    self.system_origin = ICPoint2D()            # Variavel que define a origem do sistema
    self.window()                               # Cria a janela principal sub janelas e widgets
    root.mainloop()                             # Loop da janela

  @property
  def x_min(self) -> float:
    return self.__x_min

  @x_min.setter
  def x_min(self, x_min) -> None:
    self.x_min = min(self.x_min, x_min)

  @property
  def x_max(self) -> float:
    return self.__x_max

  @x_min.setter
  def x_max(self, x_max) -> None:
    self.x_max = max(self.x_max, x_max)

  @property
  def y_min(self) -> float:
    return self.__y_min

  @y_min.setter
  def y_min(self, y_min) -> None:
    self.y_min = min(self.y_min, y_min)

  @property
  def y_max(self) -> float:
    return self.__y_max

  @y_max.setter
  def y_max(self, y_max) -> None:
    self.y_max = max(self.y_max, y_max)

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
    self.__x_min, self.__x_max, self.__y_min, self.__y_max = -5, 5, -5, 5
    self.ticks_frequency = 1  # Valor inicial, será ajustado dinamicamente

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
      command= self.destroy_insert_window,
      activebackground= Color.white.value,
      activeforeground= Color.black.value,
      bg= Color.gray.value,
      fg= Color.white.value
      )
    self.bt_quit.place(relx=0.55, rely=0.9, relwidth=0.25, relheight=0.08)

  def destroy_insert_window(self):
    self.insert.destroy()

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
        
        else:
          entry_validate = float(self.coordinate_center_x_entry.get())
          entry_validate = float(self.coordinate_center_y_entry.get())
          entry_validate = float(self.dimensions_a_px_entry.get())
          if(self.geometric_form_entry.get() == "Retangulo"):
            entry_validate = float(self.dimensions_b_px_entry.get())
                  
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
      new_form =  ICCircle(radius=float(self.dimensions_a_px_entry.get()),  centroid=ICPoint2D(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)
      
      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form
        
    if(self.geometric_form_entry.get() == "Semicirculo"):
      new_form = ICSemicircle(radius=float(self.dimensions_a_px_entry.get()), origin=ICPoint2D(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)

      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form

    if(self.geometric_form_entry.get() == "Quadrante"):
      new_form = ICQuadrant(radius=float(self.dimensions_a_px_entry.get()), origin=ICPoint2D(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)
      
      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form

    if(self.geometric_form_entry.get() == "Retangulo"):
      new_form = ICRectangle(width=float(self.dimensions_a_px_entry.get()), height=float(self.dimensions_b_px_entry.get()), centroid=ICPoint2D(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), system_origin=self.system_origin, virtual_form=self.verify_subare())
      self.composite_figure.append(new_form)
      
      self.treeview_list.insert(parent='', index='end', iid=count, 
        text=self.geometric_form_entry.get(), values=(self.coordinate_center_x_entry.get(),self.coordinate_center_y_entry.get(),self.subare_entry.get()))
      count += 1
      return new_form
  
  # Adiciona as figuras do MatPlotLib
  def add_figure_matplotlib(self) -> None:
    if(self.verify_subare()):
      subarea = 2     # Subtrair (Fica a frente)
      edgeclr='black' # Cor da borda
      faceclr='white' # Cor de preenchimento
    else:
      subarea = 1     # Adicionar (Fica atras)
      edgeclr='black' # Borda
      faceclr='blue'  # Preenchimento

    figure = None
    form = self.geometric_form_entry.get()

    if(form == "Triangulo"):
      points = [(float(self.dimensions_a_px_entry.get()), float(self.dimensions_a_py_entry.get())),  # Ponto A Vértices (x, y)
                (float(self.dimensions_b_px_entry.get()), float(self.dimensions_b_py_entry.get())),  # Ponto B Vértices (x, y)
                (float(self.dimensions_c_px_entry.get()), float(self.dimensions_c_py_entry.get()))   # Ponto C Vértices (x, y)
      ]

      figure = Polygon(
        xy = points,               # Pontos do Triangulo
        closed = True,             # Fechar o polígono
        edgecolor = edgeclr,       # Cor da borda
        facecolor = faceclr,       # Cor de preenchimento
        zorder = subarea           # Ordem
      )

      self.x_min = [p[0] for p in points] # Reajustando limite inferior em X caso a figura ultrapasse
      self.x_max = [p[0] for p in points] # Reajustando limite superior em X caso a figura ultrapasse
      self.y_max = [p[1] for p in points] # Reajustando limite inferior em Y caso a figura ultrapasse
      self.y_min = [p[1] for p in points] # Reajustando limite superior em Y caso a figura ultrapasse

    if(form == "Circunferencia"):
      origin = [(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get()))]
      rad = float(self.dimensions_a_px_entry.get())

      figure = Circle(
        xy = origin,          # Centro do círculo
        radius = rad,         # Raio
        edgecolor = edgeclr,  # Cor da borda
        facecolor = faceclr,  # Cor de preenchimento
        zorder = subarea      # Ordem
      )

    if(form == "Semicirculo"):
      origin = [(float(self.coordinate_center_x_entry.get()), float(self.coordinate_center_y_entry.get()))]
      r = float(self.dimensions_a_px_entry.get())

      figure = Wedge(
        center = origin,      # Centro do círculo
        radius = rad,         # Raio
        theta1=0,             # Ângulo inicial (graus)
        theta2=180,           # Ângulo final (graus)
        edgecolor = edgeclr,  # Cor da borda
        facecolor = faceclr,  # Cor de preenchimento
        zorder = subarea      # Ordem
      )
      """
        situações de orientação meio_circulo
        orientação 0: 0-180
        orientação 1: 90-270
        orientação 2: 180-0
        orientacao 3: 270-90
      """
    
    if(form == "Quadrante"):
      figure = Wedge(
        center=(float(self.coordinate_center_x_entry.get()),float(self.coordinate_center_y_entry.get())), # Centro
        r=float(self.dimensions_a_px_entry.get()),               # Raio
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

    if(form == "Retangulo"):
      figure = Rectangle(
        xy=((float(self.coordinate_center_x_entry.get()) - (float(self.dimensions_a_px_entry.get()) / 2)),
            (float(self.coordinate_center_y_entry.get()) - (float(self.dimensions_b_px_entry.get()) / 2))),       # Canto inferior esquerdo
        width=float(self.dimensions_a_px_entry.get()),           # Largura
        height=float(self.dimensions_b_px_entry.get()),          # Altura
        edgecolor=edgeclr, # Borda
        facecolor=faceclr,  # Preenchimento
        zorder=subarea           # Ordem
      )

    plt.gca().add_patch(figure)
    self.auto_resize_matplotlib()
    plt.draw()
    return figure

  # Remove as formas da tabela e da lista de objetos
  def remove_item(self):
    select = self.treeview_list.selection()[0]
    if(select):
      index = self.treeview_list.index(select)
      self.treeview_list.delete(select)
      figure = self.dict_shapes[self.composite_figure.components[index]]
      figure.remove()
      self.dict_shapes.pop(self.composite_figure.components[index])            
      self.composite_figure.drop(index)

      plt.draw()

  # Modifica valores nos objetos
  def modify_object(self) -> None:
    return None

  def select_form(self, event):
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

    if((self.geometric_form_entry.get() == "Circunferencia")):
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
      
      self.label_coordinates_center.config(text="Coordenada do centróide")
      self.label_coordinates_center.place(relx=0.005, rely=0.5)
      self.coordinate_center_x_entry.place(relx=0.005, rely=0.545, relwidth=0.95, relheight=0.05)
      self.coordinate_center_y_entry.place(relx=0.005, rely=0.61, relwidth=0.95, relheight=0.05)

    if((self.geometric_form_entry.get() == "Semicirculo")or
        (self.geometric_form_entry.get() == "Quadrante")):
      
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
      
      self.label_coordinates_center.config(text="Origem")
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
  
  def on_resize(self, event):
    if (event.width <= 950 and event.height <= 520):
      self.coordinate_x_entry.place(relx=0.33, rely=0.58, relwidth=0.25, relheight=0.05)
      self.coordinate_y_entry.place(relx=0.6, rely=0.58, relwidth=0.25, relheight=0.05)
    else:
      self.coordinate_x_entry.place(relx=0.23, rely=0.58, relwidth=0.3, relheight=0.04)
      self.coordinate_y_entry.place(relx=0.55, rely=0.58, relwidth=0.3, relheight=0.04)
  
  def auto_resize_matplotlib(self):
    # Calcular frequência dos ticks baseada no range
    x_padded_range = (self.x_max + 1) - (self.x_min - 1)
    y_padded_range = (self.y_max + 1) - (self.y_min - 1)
    
    self.ticks_frequency_x = max(1, int(round(x_padded_range / 10)))
    self.ticks_frequency_y = max(1, int(round(y_padded_range / 10)))

    # Aplicar limites e ticks
    self.ax.set(xlim=(self.x_min - 1, self.x_max + 1), 
                ylim=(self.y_min - 1, self.y_max + 1), 
                aspect='equal')
    
    x_ticks = np.arange(self.x_min - 1, self.x_max + 1 + self.ticks_frequency_x, self.ticks_frequency_x)
    y_ticks = np.arange(self.y_min - 1, self.y_max + 1 + self.ticks_frequency_y, self.ticks_frequency_y)
    
    self.ax.set_xticks([x for x in x_ticks if x != 0])
    self.ax.set_yticks([y for y in y_ticks if y != 0])
    plt.draw()

root = Tk()
Application(root)
