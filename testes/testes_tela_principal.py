
# import tkinter as tk
# from recursos.som_expressao import som_e_expressao_acao
# from PIL import Image, ImageTk
# import os




# # tela_principal.py
#
# import tkinter as tk
# from modulos.som_expressao import som_e_expressao_acao
# from PIL import Image, ImageTk
# import os
# from tkinter import ttk
# from tkinter import ttk
# from modulos.utilitarios import caminho_arquivo
#
# from modulos import dados_compartilhados as dc
#
#
# def criar_interface():
#     janela = tk.Tk()
#     janela.title("Mascote Interativo")
#     janela.geometry("400x400")
#
#     # 🐶 Carrega imagem inicial do mascote
#     caminho_img_inicial = os.path.join(os.path.dirname(__file__), "imagens", "mascote_normal.png")
#     imagem = Image.open(caminho_img_inicial).resize((150, 150))
#     imagem_tk = ImageTk.PhotoImage(imagem)
#
#     # 📌 Label que será atualizado com expressões
#     label_mascote = tk.Label(janela, image=imagem_tk)
#     label_mascote.image = imagem_tk
#     label_mascote.pack(pady=10)
#
#     # 🔘 Botões para testar reações
#     acoes = ["salvar", "editar", "excluir", "buscar"]
#     for acao in acoes:
#         botao = tk.Button(
#             janela,
#             text=acao.capitalize(),
#             width=20,
#             command=lambda ac=acao: som_e_expressao_acao(ac, label_mascote, janela)
#         )
#         botao.pack(pady=5)
#
#     janela.mainloop()
#
# # 🚀 Executa a interface
# if __name__ == "__main__":
#     criar_interface()