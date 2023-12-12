import tkinter as tk
import subprocess

def desligar_wifi():
    try:
        subprocess.run(["wmic", "path", "win32_networkadapter", "where", "NetConnectionID='Wi-Fi'", "call", "disable"], check=True)
        status_label.config(text="Wi-Fi desligado com sucesso.")
    except subprocess.CalledProcessError as e:
        status_label.config(text="Erro ao desligar o Wi-Fi.")

def ligar_wifi():
    try:
        subprocess.run(["wmic", "path", "win32_networkadapter", "where", "NetConnectionID='Wi-Fi'", "call", "enable"], check=True)
        status_label.config(text="Wi-Fi ligado com sucesso.")
    except subprocess.CalledProcessError as e:
        status_label.config(text="Erro ao ligar o Wi-Fi.")

# Resto do código permanece o mesmo

# Cria uma janela
window = tk.Tk()
window.title("Controle de Wi-Fi")

# Cria botões
desligar_button = tk.Button(window, text="Desligar Wi-Fi", command=desligar_wifi)
ligar_button = tk.Button(window, text="Ligar Wi-Fi", command=ligar_wifi)

# Cria uma label para exibir o status
status_label = tk.Label(window, text="")

# Organiza os elementos na janela
desligar_button.pack()
ligar_button.pack()
status_label.pack()

# Inicia a janela
window.mainloop()