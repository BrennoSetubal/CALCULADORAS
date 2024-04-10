from tkinter import *

# config window
root = Tk()
root.title('Caulc')
root.geometry('406x355')
root.minsize(406, 355)
root.maxsize(406, 355)
root.configure(background='#200175')
ic = PhotoImage(file="icon.png")
root.iconphoto(False, ic)

num1 = ''
adicao = FALSE
subtracao = FALSE
multiplicacao = FALSE
divisao = FALSE
bt_laran = '#f25602'
tx_ac = '#e84d2a'
bt_blue = '#0e1af0'
bt_k = '#060d91'

# functions
def botao_click(num):
    e.insert(END, num)


def botao_soma():
    global num1
    global adicao
    adicao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botao_sub():
    global num1
    global subtracao
    subtracao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botao_mult():
    global num1
    global multiplicacao
    multiplicacao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botao_divisao():
    global num1
    global divisao
    divisao = TRUE
    num1 = e.get()
    e.delete(0, END)


def botao_limpar():
    e.delete(0, END)


def botao_igual():
    global adicao
    global subtracao
    global multiplicacao
    global divisao
    num2 = e.get()
    e.delete(0, END)
    if adicao == TRUE:
        e.insert(0, int(num1) + int(num2))
        adicao = FALSE
    if subtracao == TRUE:
        e.insert(0, int(num1) - int(num2))
        subtracao = FALSE
    if multiplicacao == TRUE:
        e.insert(0, int(num1) * int(num2))
        multiplicacao = FALSE
    if divisao == TRUE:
        e.insert(0, int(num1) / int(num2))

# div definition
e = Entry(
    root,
    width=16,
    borderwidth=4,
    relief=FLAT,
    fg='#ffffff',
    bg='#a7a28f',
    font=('futura', 25, 'bold'),
    justify=CENTER
)

soma = Button(
    root,
    text='+',
    padx=40,
    pady=20,
    command=botao_soma,
    fg='#ffffff',
    activebackground='#ffffff',
    bg='#f25602',
    activeforeground='#e84d2a',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

subtrai = Button(
    root,
    text='- ',
    padx=40,
    pady=20,
    command=botao_sub,
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_laran,
    activeforeground=tx_ac,
    relief=FLAT,
    font=('futura', 12, 'bold')
)

mutiplica = Button(
    root,
    text='x',
    padx=40,
    pady=20,
    command=botao_mult,
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_laran,
    activeforeground=tx_ac,
    relief=FLAT,
    font=('futura', 12, 'bold')
)

divide = Button(
    root,
    text='÷',
    padx=40,
    pady=20,
    command=botao_divisao,
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_laran,
    activeforeground=tx_ac,
    relief=FLAT,
    font=('futura', 12, 'bold')
)

um = Button(
    root,
    text='1',
    padx=40,
    pady=20,
    command=lambda: botao_click(1),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

dois = Button(
    root,
    text='2',
    padx=40,
    pady=20,
    command=lambda: botao_click(2),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

tres = Button(
    root,
    text='3',
    padx=40,
    pady=20,
    command=lambda: botao_click(3),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

quatro = Button(
    root,
    text='4',
    padx=40,
    pady=20,
    command=lambda: botao_click(4),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

cinco = Button(
    root,
    text='5',
    padx=40,
    pady=20,
    command=lambda: botao_click(5),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

seis = Button(
    root,
    text='6',
    padx=40,
    pady=20,
    command=lambda: botao_click(6),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

sete = Button(
    root,
    text='7',
    padx=40,
    pady=20,
    command=lambda: botao_click(7),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

oito = Button(
    root,
    text='8',
    padx=40,
    pady=20,
    command=lambda: botao_click(8),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

nove = Button(
    root,
    text='9',
    padx=40,
    pady=20,
    command=lambda: botao_click(9),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

zero = Button(
    root,
    text='0',
    padx=91,
    pady=20,
    command=lambda: botao_click(0),
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_k,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

limpar = Button(
    root,
    text='c',
    padx=40,
    pady=20,
    command=botao_limpar,
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_blue,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

igual = Button(
    root,
    text='=',
    padx=40,
    pady=20,
    command=botao_igual,
    fg='#ffffff',
    activebackground='#ffffff',
    bg=bt_blue,
    activeforeground='#90979e',
    relief=FLAT,
    font=('futura', 12, 'bold')
)

# shows-display
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
# keys
um.grid(
    row=1,
    column=0,
)

dois.grid(
    row=1,
    column=1,
)

tres.grid(
    row=1,
    column=2,
)

quatro.grid(
    row=2,
    column=0,
)

cinco.grid(
    row=2,
    column=1,
)

seis.grid(
    row=2,
    column=2,
)

sete.grid(
    row=3,
    column=0,
)

oito.grid(
    row=3,
    column=1,
)

nove.grid(
    row=3,
    column=2,
)

zero.grid(
    row=4,
    column=0,
    columnspan=2
)

soma.grid(
    row=3,
    column=4,
)

subtrai.grid(
    row=2,
    column=4,
)

divide.grid(
    row=0,
    column=4,
)

mutiplica.grid(
    row=1,
    column=4,
)

limpar.grid(
    row=4,
    column=2
)

igual.grid(
    row=4,
    column=4
)

root.mainloop()
