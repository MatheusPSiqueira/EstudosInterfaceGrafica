from tkinter import *
from conta1 import Conta1


janela = Tk()
janela.title('Banco')
janela.geometry('500x500+400+100')
janela.configure(background='Azure1')


def informacoes():
    global janela_info
    global operacao
    global saldo1
    global cliente

    janela_info = Tk()
    janela_info.title('Banco')
    janela_info.geometry('500x500+400+100')
    janela_info.configure(background='Azure1')

    Label(janela_info, text='Suas Informações', font='Arial 18', background='PaleTurquoise1').pack(side=TOP, fill=X)

    try:
        saldo1 = float(saldo.get())
    except:
        janela_info.destroy()
        janela_erro = Tk()
        janela_erro.title('Erro')
        janela_erro.geometry('300x100+400+100')
        janela_erro.configure(background='black')
        Label(janela_erro, text='ERRO', background='grey', fg='red', font='Arial 18 bold').pack(side=TOP, fill=X)
        Label(janela_erro, text='❌ Por favor, insira um valor de saldo válido', font='Arial 10 bold', fg='red', background='black').place(x=6, y=45)

    info_nome = Label(janela_info, background='Azure1')
    info_nome.place(x=10, y=60)
    info_nome['text'] = 'Nome: '+nome.get()

    info_cpf = Label(janela_info, background='Azure1')
    info_cpf.place(x=10, y=80)
    info_cpf['text'] = 'CPF: ' + cpf.get()

    info_idade = Label(janela_info, background='Azure1')
    info_idade.place(x=10, y=100)
    info_idade['text'] = 'Idade: ' + idade.get()

    info_saldo = Label(janela_info, background='Azure1')
    info_saldo.place(x=10, y=120)
    info_saldo['text'] = 'Saldo: R$' + str(saldo1)

    janela.destroy()

    Label(janela_info, text='Deseja fazer alguma operação?', background='Azure1', font='Arial 13').place(x=10, y=170)

    bt_sim = Button(janela_info, text='Sim', background='LightBlue1', command=op_sim)
    bt_sim.place(x=20, y=200)

    bt_nao = Button(janela_info, text='Não', background='LightBlue1', command=op_nao)
    bt_nao.place(x=80, y=200)

    cliente = Conta1(saldo1, 1000)


def cria_conta():
    global saldo
    global saldo1

    Label(janela, text='', background='PaleTurquoise1').place(x=0, y=320, width=500)
    Label(janela, text='Crie sua conta', font='Arial 15', background='Azure1').place(x=80, y=350)
    Label(janela, text='Sua conta terá um limite inicial de R$ 1000,00', background='Azure1').place(x=10, y=380)
    Label(janela, text='Informe o saldo que deseja iniciar sua conta', background='Azure1').place(x=10, y=400)
    Label(janela, text='R$', background='Azure1').place(x=10, y=425)

    Button(janela, text='Finalizar', command=informacoes, background='LightBlue1').place(x=353, y=425)

    saldo = Entry(janela, background='LightCyan')
    saldo.place(height=20, width=45, x=30, y=425)


def cadastro():
    global nome
    global cpf
    global idade

    Label(janela, text='', background='PaleTurquoise1').place(x=0, y=115, width=500)
    Label(janela, text='Cadastro do Cliente', font='Arial 15', background='Azure1').place(x=80, y=150)
    Label(janela, text='Digite seu nome completo: ', background='Azure1').place(x=10, y=180)
    nome = Entry(janela, background='LightCyan')
    nome.place(height=20, width=400, x=10, y=200)

    Label(janela, text='Digite seu CPF: (incluindo pontos e traço)', background='Azure1').place(x=10, y=220)
    cpf = Entry(janela, background='LightCyan')
    cpf.place(height=20, width=200, x=10, y=240)

    Label(janela, text='Digite sua idade: ', background='Azure1').place(x=10, y=260)
    idade = Entry(janela, background='LightCyan')
    idade.place(height=20, width=50, x=10, y=280)

    Button(janela, text='Próximo', command=cria_conta, background='LightBlue1').place(x=353, y=280)


def inicio():
    Label(janela, text='💲Bem vindo ao Banco💲', font='Arial 20', background='PaleTurquoise1').pack(side=TOP, fill=X)
    Label(janela, text='Clique no botão para iniciar seu cadastro', font='Arial 12', background='Azure1').pack(side=TOP, fill=X)
    Button(janela, text='Cadastre-se', command=cadastro, background='LightBlue1').pack(side=TOP)

inicio()

def op_nao():
    Label(janela_info, text='Tudo bem, até mais!!', font='Arial 15', background='Azure1').place(x=50, y=250)

def op_sim():
    global janela_op
    janela_op = Tk()
    janela_op.title('Banco')
    janela_op.geometry('500x500+400+100')
    janela_op.configure(background='Azure1')
    janela_info.destroy()

    Label(janela_op, text='Menu de operações', font='Arial 18', background='PaleTurquoise1').pack(side=TOP, fill=X)
    Label(janela_op, text='Escolha qual operação deseja realizar: ', font='Arial 13', background='Azure1').place(x=10, y=50)

    bt_saque = Button(janela_op, text='Saque', background='LightBlue1', command=saque)
    bt_saque.place(x=20, y=90)

    bt_dep = Button(janela_op, text='Depósito', background='LightBlue1', command=deposito)
    bt_dep.place(x=100, y=90)


def func_saque():

    valor = float(valor_saque.get())
    saque = cliente.sacar(valor)

    if cliente.consulta_saldo() > 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Green')
        lb_saldo.place(x=200, y=380)
    elif cliente.consulta_saldo() == 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13')
        lb_saldo.place(x=200, y=380)
    else:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Red')
        lb_saldo.place(x=200, y=380)

    if saque == False:
        Label(janela_op, text='Operação não realizada', background='Azure1', font='Arial 13').place(x=10, y=240)
        Label(janela_op, text='Limite Insuficiente', background='Azure1', font='Arial 13').place(x=10, y=260)
        Label(janela_op, text='Saldo: R$ ' + str(cliente.consulta_saldo()), background='Azure1', font='Arial 13').place(x=10, y=280)
    else:
        Label(janela_op, text='                                        ', background='Azure1', font='Arial 13').place(x=10, y=240)
        Label(janela_op, text='                                        ', background='Azure1', font='Arial 13').place(x=10, y=260)
        Label(janela_op, text='                                        ', background='Azure1', font='Arial 13').place(x=10, y=280)
        Label(janela_op, text='Foi sacado: R$ '+str(valor), background='Azure1', font='Arial 13', fg='red').place(x=10, y=240)
        lb_saldo['text'] = 'Saldo Atual: R$ '+str(cliente.consulta_saldo())+'                                        '

def saque():

    global lb_saldo
    global valor_saque

    Label(janela_op, text='Informe o valor que deseja sacar:                  ', background='Azure1', font='Arial 13').place(x=10, y=150)
    Label(janela_op, text='R$', background='Azure1').place(x=10, y=175)

    valor_saque = Entry(janela_op, background='LightCyan')
    valor_saque.place(x=30, y=175, width=45)

    if cliente.consulta_saldo() > 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Green')
        lb_saldo.place(x=200, y=380)
    elif cliente.consulta_saldo() == 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13')
        lb_saldo.place(x=200, y=380)
    else:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Red')
        lb_saldo.place(x=200, y=380)

    bt_func_saque = Button(janela_op, text='Confirmar', background='lightblue1', command=func_saque)
    bt_func_saque.place(x=85, y=200)


def func_dep():

    valor = float(valor_dep.get())
    dep = cliente.depositar(valor)

    if cliente.consulta_saldo() > 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Green')
        lb_saldo.place(x=200, y=380)
    elif cliente.consulta_saldo() == 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13')
        lb_saldo.place(x=200, y=380)
    else:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='red')
        lb_saldo.place(x=200, y=380)

    if dep == False:
        Label(janela_op, text='Operação não realizada', background='Azure1', font='Arial 13').place(x=10, y=240)
        Label(janela_op, text='Você não pode depositar um valor menor ou igual a R$ 0.0', background='Azure1', font='Arial 13').place(x=10, y=260)
        Label(janela_op, text='                                                 ', background='Azure1', font='Arial 13').place(x=10, y=280)
    else:
        Label(janela_op, text='                                        ', background='Azure1', font='Arial 13').place(x=10, y=240)
        Label(janela_op, text='                                        ', background='Azure1', font='Arial 13').place(x=10, y=260)
        Label(janela_op, text='                                        ', background='Azure1', font='Arial 13').place(x=10, y=280)
        Label(janela_op, text='Foi depositado: R$ ' + str(valor), background='Azure1', font='Arial 13', fg='Green').place(x=10, y=240)
        lb_saldo['text'] = 'Saldo Atual: R$ '+str(cliente.consulta_saldo())+'                                   '

def deposito():

    global valor_dep

    Label(janela_op, text='Informe o valor que deseja depositar:            ', background='Azure1', font='Arial 13').place(x=10, y=150)
    Label(janela_op, text='R$', background='Azure1').place(x=10, y=175)

    valor_dep = Entry(janela_op, background='LightCyan')
    valor_dep.place(x=30, y=175, width=45)

    if cliente.consulta_saldo() > 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Green')
        lb_saldo.place(x=200, y=380)
    elif cliente.consulta_saldo() == 0:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13')
        lb_saldo.place(x=200, y=380)
    else:
        lb_saldo = Label(janela_op, text='Saldo Atual: R$ '+str(cliente.consulta_saldo())+'      ', background='Azure1', font='Arial 13', fg='Red')
        lb_saldo.place(x=200, y=380)

    bt_func_dep = Button(janela_op, text='Confirmar', background='lightblue1', command=func_dep)
    bt_func_dep.place(x=85, y=200)


janela.mainloop()