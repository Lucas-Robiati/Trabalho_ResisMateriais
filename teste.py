import tkinter as tk
from tkinter import ttk

root = tk.Tk()
# Criar a Treeview
tree = ttk.Treeview(root)  # Certifique-se de ter um 'root' (janela)
tree.pack(pady=10)

# Definir colunas (exemplo)
tree["columns"] = ("Col1", "Col2", "Col3")  # Use o nome das colunas que deseja alterar
tree.column("#0", width=50)  # Largura da coluna de identificação
tree.column("Col1", width=100)
tree.column("Col2", width=150)
tree.column("Col3", width=100)

# Definir cabeçalhos
tree.heading("#0", text="ID")
tree.heading("Col1", text="Col1")
tree.heading("Col2", text="Col2")
tree.heading("Col3", text="Col3")

# Adicionar um item (exemplo)
item_id = tree.insert("", "end", text="1", values=("Valor1", "Valor2", "Valor3"))

print(item_id)

# Alterar o valor em uma coluna (exemplo)
tree.item(item_id, values=("Novo Valor 1", "Valor2", "Novo Valor 3")) # A coluna 0 é alterada (o texto da linha)
# Ou, se quiser mudar uma coluna específica:
# tree.item(item_id, text="Novo Texto da Linha") # Mudar o texto da linha

# Exibir a Treeview
root.mainloop()
