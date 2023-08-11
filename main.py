import subprocess
import time
import tkinter as tk
from datetime import datetime, timedelta, timezone
from tkinter import messagebox


  # Adicione as portas dos seus emuladores
emulator_ports = [5555, 5565, 5575, 5585]
# Função para conectar a um emulador usando adb
def connect_emulator(port):
    subprocess.Popen(['adb', 'start-server'])
    time.sleep(1)# Encerrar qualquer instância existente
    subprocess.Popen(['adb', '-s', f'127.0.0.1:{port}', 'connect', f'127.0.0.1:{port}']) # Conectar ao emulador
    subprocess.Popen(['adb', '-s', f'127.0.0.1:{port}', 'connect', f'127.0.0.1:{port}'])

# Conectar a todos os emuladores da lista
def on_button_click():
    for port in emulator_ports:
        connect_emulator(port)

emulator_ports = [5555, 5565, 5575, 5585]

print("Conexões com emuladores estabelecidas.")





class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("250x150")
        self.configure(bg="#708090")


        self.label_username = tk.Label(self, text="Usuário:", bg="#708090", fg="white", font=("Arial", 10), pady=5)
        self.label_username.pack()
        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        self.label_password = tk.Label(self, text="Senha:", bg="#708090", fg="white", font=("Arial", 10), pady=5)
        self.label_password.pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        self.button_login = tk.Button(self,  text="Entrar", bg="black",
            fg="white",
            font=("Arial", 10),
            relief=tk.RAISED,
            bd=1,
            padx=10,
            pady=2,
            activebackground="red",
            activeforeground="white",
            command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if (
                username == "teste"
                and password == "teste"
                and self.verificar_login_valido()
        ):
            self.destroy()  # Fechar a tela de login
            self.main_page = MainPage()
        else:
            messagebox.showerror("Erro de Login", "Nome de usuário ou senha incorretos ou login expirado.")

    def verificar_login_valido(self):
        expiration_date = datetime(2023, 8, 10) + timedelta(days=2)
        data_atual = datetime.utcnow()
        return data_atual <= expiration_date

class MainPage:
    def __init__(self):

        def executar_sequencia_cliques():
            # Coordenadas dos cliques (ajuste conforme necessário)
            coordenadas_cliques = [
                ("980", "950"),  # Primeiro clique
                ("1738", "952"),  # Segundo clique
                ("1550", "680")  # Terceiro clique
            ]

            def clicar_em_coordenadas(x, y):
                comando_clique = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "tap", x, y
                ]
                subprocess.run(comando_clique, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            for x, y in coordenadas_cliques:
                clicar_em_coordenadas(x, y)
                time.sleep(1)  # Aguardar 1 segundo após cada clique

            # Comando para rolar a tela para baixo
            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "1524", "832", "1524", "332"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            # Clique adicional após a rolagem
            clicar_em_coordenadas("1553", "911")

            clicar_em_coordenadas("1050", "231")

            subprocess.run(["adb", '-s', '127.0.0.1:5555', "shell", "input", "text", "2023"])
            time.sleep(1)
            subprocess.run(["adb", '-s', '127.0.0.1:5555', "shell", "input", "keyevent", "KEYCODE_ENTER"])
            time.sleep(1)

            clicar_em_coordenadas("98.5", "325.1")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "1100", "500", "1100", "100"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2.5)

            clicar_em_coordenadas("1600", "520")

            clicar_em_coordenadas("1590", "736")

            clicar_em_coordenadas("97.6", "541")

            time.sleep(2)

            clicar_em_coordenadas("1824.5", "173.5")

            clicar_em_coordenadas("834.5", "266.7")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "837", "433", "837", "133"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2.5)

            clicar_em_coordenadas("824", "370")

            time.sleep(1)

            clicar_em_coordenadas("1260", "594")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "1112", "780", "1112", "250"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(3)

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "1112", "780", "1112", "500"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(3)

            clicar_em_coordenadas("1149.2", "700")
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "655")
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "610")      #BOTÃO DO COLETE 3
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "565")
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "520")
            # clicar_em_coordenadas("11308", "470")

            # time.sleep(1.5)

            clicar_em_coordenadas("710", "166")

            clicar_em_coordenadas("835", "265.7")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "850", "380", "850", "150"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2)

            clicar_em_coordenadas("820", "420.7")

            time.sleep(1)

            for _ in range(20):  # 10 cliques
                clicar_em_coordenadas("1004", "389")  # Ajuste as coordenadas conforme necessário

            for _ in range(16):  # 10 cliques
                clicar_em_coordenadas("1836", "392")

            # Rodada 3
            ponto_inicial = ("568", "523")
            ponto_final = ("1000", "523")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 5
            ponto_inicial = ("620", "653")
            ponto_final = ("1000", "653")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 7
            ponto_inicial = ("620", "783")
            ponto_final = ("1000", "783")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 4
            ponto_inicial = ("1426.8", "524.4")
            ponto_final = ("1840", "524.4")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 6
            ponto_inicial = ("1434", "653.3")
            ponto_final = ("1840", "653.3")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 8
            ponto_inicial = ("1445.9", "783.3")
            ponto_final = ("1840", "783.3")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", "1141.9", "651.2", "850", "280"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2)

            # Rodada 9
            ponto_inicial = ("660.7", "431")
            ponto_final = ("1000", "431")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 11
            ponto_inicial = ("660.7", "560")
            ponto_final = ("1000", "560")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 13
            ponto_inicial = ("660.7", "689.5")
            ponto_final = ("1000", "689.5")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 10
            ponto_inicial = ("1481.8", "433.3")
            ponto_final = ("1840", "433.3")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 12
            ponto_inicial = ("1481.8", "560.2")
            ponto_final = ("1840", "560.2")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5555', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            time.sleep(1.5)

            clicar_em_coordenadas("1230.5", "950.5")

        #BOTÃO CRIAR SALA 2 -----------------------------------------------------------------------------

        def executar_sequencia_cliques2():
            # Coordenadas dos cliques (ajuste conforme necessário)
            coordenadas_cliques = [
                ("980", "950"),  # Primeiro clique
                ("1738", "952"),  # Segundo clique
                ("1550", "680")  # Terceiro clique
            ]

            def clicar_em_coordenadas(x, y):
                comando_clique = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "tap", x, y
                ]
                subprocess.run(comando_clique, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            for x, y in coordenadas_cliques:
                clicar_em_coordenadas(x, y)
                time.sleep(1)  # Aguardar 1 segundo após cada clique

            # Comando para rolar a tela para baixo
            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "1524", "832", "1524", "332"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            # Clique adicional após a rolagem
            clicar_em_coordenadas("1553", "911")

            clicar_em_coordenadas("1050", "231")

            subprocess.run(["adb", '-s', '127.0.0.1:5565', "shell", "input", "text", "2023"])
            time.sleep(1)
            subprocess.run(["adb", '-s', '127.0.0.1:5565', "shell", "input", "keyevent", "KEYCODE_ENTER"])
            time.sleep(1)

            clicar_em_coordenadas("98.5", "325.1")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "1100", "500", "1100", "100"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2.5)

            clicar_em_coordenadas("1600", "520")

            clicar_em_coordenadas("1590", "736")

            clicar_em_coordenadas("97.6", "541")

            time.sleep(2)

            clicar_em_coordenadas("1824.5", "173.5")

            clicar_em_coordenadas("834.5", "266.7")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "837", "433", "837", "133"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2.5)

            clicar_em_coordenadas("824", "370")

            time.sleep(1)

            clicar_em_coordenadas("1260", "594")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "1112", "780", "1112", "250"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(3)

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "1112", "780", "1112", "500"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(3)

            clicar_em_coordenadas("1149.2", "720")
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "680")
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "640")  # BOTÃO DO COLETE 3
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "600")
            time.sleep(1)
            clicar_em_coordenadas("1149.2", "560")
            # clicar_em_coordenadas("11308", "470")

            # time.sleep(1.5)

            clicar_em_coordenadas("710", "166")

            clicar_em_coordenadas("835", "265.7")

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "850", "380", "850", "150"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2)

            clicar_em_coordenadas("820", "420.7")

            time.sleep(1)

            for _ in range(20):  # 10 cliques
                clicar_em_coordenadas("1004", "389")  # Ajuste as coordenadas conforme necessário

            for _ in range(16):  # 10 cliques
                clicar_em_coordenadas("1836", "392")

            # Rodada 3
            ponto_inicial = ("568", "523")
            ponto_final = ("1000", "523")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 5
            ponto_inicial = ("620", "653")
            ponto_final = ("1000", "653")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 7
            ponto_inicial = ("620", "783")
            ponto_final = ("1000", "783")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 4
            ponto_inicial = ("1426.8", "524.4")
            ponto_final = ("1840", "524.4")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 6
            ponto_inicial = ("1434", "653.3")
            ponto_final = ("1840", "653.3")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 8
            ponto_inicial = ("1445.9", "783.3")
            ponto_final = ("1840", "783.3")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            comando_rolar_para_baixo = [
                "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", "1141.9", "651.2", "850", "280"
            ]
            subprocess.run(comando_rolar_para_baixo, check=True)

            time.sleep(2)

            # Rodada 9
            ponto_inicial = ("660.7", "431")
            ponto_final = ("1000", "431")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 11
            ponto_inicial = ("660.7", "560")
            ponto_final = ("1000", "560")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 13
            ponto_inicial = ("660.7", "689.5")
            ponto_final = ("1000", "689.5")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 10
            ponto_inicial = ("1481.8", "433.3")
            ponto_final = ("1840", "433.3")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            # Rodada 12
            ponto_inicial = ("1481.8", "560.2")
            ponto_final = ("1840", "560.2")

            def realizar_arraste_comando(x1, y1, x2, y2):
                comando_arraste = [
                    "adb", '-s', '127.0.0.1:5565', "shell", "input", "swipe", x1, y1, x2, y2
                ]
                subprocess.run(comando_arraste, check=True)

            realizar_arraste_comando(*ponto_inicial, *ponto_final)

            time.sleep(1.5)

            clicar_em_coordenadas("1230.5", "950.5")

        # BOTÃO CRIAR SALA 3 -----------------------------------------------------------------------------

        def executar_sequencia_cliques3():
                # Coordenadas dos cliques (ajuste conforme necessário)
                coordenadas_cliques = [
                    ("980", "950"),  # Primeiro clique
                    ("1738", "952"),  # Segundo clique
                    ("1550", "680")  # Terceiro clique
                ]

                def clicar_em_coordenadas(x, y):
                    comando_clique = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "tap", x, y
                    ]
                    subprocess.run(comando_clique, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                for x, y in coordenadas_cliques:
                    clicar_em_coordenadas(x, y)
                    time.sleep(1)  # Aguardar 1 segundo após cada clique

                # Comando para rolar a tela para baixo
                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "1524", "832", "1524", "332"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                # Clique adicional após a rolagem
                clicar_em_coordenadas("1553", "911")

                clicar_em_coordenadas("1050", "231")

                subprocess.run(["adb", '-s', '127.0.0.1:5575', "shell", "input", "text", "2023"])
                time.sleep(1)
                subprocess.run(["adb", '-s', '127.0.0.1:5575', "shell", "input", "keyevent", "KEYCODE_ENTER"])
                time.sleep(1)

                clicar_em_coordenadas("98.5", "325.1")

                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "1100", "500", "1100", "100"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                time.sleep(2.5)

                clicar_em_coordenadas("1600", "520")

                clicar_em_coordenadas("1590", "736")

                clicar_em_coordenadas("97.6", "541")

                time.sleep(2)

                clicar_em_coordenadas("1824.5", "173.5")

                clicar_em_coordenadas("834.5", "266.7")

                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "837", "433", "837", "133"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                time.sleep(2.5)

                clicar_em_coordenadas("824", "370")

                time.sleep(1)

                clicar_em_coordenadas("1260", "594")

                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "1112", "780", "1112", "250"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                time.sleep(3)

                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "1112", "780", "1112", "500"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                time.sleep(3)

                clicar_em_coordenadas("1149.2", "720")
                time.sleep(1)
                clicar_em_coordenadas("1149.2", "680")
                time.sleep(1)
                clicar_em_coordenadas("1149.2", "640")  # BOTÃO DO COLETE 3
                time.sleep(1)
                clicar_em_coordenadas("1149.2", "600")
                time.sleep(1)
                clicar_em_coordenadas("1149.2", "560")
                # clicar_em_coordenadas("11308", "470")

                # time.sleep(1.5)

                clicar_em_coordenadas("710", "166")

                clicar_em_coordenadas("835", "265.7")

                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "850", "380", "850", "150"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                time.sleep(2)

                clicar_em_coordenadas("820", "420.7")

                time.sleep(1)

                for _ in range(20):  # 10 cliques
                    clicar_em_coordenadas("1004", "389")  # Ajuste as coordenadas conforme necessário

                for _ in range(16):  # 10 cliques
                    clicar_em_coordenadas("1836", "392")

                # Rodada 3
                ponto_inicial = ("568", "523")
                ponto_final = ("1000", "523")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 5
                ponto_inicial = ("620", "653")
                ponto_final = ("1000", "653")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 7
                ponto_inicial = ("620", "783")
                ponto_final = ("1000", "783")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 4
                ponto_inicial = ("1426.8", "524.4")
                ponto_final = ("1840", "524.4")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 6
                ponto_inicial = ("1434", "653.3")
                ponto_final = ("1840", "653.3")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 8
                ponto_inicial = ("1445.9", "783.3")
                ponto_final = ("1840", "783.3")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                comando_rolar_para_baixo = [
                    "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", "1141.9", "651.2", "850", "280"
                ]
                subprocess.run(comando_rolar_para_baixo, check=True)

                time.sleep(2)

                # Rodada 9
                ponto_inicial = ("660.7", "431")
                ponto_final = ("1000", "431")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 11
                ponto_inicial = ("660.7", "560")
                ponto_final = ("1000", "560")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 13
                ponto_inicial = ("660.7", "689.5")
                ponto_final = ("1000", "689.5")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 10
                ponto_inicial = ("1481.8", "433.3")
                ponto_final = ("1840", "433.3")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                # Rodada 12
                ponto_inicial = ("1481.8", "560.2")
                ponto_final = ("1840", "560.2")

                def realizar_arraste_comando(x1, y1, x2, y2):
                    comando_arraste = [
                        "adb", '-s', '127.0.0.1:5575', "shell", "input", "swipe", x1, y1, x2, y2
                    ]
                    subprocess.run(comando_arraste, check=True)

                realizar_arraste_comando(*ponto_inicial, *ponto_final)

                time.sleep(1.5)

                clicar_em_coordenadas("1230.5", "950.5")

        # BOTÃO CRIAR SALA 3 -----------------------------------------------------------------------------

        def executar_sequencia_cliques4():
                    # Coordenadas dos cliques (ajuste conforme necessário)
                    coordenadas_cliques = [
                        ("980", "950"),  # Primeiro clique
                        ("1738", "952"),  # Segundo clique
                        ("1550", "680")  # Terceiro clique
                    ]

                    def clicar_em_coordenadas(x, y):
                        comando_clique = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "tap", x, y
                        ]
                        subprocess.run(comando_clique, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                    for x, y in coordenadas_cliques:
                        clicar_em_coordenadas(x, y)
                        time.sleep(1)  # Aguardar 1 segundo após cada clique

                    # Comando para rolar a tela para baixo
                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "1524", "832", "1524", "332"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    # Clique adicional após a rolagem
                    clicar_em_coordenadas("1553", "911")

                    clicar_em_coordenadas("1050", "231")

                    subprocess.run(["adb", '-s', '127.0.0.1:5585', "shell", "input", "text", "2023"])
                    time.sleep(1)
                    subprocess.run(["adb", '-s', '127.0.0.1:5585', "shell", "input", "keyevent", "KEYCODE_ENTER"])
                    time.sleep(1)

                    clicar_em_coordenadas("98.5", "325.1")

                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "1100", "500", "1100", "100"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    time.sleep(2.5)

                    clicar_em_coordenadas("1600", "520")

                    clicar_em_coordenadas("1590", "736")

                    clicar_em_coordenadas("97.6", "541")

                    time.sleep(2)

                    clicar_em_coordenadas("1824.5", "173.5")

                    clicar_em_coordenadas("834.5", "266.7")

                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "837", "433", "837", "133"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    time.sleep(2.5)

                    clicar_em_coordenadas("824", "370")

                    time.sleep(1)

                    clicar_em_coordenadas("1260", "594")

                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "1112", "780", "1112", "250"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    time.sleep(3)

                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "1112", "780", "1112", "500"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    time.sleep(3)

                    clicar_em_coordenadas("1149.2", "720")
                    time.sleep(1)
                    clicar_em_coordenadas("1149.2", "680")
                    time.sleep(1)
                    clicar_em_coordenadas("1149.2", "640")  # BOTÃO DO COLETE 3
                    time.sleep(1)
                    clicar_em_coordenadas("1149.2", "600")
                    time.sleep(1)
                    clicar_em_coordenadas("1149.2", "560")
                    # clicar_em_coordenadas("11308", "470")

                    # time.sleep(1.5)

                    clicar_em_coordenadas("710", "166")

                    clicar_em_coordenadas("835", "265.7")

                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "850", "380", "850", "150"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    time.sleep(2)

                    clicar_em_coordenadas("820", "420.7")

                    time.sleep(1)

                    for _ in range(20):  # 10 cliques
                        clicar_em_coordenadas("1004", "389")  # Ajuste as coordenadas conforme necessário

                    for _ in range(16):  # 10 cliques
                        clicar_em_coordenadas("1836", "392")

                    # Rodada 3
                    ponto_inicial = ("568", "523")
                    ponto_final = ("1000", "523")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 5
                    ponto_inicial = ("620", "653")
                    ponto_final = ("1000", "653")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 7
                    ponto_inicial = ("620", "783")
                    ponto_final = ("1000", "783")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 4
                    ponto_inicial = ("1426.8", "524.4")
                    ponto_final = ("1840", "524.4")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 6
                    ponto_inicial = ("1434", "653.3")
                    ponto_final = ("1840", "653.3")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 8
                    ponto_inicial = ("1445.9", "783.3")
                    ponto_final = ("1840", "783.3")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    comando_rolar_para_baixo = [
                        "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", "1141.9", "651.2", "850", "280"
                    ]
                    subprocess.run(comando_rolar_para_baixo, check=True)

                    time.sleep(2)

                    # Rodada 9
                    ponto_inicial = ("660.7", "431")
                    ponto_final = ("1000", "431")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 11
                    ponto_inicial = ("660.7", "560")
                    ponto_final = ("1000", "560")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 13
                    ponto_inicial = ("660.7", "689.5")
                    ponto_final = ("1000", "689.5")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 10
                    ponto_inicial = ("1481.8", "433.3")
                    ponto_final = ("1840", "433.3")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    # Rodada 12
                    ponto_inicial = ("1481.8", "560.2")
                    ponto_final = ("1840", "560.2")

                    def realizar_arraste_comando(x1, y1, x2, y2):
                        comando_arraste = [
                            "adb", '-s', '127.0.0.1:5585', "shell", "input", "swipe", x1, y1, x2, y2
                        ]
                        subprocess.run(comando_arraste, check=True)

                    realizar_arraste_comando(*ponto_inicial, *ponto_final)

                    time.sleep(1.5)

                    clicar_em_coordenadas("1230.5", "950.5")



        janela = tk.Tk()
        janela.title("BOT SALAS")
        janela.geometry("230x280")
        janela.configure(bg="#708090")
        janela.iconbitmap("bot_icon_214984.ico")

        # Botão para Desbugar
        botao_abrir = tk.Button(janela, text="Desbug", bg="darkred", fg="white", font=("Arial", 10), command=on_button_click)
        botao_abrir.pack(pady=5)

        # BOTÃO PARA CRIAR SALA INSTANCIA 1
        botao_cliques = tk.Button(janela, text="CRIAR SALA", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques)
        botao_cliques.pack(pady=15)

        # BOTÃO PARA CRIAR SALA INSTANCIA 2
        botao_cliques = tk.Button(janela, text="CRIAR SALA2", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques2)
        botao_cliques.pack(pady=15)

        # BOTÃO PARA CRIAR SALA INSTANCIA 3
        botao_cliques = tk.Button(janela, text="CRIAR SALA3",  bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques3)
        botao_cliques.pack(pady=15)

        # BOTÃO PARA CRIAR SALA INSTANCIA 4
        botao_cliques = tk.Button(janela, text="CRIAR SALA4", bg="black", fg="white", font=("Arial", 10), command=executar_sequencia_cliques4)
        botao_cliques.pack(pady=15)

        # Executar a interface gráfica
        janela.mainloop()

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
