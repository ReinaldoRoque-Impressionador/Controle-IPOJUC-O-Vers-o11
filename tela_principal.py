# tela_principal.py

import tkinter as tk
from recursos.som_expressao import som_e_expressao_acao
from PIL import Image, ImageTk
import os


import tkinter as tk
from tkinter import ttk
from modulos.abas.aba_clientes import montar_aba_clientes
# outras abas...


def criar_tela_principal(notebook):
    frame = ttk.Frame(notebook)



def criar_interface():
    root = tk.Tk()
    root.title("Sistema Principal")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    aba_clientes = ttk.Frame(notebook)
    notebook.add(aba_clientes, text="Clientes")
    montar_aba_clientes(aba_clientes, inner_frame=None)

    # outras abas...

    root.mainloop()

if __name__ == "__main__":
    criar_interface()

def caminho_imagem(nome):
    base = os.path.dirname(os.path.dirname(__file__))
    return os.path.join(base, "imagensipojucao", "imagens", nome)

def abrir_janela_principal(nome, perfil):
    janela = tk.Toplevel()
    janela.title(f"Bem-vindo, {nome} ({perfil})")
    janela.geometry("400x450")

    # 🐶 Carrega imagem inicial do mascote
    caminho_img_inicial = os.path.join(os.path.dirname(__file__), "imagens", "mascote_normal.png")
    #imagem = Image.open(caminho_img_inicial).resize((150, 150))
    imagem = Image.open(caminho_imagem("mascote_feliz.png")).resize((150, 150))
    imagem_tk = ImageTk.PhotoImage(imagem)

    print("Caminho mascote:", caminho_imagem("mascote_feliz.png"))
    print("Existe?", os.path.exists(caminho_imagem("mascote_feliz.png")))

    # 📌 Label que será atualizado com expressões
    label_mascote = tk.Label(janela, image=imagem_tk)
    label_mascote.image = imagem_tk
    label_mascote.pack(pady=10)

    # 👤 Informações do usuário
    label_usuario = tk.Label(janela, text=f"Usuário: {nome}\nPerfil: {perfil}", font=("Arial", 12))
    label_usuario.pack(pady=5)

    # 🔘 Botões para testar reações
    acoes = ["salvar", "editar", "excluir", "buscar"]
    for acao in acoes:
        botao = tk.Button(
            janela,
            text=acao.capitalize(),
            width=20,
            command=lambda ac=acao: som_e_expressao_acao(ac, label_mascote, janela)
        )
        botao.pack(pady=5)

    janela.protocol("WM_DELETE_WINDOW", janela.destroy)



def chamar_tela_principal(notebook):
    frame = criar_tela_principal(notebook)
    notebook.add(frame, text="Cadastro")



