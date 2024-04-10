from tkinter import *
from tkinter import ttk

# depois fazer uma verssão com as imagens usando o pillow

cor_w = "#cfcfd1"
cor1 = "#1c1c21"
cor2 = "#24244f"
cor3 = "#141436"
cor4 = "#050733"
cor_r = "#e30b0b"

root = Tk()
root.minsize(1000, 500)
root.maxsize(1000, 500)
root.geometry('1000x500')
root.title('')
icon = PhotoImage(file="icon_main.png")
root.iconphoto(FALSE, icon)
root.configure(bg=cor1)

# frames
frame_top = Frame(root, width=700, height=100, bg=cor2, pady=0, padx=4, relief=FLAT)
frame_top.place(x=2, y=2)

frame_left = Frame(root, width=700, height=394, bg=cor3, pady=5, padx=4, relief=FLAT)
frame_left.place(x=2, y=104)

frame_right = Frame(root, width=294, height=496, bg=cor4, pady=0, padx=4, relief=FLAT)
frame_right.place(x=704, y=2)

style = ttk.Style(root)
style.theme_use("clam")

# Label
l_name_app = Label(
    frame_top,
    text="CALCULADORA DE MEDIDAS",
    height=1,
    padx=0,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
l_name_app.place(x=120, y=30)

# CONFIG UNIT
unit_all = {
    'massa': [
        {'kg': 1000},
        {'hg': 100},
        {'dag': 10},
        {'g': 1},
        {'dg': 0.1},
        {'cg': 0.01},
        {'mg': 0.001}
    ],
    'distancia': [
        {'km': 1000},
        {'hm': 100},
        {'dam': 10},
        {'m': 1},
        {'dm': 0.1},
        {'cm': 0.01},
        {'mm': 0.001}
    ],
    'temperatura': [
        {'°C': 'Celsius'},
        {'°F': 'Fahrenheit'}
    ],
    'velocidade': [
        {"m/s": 1},
        {"km/h": 0.277778},
        {"mph": 0.44704},
        {"knot": 0.514444}
    ],
    'tempo': [
        {"s": 1},
        {"min": 60},
        {"h": 3600},
        {"dia": 86400},
        {"semana": 604800},
        {"mes": 2629800},
        {"ano": 31557600}
    ],
    'dados': [
        {"byte": 1},
        {"kilobyte": 1024},
        {"megabyte": 1048576},
        {"gigabyte": 1073741824},
        {"terabyte": 1099511627776},
        {"petabyte": 1125899906842624}
    ],
    'pressao': [
        {"Pa": 1},
        {"psi": 6894.76},
        {"bar": 100000},
        {"atm": 101325}
    ],
    'area': [
        {"m²": 1},
        {"km²": 1000000},
        {"hectare": 10000},
        {"acre": 4046.86}
    ],
    'potencia': [
        {"W": 1},
        {"kW": 1000},
        {"MW": 1000000},
        {"hp": 745.699872}
    ]
}


# functions

def set_combobox_height(event=None):
    comb_from.config(height=len(unit_all))
    comb_to.config(height=len(unit_all))


# menu
def show_menu(i):
    unit_from = []
    unit_for = []
    unit_value = []

    for b in unit_all[i]:
        for k, v in b.items():
            unit_from.append(k)
            unit_for.append(k)
            unit_value.append(v)
    comb_from['values'] = unit_from
    comb_to['values'] = unit_for
    l_unit['text'] = i.upper()

    def conversions():
        get_unit_1 = comb_from.get()
        get_unit_2 = comb_to.get()

        num_conver = float(en_inf_1.get())

        print(get_unit_1, get_unit_2, num_conver)

# container infos conversions
    l_dig = Label(
        frame_right,
        text="Digite o número",
        height=1,
        width=25,
        pady=1,
        padx=3,
        relief=FLAT,
        anchor=CENTER,
        font=("Ivy", 15),
        borderwidth=2,
        bg=cor2,
        fg=cor_w
    )
    l_dig.place(x=1, y=220)

    en_inf = Label(
        frame_right,
        text='',
        width=17,
        relief=SOLID,
        font=("Ivy", 20),
        justify=CENTER,
        bg=cor2,
        fg=cor_w,
    )
    en_inf.place(x=6, y=400)

    en_inf_1 = Entry(
        frame_right,
        width=10,
        relief=SOLID,
        font=("Ivy", 20),
        justify=CENTER,
        bg=cor2,
        fg=cor_w,
    )
    en_inf_1.place(x=5, y=300)

    calc = Button(
        frame_right,
        text='CALCULAR',
        command=conversions,
        height=1,
        width=11,
        relief=FLAT,
        font=("Ivy", 13, 'bold'),
        justify=CENTER,
        activebackground=cor2,
        activeforeground=cor_w,
        bg=cor_r,
        fg=cor_w,
    )
    calc.place(x=164, y=301)


# buttons frame_left

# PRIMEIRA FILEIRA
# 0 = MASA
b_0_app = Button(
    frame_left,
    command=lambda: show_menu('massa'),
    text="MASA",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_0_app.place(x=1, y=1)

# 1 = DISTANCIA
b_1_app = Button(
    frame_left,
    command=lambda: show_menu('distancia'),
    text="DISTANCIA",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_1_app.place(x=240, y=1)

# 2 = TEMPERATURA
b_2_app = Button(
    frame_left,
    command=lambda: show_menu('temperatura'),
    text="TEMPERATURA",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_2_app.place(x=477, y=1)

# SEGUNDA FILEIRA
# 3 = VELOCIDADE
b_3_app = Button(
    frame_left,
    command=lambda: show_menu('velocidade'),
    text="VELOCIDADE",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_3_app.place(x=1, y=130)

# 4 = TEMPO
b_4_app = Button(
    frame_left,
    command=lambda: show_menu('tempo'),
    text="TEMPO",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_4_app.place(x=240, y=130)

# 5 = BYTES/BITS
b_5_app = Button(
    frame_left,
    command=lambda: show_menu('dados'),
    text="DADOS",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_5_app.place(x=477, y=130)

# TERCEIRA FILEIRA
# 6 = PRESSÃO
b_6_app = Button(
    frame_left,
    command=lambda: show_menu('pressao'),
    text="PRESSÃO",
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_6_app.place(x=1, y=254)

# 7 = ÁREA
b_7_app = Button(
    frame_left,
    text="ÁREA",
    command=lambda: show_menu('area'),
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_7_app.place(x=240, y=254)

# 8 = POTENCIA
b_8_app = Button(
    frame_left,
    text="POTENCIA",
    command=lambda: show_menu('potencia'),
    width=12,
    activebackground=cor3,
    activeforeground=cor_w,
    height=2,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 20, "bold"),
    bg=cor2,
    fg=cor_w
)
b_8_app.place(x=477, y=254)

# frame_right
l_unit = Label(
    frame_right,
    text="UNIDADES",
    height=3,
    width=21,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 18),
    bg=cor2,
    fg=cor_w
)
l_unit.place(x=-4, y=1)

l_from = Label(
    frame_right,
    text="De",
    height=1,
    width=3,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 12),
    bg=cor2,
    fg=cor_w
)
l_from.place(x=15, y=140)

l_to = Label(
    frame_right,
    text="Para",
    height=1,
    width=3,
    relief=FLAT,
    anchor=CENTER,
    font=("Ivy", 12),
    bg=cor2,
    fg=cor_w
)
l_to.place(x=150, y=140)

comb_from = ttk.Combobox(
    frame_right,
    height=1,
    width=8,
    justify="center",
    font=("Ivy", 10)
)
comb_from.place(x=55, y=141)

comb_to = ttk.Combobox(
    frame_right,
    height=1,
    width=8,
    justify="center",
    font=("Ivy", 10)
)
comb_to.place(x=190, y=141)

comb_from["values"] = list(unit_all.keys())

set_combobox_height()

root.mainloop()

# brunofraga.com
