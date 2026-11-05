import customtkinter as ctk
import tkinter as tk

janela = ctk.CTk()

janela.geometry('800x600')
janela.title("PONG")

janela.configure(fg_color="black")

campo = tk.Canvas(
    janela,
    width=800,
    height=600,
    bg="black",
    highlightthickness=0
)

campo.pack()

raquete_1 = campo.create_rectangle(
    30, 250, 45, 350,
    fill="white"
)

raquete_2 = campo.create_rectangle(
    755, 250, 770, 350,
    fill="white"
)

bola = campo.create_oval(
    390, 290, 410, 310,
    fill="white"
)

pontos_1 = 0
pontos_2 = 0

speed_x = 5
speed_y = 4

tempo = 5

placar = campo.create_text(
    400, 50,
    text="0     0",
    fill="white",
    font=("Arial", 30)
)

j1_cima = False
j1_baixo = False

j2_cima = False
j2_baixo = False


def pressionar(event):
    global j1_cima, j1_baixo
    global j2_cima, j2_baixo

    tecla = event.keysym.lower()

    if tecla == "w":
        j1_cima = True
    elif tecla == "s":
        j1_baixo = True
    elif tecla == "up":
        j2_cima = True
    elif tecla == "down":
        j2_baixo = True


def soltar(event):
    global j1_cima, j1_baixo
    global j2_cima, j2_baixo

    tecla = event.keysym.lower()

    if tecla == "w":
        j1_cima = False
    elif tecla == "s":
        j1_baixo = False
    elif tecla == "up":
        j2_cima = False
    elif tecla == "down":
        j2_baixo = False


def mover_pau():

    if j1_cima:
        campo.move(raquete_1, 0, -7)

    if j1_baixo:
        campo.move(raquete_1, 0, 7)

    if j2_cima:
        campo.move(raquete_2, 0, -7)

    if j2_baixo:
        campo.move(raquete_2, 0, 7)


def mover_saco():

    global speed_x, speed_y
    global pontos_1, pontos_2

    campo.move(bola, speed_x, speed_y)

    posicao = campo.coords(bola)

    pos1 = campo.coords(raquete_1)
    pos2 = campo.coords(raquete_2)


    if speed_x < 0:
        if posicao[0] <= pos1[2] and posicao[2] >= pos1[0]:
            if posicao[3] >= pos1[1] and posicao[1] <= pos1[3]:
                speed_x = abs(speed_x)


    if speed_x > 0:
        if posicao[0] <= pos2[2] and posicao[2] >= pos2[0]:
            if posicao[3] >= pos2[1] and posicao[1] <= pos2[3]:
                speed_x = -abs(speed_x)

    if posicao[1] <= 0 or posicao[3] >= 600:
        speed_y = -speed_y


    if posicao[2] < 0:
        pontos_2 += 1
        pontos_att()

        campo.coords(bola, 390, 290, 410, 310)
        speed_x = -5
        speed_y = 4


    if posicao[0] > 800:
        pontos_1 += 1
        pontos_att()

        campo.coords(bola, 390, 290, 410, 310)
        speed_x = 5
        speed_y = 4
def pontos_att():

    campo.itemconfig(
        placar,
        text=str(pontos_1) + "      " + str(pontos_2)
    )

janela.bind("<KeyPress>", pressionar)
janela.bind("<KeyRelease>", soltar)


def atualizar():

    mover_pau()
    mover_saco()

    janela.after(16, atualizar)


def contagem():

    global tempo

    campo.itemconfig(placar, text=str(tempo))

    if tempo > 0:
        tempo -= 1
        janela.after(1000, contagem)
    else:
        campo.itemconfig(placar, text="0    0")
        atualizar()


contagem()
janela.mainloop()

