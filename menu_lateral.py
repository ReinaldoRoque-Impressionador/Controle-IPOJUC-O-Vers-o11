#importação após reestruturação do projeto
from recursos import aba_itau

from modulos.abas.aba_login_fusion import chamar_aba_login_fusion
from modulos.abas.aba_cadastro import chamar_aba_cadastro
from modulos.abas.aba_financeiro import chamar_aba_financeiro
from modulos.abas.aba_clientes import chamar_aba_clientes
from modulos.abas.aba_consulta import chamar_aba_consulta
from modulos.abas.aba_relatorios import chamar_aba_relatorios
from modulos.abas.aba_clima import chamar_aba_clima
from modulos.recursos.aba_itau import chamar_aba_itau
#importações após reestruturação do projeto



def menu_lateral(frame_principal):
    menu = tk.Frame(frame_principal, bg="gray", width=200)
    menu.pack(side="left", fill="y")

    ttk.Button(menu, text="Login", command=chamar_aba_login_fusion).pack(pady=5)
    ttk.Button(menu, text="Cadastro", command=chamar_aba_cadastro).pack(pady=5)
    ttk.Button(menu, text="Financeiro", command=chamar_aba_financeiro).pack(pady=5)
    ttk.Button(menu, text="Clientes", command=chamar_aba_clientes).pack(pady=5)
    ttk.Button(menu, text="Consulta", command=chamar_aba_consulta).pack(pady=5)
    ttk.Button(menu, text="Relatórios", command=chamar_aba_relatorios).pack(pady=5)
    ttk.Button(menu, text="Clima", command=chamar_aba_clima).pack(pady=5)
    ttk.Button(menu, text="Itaú", command=chamar_aba_itau).pack(pady=5)
    # etc...