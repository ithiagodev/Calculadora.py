import customtkinter as ctk

# Configuração do tema da aplicação
ctk.set_appearance_mode("dark")

# Criando a janela principal da aplicação
app = ctk.CTk()
app.title("Calculadora.py")
app.geometry("300x400")

# Criando o campo de entrada (visor da calculadora)
campo = ctk.CTkEntry(app, font=("Arial", 24), justify="right")
campo.pack(pady=10, padx=10, fill="both")

# Função que será chamada ao clicar em um botão numérico ou operador
def clicar(tecla):
    campo.insert("end", tecla)

# Função que executa o cálculo quando o botão "=" é pressionado
def calcular():
    try:
        resultado = eval(campo.get())
        campo.delete(0, "end")
        campo.insert("end", str(resultado))
    except:
        campo.delete(0, "end")
        campo.insert("end", "Erro")

# Função que apaga todo o conteúdo do campo (botão C)
def limpar():
    campo.delete(0, "end")

# Função que apaga o último caractere inserido (botão ⌫)
def apagar():
    texto = campo.get()
    campo.delete(0, "end")
    campo.insert("end", texto[:-1])

# Função para capturar teclas pressionadas no teclado
def pressionar_tecla(event):
    tecla = event.keysym

    mapeamento = {
        "plus": "+",
        "minus": "-",
        "asterisk": "*",
        "slash": "/",
        "percent": "%",
        "Return": "=",
        "BackSpace": "⌫",
        "Escape": "C"
    }

    if tecla in "0123456789*/-+.%":
        clicar(tecla)
    elif tecla == "Return":
        calcular()
    elif tecla == "BackSpace":
        apagar()
    elif tecla == "Escape":
        limpar()
    else:
        clicar(mapeamento.get(tecla, ""))

# Criando um frame para os botões da calculadora
frame_botoes = ctk.CTkFrame(app)
frame_botoes.pack(pady=10, padx=10, fill="both", expand=True)

# Layout dos botões da calculadora (um array 2D com as linhas e colunas dos botões)
botoes = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "="]
]

# Criando os botões dinamicamente a partir do layout definido acima
for i, linha in enumerate(botoes):
    for j, texto in enumerate(linha):
        if texto == "=":
            comando = calcular
        elif texto == "C":
            comando = limpar
        elif texto == "⌫":
            comando = apagar
        else:
            comando = lambda t=texto: clicar(t)

        botao = ctk.CTkButton(frame_botoes, text=texto, font=("Arial", 20), command=comando)
        botao.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")

# Ajustando as colunas e linhas do grid para se expandirem proporcionalmente
for i in range(len(botoes)):
    frame_botoes.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame_botoes.grid_columnconfigure(j, weight=1)

# Configura a captura de teclas do teclado
app.bind("<Key>", pressionar_tecla)

# Inicia o loop da interface gráfica
app.mainloop()