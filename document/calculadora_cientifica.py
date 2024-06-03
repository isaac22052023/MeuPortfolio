# importando tkinter
from tkinter import *
from tkinter import ttk

# importando a biblioteca math
import math

# cores
cor1 = "#3b3b3b" # black
cor2 = "#feffff" # white
cor3 = "#37474F" # gray
cor4 = "#FF6000" # orange


# criando janela principal
janela = Tk()
janela.title("CALCULADORA")
janela.geometry("235x287")
janela.config(bg = cor1)


# criando frames 
parte_tela = Frame(janela, width = 300, height = 56, bg = cor3)
parte_tela.grid(row = 0, column = 0)

parte_cientifica = Frame(janela, width = 300, height = 86)
parte_cientifica.grid(row = 1, column = 0)

corpo = Frame(janela, width= 300, height= 340)
corpo.grid(row = 2, column = 0)

# funções
global todos_valores

todos_valores = ''
numeros = StringVar()

# funçao entrar valores na tela 
def entrar_valores(valor):
    global todos_valores

    todos_valores = todos_valores + str(valor)
    numeros.set(todos_valores)

# funçao calcular
def calcular():
    global todos_valores

    modulos = ['math.tan','math.sin','math.cos','math.sqrt','math.log','math.log10','math.e','math.pow','math.pi']

    for i in modulos:
        if i=='math.tan':
            todos_valores = todos_valores.replace("tan",i)

        if i=='math.sin':
            todos_valores = todos_valores.replace("sin",i)

        if i=='math.cos':
            todos_valores = todos_valores.replace("cos",i)

        if i=='math.sqrt':
            todos_valores = todos_valores.replace("sqrt",i)

    # -----------------------------------------------------

        if i=='math.log':
            todos_valores.replace("log",i)

        if i=='math.log10':
            todos_valores.replace("log10",i)

        if i=='math.e':
            todos_valores = todos_valores.replace("e",i)

        if i=='math.pow':
            todos_valores = todos_valores.replace("pow",i)

    # -----------------------------------------------------

        if i=='math.pi':
            todos_valores = todos_valores.replace("pi",i)


    resultado = str(eval(todos_valores))
    numeros.set(resultado)

    todos_valores = ''

# funçao limpar tela
def limpar():
    global todos_valores
    todos_valores = ''
    numeros.set("")



# configurando a tela
label_tela = Label(parte_tela, textvariable = numeros, width = 16, height = 2, padx = 7, anchor = 'e', bd = 0, justify = RIGHT, font = ('Ivy 18'), bg= cor3, fg = cor2)
label_tela.place(x = 0, y= 0)


# configurando a parte da calculadora cientifica
btn_tan1 = Button(parte_cientifica, command = lambda: entrar_valores('tan'), text ='tan', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_tan1.place(x = 0, y= 0)
btn_sin = Button(parte_cientifica, command = lambda: entrar_valores('sin'), text ='sin', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_sin.place(x = 59, y= 0)
btn_cos = Button(parte_cientifica, command = lambda: entrar_valores('cos'), text ='cos', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_cos.place(x = 118, y= 0)
btn_sqrt = Button(parte_cientifica, command = lambda: entrar_valores('sqrt'), text ='sqrt', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_sqrt.place(x = 177, y= 0)

btn_log = Button(parte_cientifica, command = lambda: entrar_valores('log'), text ='log', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_log.place(x = 0, y= 29)
btn_log10 = Button(parte_cientifica, command = lambda: entrar_valores('log10'), text ='log10', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_log10.place(x = 59, y= 29)
btn_e = Button(parte_cientifica, command = lambda: entrar_valores('e'), text ='e', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_e.place(x = 118, y= 29)
btn_pow = Button(parte_cientifica, command = lambda: entrar_valores('pow'), text ='pow', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_pow.place(x = 177, y= 29)

btn_pi = Button(parte_cientifica, command = lambda: entrar_valores('pi'), text ='pi', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_pi.place(x = 0, y= 58)
btn_comma = Button(parte_cientifica, command = lambda: entrar_valores(','), text =',', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_comma.place(x = 59, y= 58)
btn_parenthesis_left = Button(parte_cientifica, command = lambda: entrar_valores('('), text ='(', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_parenthesis_left.place(x = 118, y= 58)
btn_parenthesis_right = Button(parte_cientifica, command = lambda: entrar_valores(')'), text =')', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_parenthesis_right.place(x = 177, y= 58)

# configurando a parte corpo
btn_C = Button(corpo, command = limpar, text ='C', width = 14, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_C.place(x = 0, y= 0)
btn_percentage = Button(corpo, command = lambda: entrar_valores('%'), text ='%', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_percentage.place(x = 118, y= 0)
btn_bar = Button(corpo, command = lambda: entrar_valores('/'), text ='/', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_bar.place(x = 177, y= 0)

btn_7 = Button(corpo, command = lambda: entrar_valores('7'), text ='7', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_7.place(x = 0, y= 29)
btn_8 = Button(corpo, command = lambda: entrar_valores('8'), text ='8', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_8.place(x = 59, y= 29)
btn_9 = Button(corpo, command = lambda: entrar_valores('9'), text ='9', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_9.place(x = 118, y= 29)
btn_multiplicatian = Button(corpo, command = lambda: entrar_valores('*'), text ='*', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_multiplicatian.place(x = 177, y= 29)

btn_4 = Button(corpo, command = lambda: entrar_valores('4'), text ='4', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_4.place(x = 0, y= 58)
btn_5 = Button(corpo, command = lambda: entrar_valores('5'), text ='5', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_5.place(x = 59, y= 58)
btn_6 = Button(corpo, command = lambda: entrar_valores('6'), text ='6', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_6.place(x = 118, y= 58)
btn_less= Button(corpo, command = lambda: entrar_valores('-'), text ='-', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_less.place(x = 177, y= 58)

btn_1 = Button(corpo, command = lambda: entrar_valores('1'), text ='1', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_1.place(x = 0, y= 87)
btn_2 = Button(corpo, command = lambda: entrar_valores('2'), text ='2', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_2.place(x = 59, y= 87)
btn_3 = Button(corpo, command = lambda: entrar_valores('3'), text ='3', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_3.place(x = 118, y= 87)
btn_more = Button(corpo, command = lambda: entrar_valores('+'), text ='+', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_more.place(x = 177, y= 87)

btn_0 = Button(corpo, command = lambda: entrar_valores('0'), text ='0', width = 14, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_0.place(x = 0, y= 116)
btn_point = Button(corpo, command = lambda: entrar_valores('.'), text ='.', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor1, fg = cor2)
btn_point.place(x = 118, y= 116)
btn_equal = Button(corpo, command = calcular, text ='=', width = 6, height = 1, relief = RAISED, overrelief = RIDGE, font = ('Ivy 10 bold'), bg= cor4, fg = cor2)
btn_equal.place(x = 177, y= 116)


janela.mainloop()