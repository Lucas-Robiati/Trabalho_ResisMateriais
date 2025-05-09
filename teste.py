import tkinter as tk
import tkinter.ttk as ttk

# Cria a janela e a Treeview
janela = tk.Tk()
tree = ttk.Treeview(janela, columns=("Coluna 1", "Coluna 2", "Coluna 3"))
tree.heading("#0", text="Coluna 1")
tree.heading("Coluna 1", text="Coluna 1")
tree.heading("Coluna 2", text="Coluna 2")
tree.heading("Coluna 3", text="Coluna 3")
tree.pack()

# Adiciona alguns dados de exemplo
tree.insert("", "end", iid="item1", text="Item 1", values=("Valor 1", "Valor 2", "Valor 3"))
tree.insert("", "end", iid="item2", text="Item 2", values=("Outro Valor 1", "Outro Valor 2", "Outro Valor 3"))

# Função para obter informações do item selecionado
def obter_informacoes():
    # Obtém o item selecionado
    selecionado = tree.selection()

    # Verifica se houve uma seleção
    if selecionado:
        # Obtém o iid do item selecionado
        iid = selecionado[0]

        # Obtém os valores dos campos do item selecionado
        valores = tree.item(iid, "values")

        # Imprime os valores
        print(f"Item Selecionado: {iid}")
        print(f"Coluna 1: {valores[0]}")
        print(f"Coluna 2: {valores[1]}")
        print(f"Coluna 3: {valores[2]}")
    else:
        print("Nenhum item selecionado.")

# Adiciona um botão para chamar a função
botao = tk.Button(janela, text="Obter Informações", command=obter_informacoes)
botao.pack()

# Inicia o loop da janela
janela.mainloop()
