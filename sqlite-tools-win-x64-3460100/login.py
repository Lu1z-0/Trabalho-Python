from tkinter import *
import sqlite3

janela = Tk()
janela.geometry("200x100")
janela.title("Login")

def clique():
    email = ed1.get()
    senha = ed2.get()

    banco = sqlite3.connect('ecommerce.db')
    cursor = banco.cursor()

    cursor.execute("SELECT senha FROM funcionario WHERE email = ?", (email,))
    resultado = cursor.fetchone()

    if resultado:
        senha_bd = resultado[0]
        if senha == senha_bd:
            lb4 = Label(janela, text="Bem Vindo!")
            lb4.grid(row=4, column=1)
        else:
            lb5 = Label(janela, text="Senha Incorreta!")
            lb5.grid(row=4, column=1)
    else:
        lb5 = Label(janela, text="E-mail Não Encontrado!")
        lb5.grid(row=4, column=1)

    banco.close()

lb2 = Label(janela, text="E-mail:")
lb2.grid(row=0, column=0)

lb3 = Label(janela, text="Senha:")
lb3.grid(row=1, column=0)

ed1 = Entry(janela)
ed1.grid(row=0, column=1)

ed2 = Entry(janela, show="*")
ed2.grid(row=1, column=1)

bt1 = Button(janela, text="Entrar", command=clique)
bt1.grid(column=1, row=3)

janela.mainloop()
