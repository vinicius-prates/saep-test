from tkinter import *
from tkinter import ttk
# from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error



###Função para criar conexão com o BD
def ConectaBanco():
    caminho="BD_P3_Import.db"
    conectado=None
    try:
        conectado=sqlite3.connect(caminho)
    except Error as msg_erro:
        print(msg_erro)
    return conectado

conect = ConectaBanco()
### Fim da Função para criar conexão com o BD





### Criação e posicionamento da tela Principal
tela_principal = Tk()
tela_principal.title('VEICULOS A VENDA NOS PATIOS EM AZUL')

C = Canvas(tela_principal, bg="white",
           height=800, width=1200)


### Demarcando áreas da planta na tela
#Area_1
area_1 = C.create_rectangle((450,260), (750,550),fill="white")
text_1 = C.create_text(600, 410, text='1', fill='black', font=('Arial', 20, 'bold'))

#Area_2
area_2 = C.create_rectangle((200, 600), (1050, 780),fill="white")
text_2 = C.create_text(625, 700, text='2', fill='black', font=('Arial', 20, 'bold'))

#Area_3
area_3 = C.create_rectangle((200, 450), (300, 580),fill="white")
text_3 = C.create_text(250, 515, text='3', fill='black', font=('Arial', 20, 'bold'))

#Area_4
area_4 = C.create_rectangle((800, 300), (900, 500),fill="white")
text_4 = C.create_text(850, 400, text='4', fill='black', font=('Arial', 20, 'bold'))

#Area_5
area_5 = C.create_rectangle((650, 10), (850, 280),fill="white")
text_5 = C.create_text(750, 165, text='5', fill='black', font=('Arial', 20, 'bold'))

#Area_6
area_6 = C.create_rectangle((650, 10), (800, 100),fill="white")
text_6 = C.create_text(725, 55, text='6', fill='black', font=('Arial', 20, 'bold'))


# Inclinação Usar referencia ao Triangulo pitagorico 3-4-5
# onde h=2,4

#Area_7 Inclinado
# Para Fazer umPoligono Transparente outline='black', fill='', width=1.  Caso nao coloque os parametros gerará um poligone preenchido
area_7 = C.create_polygon((220,80), (240,20), (360, 60),(340, 120), outline='black', fill='', width=1)
text_7 = C.create_text(290, 80, text='7', fill='black', font=('Arial', 20, 'bold'))


#Area_8 Inclinado
area_8 = C.create_polygon((1000,100), (1036,52), (1164, 148),(1128, 196), outline='black', fill='', width=1)
text_8 = C.create_text(1074, 120, text='8', fill='black', font=('Arial', 20, 'bold'))

#Area_9 Inclinado
area_9 = C.create_polygon((1000,300), (1036,252), (1164, 348),(1128, 396), outline='black', fill='', width=1)
text_9 = C.create_text(1074, 320, text='9', fill='black', font=('Arial', 20, 'bold'))

#Area_10 Inclinado
area_10 = C.create_polygon((1000,500), (1036,452), (1164, 548),(1128, 596), outline='black', fill='', width=1)
text_10 = C.create_text(1074, 525, text='10', fill='black', font=('Arial', 20, 'bold'))

#Area_11 Inclinado
area_11 = C.create_polygon((200,100), (570,220), (480, 480),(100, 330), outline='black', fill='', width=1)
text_11 = C.create_text(340, 270, text='11', fill='black', font=('Arial', 20, 'bold'))
#poligono = C.create_polygon((200,100), (570,220), (480, 480),(100, 300),fill="black")

### FIM de Demarcando áreas da planta na tela




### Função chamada no carregamento da tela principal
def pinta_tela_principal(area):
    if area == 1:
        ar_1 = C.create_rectangle((450, 260), (750, 550), fill="blue")
        te_1 = C.create_text(600, 410, text='1', fill='white', font=('Arial', 20, 'bold'))
    elif area == 2:
        area_2 = C.create_rectangle((200, 600), (1050, 780), fill="blue")
        text_2 = C.create_text(625, 700, text='2', fill='white', font=('Arial', 20, 'bold'))

    elif area == 3:
        area_3 = C.create_rectangle((200, 450), (300, 580), fill="blue")
        text_3 = C.create_text(250, 515, text='3', fill='white', font=('Arial', 20, 'bold'))

    elif area == 4:
        area_4 = C.create_rectangle((800, 300), (900, 500), fill="blue")
        text_4 = C.create_text(850, 400, text='4', fill='white', font=('Arial', 20, 'bold'))

    elif area == 5:
        area_5 = C.create_rectangle((650, 10), (850, 280), fill="blue")
        text_5 = C.create_text(750, 165, text='5', fill='white', font=('Arial', 20, 'bold'))

    elif area == 6:
        area_6 = C.create_rectangle((650, 10), (800, 100), fill="blue")
        text_6 = C.create_text(725, 55, text='6', fill='white', font=('Arial', 20, 'bold'))

    elif area == 7:
        area_7 = C.create_polygon((220, 80), (240, 20), (360, 60), (340, 120), outline='black', fill='blue', width=1)
        text_7 = C.create_text(290, 80, text='7', fill='white', font=('Arial', 20, 'bold'))

    elif area == 8:
        area_8 = C.create_polygon((1000, 100), (1036, 52), (1164, 148), (1128, 196), outline='black', fill='blue', width=1)
        text_8 = C.create_text(1074, 120, text='8', fill='white', font=('Arial', 20, 'bold'))

    elif area == 9:
        area_9 = C.create_polygon((1000, 300), (1036, 252), (1164, 348), (1128, 396), outline='black', fill='blue', width=1)
        text_9 = C.create_text(1074, 320, text='9', fill='white', font=('Arial', 20, 'bold'))

    elif area == 10:
        area_10 = C.create_polygon((1000, 500), (1036, 452), (1164, 548), (1128, 596), outline='black', fill='blue', width=1)
        text_10 = C.create_text(1074, 525, text='10', fill='white', font=('Arial', 20, 'bold'))

    elif area == 11:
        area_11 = C.create_polygon((200, 100), (570, 220), (480, 480), (100, 330), outline='black', fill='blue', width=1)
        text_11 = C.create_text(340, 270, text='11', fill='white', font=('Arial', 20, 'bold'))

### FIM da Função chamada no carregamento da tela principal


# Montamos aqui nossa instrução SQL. 3 Aspas para abrir e fechar é para que suporte descrever em varias linhas
# Não usamos no código. É apenas para usar em uma consulta para se ambientar com o modelo
inst_sql_tudo = """
Select automoveis.modelo, concessionarias.concessionária, alocacao.* 
from automoveis, concessionarias, alocacao 
where alocacao.automovel = automoveis.id 
and alocacao.concessionária = concessionarias.id order by area, modelo, concessionária
"""

inst_sql_distinct_area = """
Select DISTINCT alocacao.area from alocacao where alocacao.quantidade > 0
"""

# Modo 1 - Usado no carregamento da ComboBox da Tela de Venda
def Consulta_BD(conexao, sql):
    i=conexao.cursor()
    i.execute(sql)
    resposta = []
    for row in i.fetchall():
        resposta.append(row[0])
    return resposta
    #print("Consulta Realizada com Sucesso")


# Modo 2 - Usado no carregamento da tela principal e do TreeView da tela de detalhe
def Consulta_BD_V2(conexao, sql):
    i=conexao.cursor()
    i.execute(sql)
    resposta=i.fetchall()
    return resposta
    #print("Consulta Realizada com Sucesso")


def Atualiza_BD(conexao, sql):
    s=conexao.cursor()
    s.execute(sql)
    conexao.commit()



#dados receberá o resultado da consulta que retorna uma tupla
dados=Consulta_BD_V2(conect, inst_sql_distinct_area)
for r in dados:
    #print(r)
    pinta_tela_principal(r[0])

def cmd_click_venda(area):
    try:
        selecionado = tv.focus()
        temp = tv.item(selecionado, 'values')
        #print(temp[0])
        tela_venda(temp[0],area)

    except:
         messagebox.showinfo(title="OPS", message="Selecione um item da lista para ser vendido")


def tela_detalhe(area):
    global tela_detalheX
    tela_detalheX = Toplevel()
    tela_detalheX.title('VEICULOS DISPONIVEIS PARA ESSA AREA')
    tela_detalheX.geometry('1200x800+100+10')
    tela_detalheX.transient(tela_principal)
    tela_detalheX.focus_force()
    tela_detalheX.grab_set()

    lbl_area = Label(tela_detalheX, text="Área " + str(area), fg="black", font=('Arial', 40))
    lbl_area.pack()
    lbl_area.place(bordermode=OUTSIDE, height=250, width=220, x=200, y=10)

    global tv

    tv = ttk.Treeview(tela_detalheX, selectmode='browse', columns=('modelo','preco'), show='headings')
    tv.column('modelo', width=450)
    tv.column('preco', width=300)
    tv.heading('modelo', text='MODELO')
    tv.heading('preco', text='PREÇO')
    tv.pack()
    tv.place(height=300, width=760, x=200, y=200)
    inst_sql_venda = "Select automoveis.modelo, automoveis.preço "
    inst_sql_venda = inst_sql_venda + "from automoveis, concessionarias, alocacao "
    inst_sql_venda = inst_sql_venda + "where area = " + str(area)
    inst_sql_venda = inst_sql_venda + " and alocacao.automovel = automoveis.id "
    inst_sql_venda = inst_sql_venda + "and alocacao.concessionária = concessionarias.id "
    inst_sql_venda = inst_sql_venda + "order by modelo"
    #dados_grid=Consulta_BD(conect, inst_sql_venda)
    dados_grid = Consulta_BD_V2(conect, inst_sql_venda)
    for m in dados_grid:
        tv.insert("","end", values=m)



    #cmd_vender = Button(tela_detalhe, text='Vender', command=lambda: cmd_click_venda(item_Selecionado), font=('Arial', 30))
    cmd_vender = Button(tela_detalheX, text='Vender', command=lambda: cmd_click_venda(area), font=('Arial', 30))
    cmd_vender.pack()  # faz o botão aparecer na tela
    cmd_vender.place(bordermode=OUTSIDE, height=60, width=180, x=500, y=600)

    # lbl_area.grid(row=0, column=0)
    # tv.grid(row=1, column=0)
    # cmd_vender.grid(row=1, column=2)


def tela_venda(modelo,area):

    global cb_cliente
    global cbb_conc

    telavenda = Toplevel()
    telavenda.title('VENDENDO DO PATIO')
    telavenda.geometry('800x400+450+280')
    telavenda.focus_force()
    telavenda.grab_set()

    lbl_area = Label(telavenda, text=modelo, fg="black", font=('Arial', 20))
    lbl_cliente = Label(telavenda, text="Cliente ", fg="black", font=('Arial', 15))
    lbl_concessionaria = Label(telavenda, text="Concessionaria ", fg="black", font=('Arial', 15))



    inst_sql_cliente = "Select clientes.Nome from clientes"


    #A linha abaixo acrescenta Apostrofe a varival modelo para compor a instrucao SQL
    modelo = "'" + modelo + "'"

    #print(modelo)

    cb_cliente = ttk.Combobox(telavenda, width=60)
    cb_cliente['values'] = Consulta_BD(conect, inst_sql_cliente)

    inst_sql_concessionaria = "Select concessionarias.concessionária"
    inst_sql_concessionaria = inst_sql_concessionaria + " from alocacao, concessionarias, automoveis "
    inst_sql_concessionaria = inst_sql_concessionaria + "where automoveis.modelo = " + modelo
    inst_sql_concessionaria = inst_sql_concessionaria + " and alocacao.automovel = automoveis.id"
    inst_sql_concessionaria = inst_sql_concessionaria + " and concessionarias.id = alocacao.concessionária "
    inst_sql_concessionaria = inst_sql_concessionaria + " and area = " + str(area)
    inst_sql_concessionaria = inst_sql_concessionaria + " and alocacao.quantidade > 0"
    #dados_combo_conc = Consulta_BD_V2(conect, inst_sql_concessionaria)

    cbb_conc = ttk.Combobox(telavenda, width=60)
    cbb_conc['values']= Consulta_BD(conect, inst_sql_concessionaria)

    cmd_confirmar = Button(telavenda, text='Confirmar', command=lambda: cmd_click_confirmar(modelo, area) , font=('Arial', 30))


    lbl_area.grid(row=2, column=1)
    lbl_cliente.grid(row=6, column=1)
    lbl_concessionaria.grid(row=10, column=1)
    cb_cliente.grid(row=6, column=2)
    cbb_conc.grid(row=10, column=2)
    cmd_confirmar.grid(row=16, column=2)


def cmd_click_confirmar(modelo, area):

    if (cb_cliente.get()) == "" or (cbb_conc.get()) == "":

        messagebox.showinfo(title="OPS", message="Selecione o Cliente e a Concessionária")

    else:

        print(cb_cliente.get())
        print(cbb_conc.get())
        print(modelo)
        print(area)


        inst_sql_alocacao =  "Select alocacao.id "
        inst_sql_alocacao = inst_sql_alocacao + "from alocacao, automoveis, concessionarias where "
        inst_sql_alocacao = inst_sql_alocacao + "automoveis.modelo = " + modelo
        inst_sql_alocacao = inst_sql_alocacao + " and automoveis.id = alocacao.automovel "
        inst_sql_alocacao = inst_sql_alocacao + " and concessionarias.concessionária = '" + cbb_conc.get()
        inst_sql_alocacao = inst_sql_alocacao + "' and alocacao.area = " + str(area)

        linha_alocacao_atualizar = Consulta_BD(conect, inst_sql_alocacao)

        print(linha_alocacao_atualizar[0])

        inst_sql_update_qtde = "UPDATE alocacao SET quantidade = quantidade - 1 where "
        inst_sql_update_qtde = inst_sql_update_qtde + "id = " + str(linha_alocacao_atualizar[0])
        # (Select alocacao.quantidade "
        # inst_sql_update_qtde = inst_sql_update_qtde + "from alocacao, automoveis, concessionarias where "
        # inst_sql_update_qtde = inst_sql_update_qtde + "automoveis.modelo = " + modelo
        # inst_sql_update_qtde = inst_sql_update_qtde + " and automoveis.id = alocacao.automovel "
        # inst_sql_update_qtde = inst_sql_update_qtde + " and concessionarias.concessionária = '" + cbb_conc.get()
        # inst_sql_update_qtde = inst_sql_update_qtde + "' and alocacao.area = " + str(area) + ")"
        print(inst_sql_update_qtde)



        try:

             Atualiza_BD(conect, inst_sql_update_qtde)
             messagebox.showinfo(title="VENDA FINALIZADA", message="Venda Finalizada com sucesso")

        except:

             messagebox.showinfo(title="OPS!", message="Algua coisa não saiu como esperado. Contate o SAC.")



def click_esquerdo(event):
    # Area_1
    if event.x >= 450 and event.x <= 750 and event.y >= 260 and event.y <= 550:
        tela_detalhe(1)

    # Area_2
    elif event.x >= 200 and event.x <= 1050 and event.y >= 600 and event.y <= 780:
        tela_detalhe(2)

    # Area_3
    elif event.x >= 200 and event.x <= 300 and event.y >= 450 and event.y <= 580:
        tela_detalhe(3)

    # Area_4
    elif event.x >= 800 and event.x <= 900 and event.y >= 300 and event.y <= 500:
        tela_detalhe(4)

    # Area_5 e Area_6
    elif event.x >= 650 and event.x <= 850 and event.y >= 10 and event.y <= 280:
        if event.x >= 650 and event.x <= 800 and event.y >= 10 and event.y <= 100:
            tela_detalhe(6)
        else:
            tela_detalhe(5)

    # Area_7
    elif event.x >= 220 and event.x <= 360 and event.y >= 20 and event.y <= 120:
         tela_detalhe(7)

    # Area_8
    elif event.x >= 1000 and event.x <= 1164 and event.y >= 52 and event.y <= 196:
        tela_detalhe(8)

    # Area_9
    elif event.x >= 1000 and event.x <= 1164 and event.y >= 252 and event.y <= 396:
        tela_detalhe(9)

    # Area_10
    elif event.x >= 1000 and event.x <= 1164 and event.y >= 452 and event.y <= 548:
        tela_detalhe(10)

    # Area_11
    elif event.x >= 100 and event.x <= 570 and event.y >= 100 and event.y <= 480:
        tela_detalhe(11)



tela_principal.bind("<Button-1>", click_esquerdo)

C.pack()
tela_principal.mainloop()
