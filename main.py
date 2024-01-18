import tkinter 
from tkinter import *
from tkinter import ttk

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

janela = Tk()
janela.title("Tic Tac Toe")
janela.geometry("260x370")
janela.configure(bg=fundo)

frame_cima = Frame(janela, width=240, height=100, bg=co1, relief="raised")
frame_cima.grid(row=0, column=0, sticky= NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, bg=fundo, relief="flat")
frame_baixo.grid(row=1, column=0, sticky= NW)
#
#
app_x = Label(frame_cima, text="X", height=1, relief= "flat", anchor= "center", font=("Ivy 40 bold"), bg=co1, fg=co7)
app_x.place(x=25, y=10)
app_x = Label(frame_cima, text="Jogador 1", height=1, relief= "flat", anchor= "center", font=("Ivy 7 bold"), bg=co1, fg=co0)
app_x.place(x=17, y=70)
app_x_pontos = Label(frame_cima, text="0", height=1, relief= "flat", anchor= "center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_x_pontos.place(x=80, y=20)
#
app_separador = Label(frame_cima, text=":", height=1, relief= "flat", anchor= "center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_separador.place(x=110, y=20)

app_o = Label(frame_cima, text="O", height=1, relief= "flat", anchor= "center", font=("Ivy 40 bold"), bg=co1, fg=co4)
app_o.place(x=170, y=10)
app_o = Label(frame_cima, text="Jogador 2", height=1, relief= "flat", anchor= "center", font=("Ivy 7 bold"), bg=co1, fg=co0)
app_o.place(x=165, y=70)
app_o_pontos = Label(frame_cima, text="0", height=1, relief= "flat", anchor= "center", font=("Ivy 30 bold"), bg=co1, fg=co0)
app_o_pontos.place(x=130, y=20)

#logica

jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [["1","2","3"], ["4","5","6"], ["7","8","9"]]

jogando = "X"
jogar = ""
contador = 0
contador_rodada = 0

def inicia_jogo():
    b_jogar.place(x=800, y=350)
    def controlador(i):
        global jogando
        global contador
        global jogar
        global contador_rodada
        
        if i==str(1):
            if b_0["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')    
        
        if i==str(2):
            if b_1["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')     
        
        if i==str(3):
            if b_2["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')    
        
        if i==str(4):
            if b_3["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate') 
        
        if i==str(5):
            if b_4["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')    
        
        if i==str(6):
            if b_5["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')    
        
        if i==str(7):
            if b_6["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')     
        
        if i==str(8):
            if b_7["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')   
        
        if i==str(9):
            if b_8["text"] =="":
                if jogando == "X":
                    cor = co7
                if jogando == "O":
                    cor = co8

                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2]  = jogando
                
                
                if jogando == "X":
                    jogando = "O"
                    joga = 'jogador 1'
                else:
                    jogando = "X"
                    joga = 'jogador 2'
                contador += 1
                
                
                if contador >= 5:
                    #horizontais
                    if tabela[0][0] == tabela[0][1] == tabela[0][2]!= "":
                        vencedor(jogando)
                    elif tabela[1][0] == tabela[1][1] == tabela[1][2]!= "":
                        vencedor(jogando)
                    elif tabela[2][0] == tabela[2][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #coluna
                    elif tabela[0][0] == tabela[1][0] == tabela[2][0]!= " ":
                        vencedor(jogando)
                    elif tabela[0][1] == tabela[1][1] == tabela[2][1]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][2] == tabela[2][2]!= "":
                        vencedor(jogando)
                    #diagonais
                    elif tabela[0][0] == tabela[1][1] == tabela[2][2]!= "":
                        vencedor(jogando)
                    elif tabela[0][2] == tabela[1][1] == tabela[2][0]!= "":
                        vencedor(jogando)
                    #empate
                    if contador >= 9:
                        vencedor('foi empate')   
        

    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_rodada
        global contador
        
        b_0['state'] = "disabled"
        b_1['state'] = "disabled"
        b_2['state'] = "disabled"
        b_3['state'] = "disabled"
        b_4['state'] = "disabled"
        b_5['state'] = "disabled"
        b_6['state'] = "disabled"
        b_7['state'] = "disabled"
        b_8['state'] = "disabled"

        
        app_vencedor = Label(frame_baixo, text="", height=1, relief="flat", anchor="center", font=("Ivy 13 bold"), bg=co1, fg=co2)
        app_vencedor.place(x=40, y=220)
        
        if i =='X':
            score_2 += 1
            app_vencedor['text'] = "Jogador 2 venceu"
            app_o_pontos['text'] = score_2
        
        if i =='O':
            score_1 += 1
            app_vencedor['text'] = "Jogador 1 venceu"
            app_x_pontos['text'] = score_1
            
        if i =='foi empate':
            app_vencedor['text'] = "Empate"
            
        
        def start(b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8):
            b_0['text'] = ""
            b_1['text'] = ""
            b_2['text'] = ""
            b_3['text'] = ""
            b_4['text'] = ""
            b_5['text'] = ""
            b_6['text'] = ""
            b_7['text'] = ""
            b_8['text'] = ""
            
            b_0['state'] = "normal"
            b_1['state'] = "normal"
            b_2['state'] = "normal"
            b_3['state'] = "normal"
            b_4['state'] = "normal"
            b_5['state'] = "normal"
            b_6['state'] = "normal"
            b_7['state'] = "normal"
            b_8['state'] = "normal"
            
            app_vencedor.destroy()
            b_jogar.destroy()

        b_jogar = Button(frame_baixo, command=lambda: start(b_0, b_1, b_2, b_3, b_4, b_5, b_6, b_7, b_8), text="jogaDNV", width=10, height=1, relief="raise", overrelief=RIDGE, font=("Ivy 10 bold"), bg=fundo, fg=co0)
        b_jogar.place(x=85, y=196)

        
        def jogo_acabou():
            b_jogar.destroy()
            app_vencedor.destroy()
            
            terminar()
            
        if contador_rodada >= 5:
            jogo_acabou()
        else:
            contador_rodada += 1
            
            tabela = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
            contador = 0
            
        
    def terminar():
        global tabela
        global contador_rodada
        global score_1  
        global score_2
        global contador
        global contador_rodada
        
        tabela = [["1","2","3"], ["4","5","6"], ["7","8","9"]]
        contador_rodada = 0
        score_1 = 0
        score_2 = 0
        contador = 0
        
        b_0['state'] = "disabled"
        b_1['state'] = "disabled"
        b_2['state'] = "disabled"
        b_3['state'] = "disabled"
        b_4['state'] = "disabled"
        b_5['state'] = "disabled"
        b_6['state'] = "disabled"
        b_7['state'] = "disabled"
        b_8['state'] = "disabled"
        
        app_fim = Label(frame_baixo, text="Fim", width= 17, relief="flat", anchor="center", font=("Ivy 13 bold"), bg=co1, fg=co2)
        app_fim.place(x=25, y=90)
        
        def jogar_de_novo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()
            inicia_jogo()
            
        b_jogar= Button(frame_baixo, command =jogar_de_novo,text="jogar", width=10, relief= "raise",overrelief=RIDGE, font=("Ivy 10 bold"), bg=fundo, fg=co0)
        b_jogar.place(x=85, y=196)
    
    #linhas verticais
    app_ = Label(frame_baixo, text="", height=23, relief= "flat", pady=5, anchor= "center", font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_.place(x=90, y=15)
    app_ = Label(frame_baixo, text="", height=23, relief= "flat", pady=5, anchor= "center", font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_.place(x=157, y=15)

    #linhas horizontais
    app_ = Label(frame_baixo, text="", width=46, relief= "flat", padx=2, anchor= "center", font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_.place(x=30, y=63)
    app_ = Label(frame_baixo, text="", width=46, relief= "flat", padx=2, anchor= "center", font=("Ivy 5 bold"), bg=co0, fg=co0)
    app_.place(x=30, y=127)

    #buttons
    b_0= Button(frame_baixo, command=lambda:controlador("1"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_0.place(x=30, y=15)
    b_1= Button(frame_baixo, command=lambda:controlador("2"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_1.place(x=96, y=15)
    b_2= Button(frame_baixo, command=lambda:controlador("3"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_2.place(x=163, y=15)

    #linha 1
    b_3= Button(frame_baixo, command=lambda:controlador("4"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_3.place(x=30, y=75)
    b_4= Button(frame_baixo, command=lambda:controlador("5"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_4.place(x=96, y=75)
    b_5= Button(frame_baixo, command=lambda:controlador("6"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_5.place(x=163, y=75)

    #linha 2
    b_6= Button(frame_baixo, command=lambda:controlador("7"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_6.place(x=30, y=135)
    b_7= Button(frame_baixo, command=lambda:controlador("8"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_7.place(x=96, y=135)
    b_8= Button(frame_baixo, command=lambda:controlador("9"), text="", width=3, relief= "flat", overrelief=RIDGE, font=("Ivy 20 bold"), bg=fundo, fg=co0)
    b_8.place(x=163, y=135)



#linha 0
b_jogar= Button(frame_baixo, command =inicia_jogo,text="jogar", width=10, relief= "raise", overrelief=RIDGE, font=("Ivy 10 bold"), bg=fundo, fg=co0)
b_jogar.place(x=85, y=196)

janela.mainloop()