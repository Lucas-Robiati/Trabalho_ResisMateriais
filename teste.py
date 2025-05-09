import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

def criar_combobox_com_imagem(janela, valores, caminho_imagem):
    # Crie uma variável para armazenar o valor selecionado
    valor_selecionado = tk.StringVar()

    # Carregue a imagem e ajuste o tamanho
    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((20, 20)) # Ajuste as dimensões conforme necessário
    imagem = ImageTk.PhotoImage(imagem)

    # Crie uma combobox personalizada com um label para exibir a imagem
    def mostrar_imagem(valor_selecionado):
        label_imagem.configure(image=imagem)
        label_imagem.image = imagem # Manter a imagem na memória

    combobox = ttk.Combobox(janela, textvariable=valor_selecionado, values=valores)
    combobox.bind("<<ComboboxSelected>>", lambda event: mostrar_imagem(combobox.get()))

    # Crie um label para exibir a imagem (pode ser oculto quando não estiver selecionado)
    label_imagem = tk.Label(janela, image=imagem)
    label_imagem.image = imagem  # Manter a imagem na memória

    # Posicione os widgets
    combobox.pack(pady=5)
    label_imagem.pack(pady=5)

    # Defina o valor inicial
    combobox.current(0)

    return combobox

# Exemplo de Uso:
if __name__ == "__main__":
    janela = tk.Tk()
    janela.title("Combobox com Imagem")

    valores_combobox = ["Opção 1", "Opção 2", "Opção 3"]
    caminho_imagem = "Assets/Quadrante0.png" # Substitua pelo caminho da sua imagem

    # Crie a combobox personalizada
    combobox = criar_combobox_com_imagem(janela, valores_combobox, caminho_imagem)

    janela.mainloop()
