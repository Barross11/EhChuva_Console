import os
import random
import getpass

def main():

    def limpar_console():
        os.system('cls' if os.name == 'nt' else 'clear')
    limpar_console()

    global usuario
    global senha_do_usuario
    usuario = []
    senha_do_usuario = []

    def tela_principal():
        global usuario
        limpar_console()
        print("-EhChuva-\Versão-CONSOLE/-")
        print(f"{usuario}, a cidade que vamos verificar a metereologia é RECIFE")
        print("Recife tem os seguintes bairros:\n1.Boa Viagem  | 9.Casa Forte\n2.San Martin  | 10.Pina\n3.Santo Amaro | 11.Madalena\n4.Graças      | 12.Imbiribeira\n5.Encruzilhada| 13.Espinheiro\n6.Derby       | 14.Cordeiro\n7.Piedade     | 15.Iputinga\n8.Jordão      |")
        bairros_recife = [
            "Boa Viagem",
            "San Martin",
            "Santo Amaro",
            "Graças",
            "Encruzilhada",
            "Derby",
            "Piedade",
            "Jordão",
            "Casa Forte",
            "Pina",
            "Madalena",
            "Imbiribeira",
            "Espinheiro",
            "Cordeiro",
            "Iputinga"
        ]
        decisao = input("Você deseja receber informações metereologicas sobre os bairros? ")
        if decisao == "sim":
            limpar_console()
            print("-EhChuva-\Versão-CONSOLE/-")
            bairros_aleatorios = random.sample(bairros_recife, 15)
            for bairro in bairros_aleatorios:
                temperatura = random.randint(25,35)
                possibilidade = random.random()
                if possibilidade < 0.3:
                    print(f"--{bairro} está a uma temperatura de {temperatura}C° e chovendo--\n")
                elif possibilidade < 0.6:
                    print(f"--{bairro} está a uma temperatura de {temperatura}C° e com possibilidade de chuva--\n")
                else:
                    print(f"--{bairro} está a uma temperatura de {temperatura}C° e sem chuva--\n")
        else:
            print(f"OK, até uma próxima. Foi uma prazer lhe conhecer {usuario}")

    def func_cadastro():

        global usuario
        global senha_do_usuario

        regras = ("----Regras----\n\--Usuário:--/\n1. É preciso que você escolha um usuário!\n2. É preciso que o nome do usuário tenha mais de 3 caracteres\n\--Senha:--/ \n1.É preciso que você escolha uma senha!\n2.Coloque pelo menos 1 caractere especial!\n3.Precisa ter mais que 3 caracteres e menos que 10")
        caracteres_especiais = ["!", "@", "#", "$", "%", "&", "*", "-", "_", "+", "=", "/", "\\", "|", ":", ";", ",", ".", "?", "(", ")", "[", "]", "{", "}", "<", ">", "'", "`", "~", "^", "¡", "¿", "ç"]
        limpar_console()
        print("-EhChuva-\Versão-CONSOLE/-")
        print("Seja Bem vindo a Aba de Cadastro :)")
        cadastro = False
        while cadastro == False:
            limpar_console()
            print("-EhChuva-\Versão-CONSOLE/-")
            escolha_usuario = input("Me diga o usuario que deseja usar> ")
            while escolha_usuario == "" or len(escolha_usuario) <= 3:
                limpar_console()
                print(regras)
                escolha_usuario = input("Me diga o usuario que deseja usar> ")
            limpar_console()
            print("-EhChuva-\Versão-CONSOLE/-")
            print(f"Seu nome de usuário é {escolha_usuario}")
            decisao = input("Tem certeza que deseja manter esse nome? ").lower()
            while decisao != "sim":
                limpar_console()
                print("-EhChuva-\Versão-CONSOLE/-")
                escolha_usuario = input("Me diga o usuario que deseja usar> ")
                while escolha_usuario == "" or len(escolha_usuario) <= 3:
                    limpar_console()
                    print("-EhChuva-\Versão-CONSOLE/-")
                    print(regras)
                    escolha_usuario = input("Me diga o usuario que deseja usar> ")
                limpar_console()
                print("-EhChuva-\Versão-CONSOLE/-")
                print(f"Seu nome de usuário é {escolha_usuario}")
                decisao = input("Tem certeza que deseja manter esse nome? ").lower()            
            usuario.append(escolha_usuario)
            limpar_console()
            print("-EhChuva-\Versão-CONSOLE/-")
            escolha_senha_usuario = getpass.getpass(f"Olá {escolha_usuario}, qual senha você deseja usar?> ")
            while escolha_senha_usuario == "" or not any(char in caracteres_especiais for char in escolha_senha_usuario) or len(escolha_senha_usuario) >= 10 or len(escolha_senha_usuario) <= 3:
                limpar_console()
                print("-EhChuva-\Versão-CONSOLE/-")
                print(regras)
                escolha_senha_usuario = getpass.getpass(f"{escolha_usuario}, qual senha você deseja usar? ")
            senha_do_usuario.append(escolha_senha_usuario)
            cadastro = True
        tela_principal()

    def login():

        global usuario
        global senha_do_usuario

        limpar_console()
        print("-EhChuva-\Versão-CONSOLE/-")        
        decisao = ""
        while decisao != "sim":
            limpar_console()
            print("-EhChuva-\Versão-CONSOLE/-")
            print("Seja Bem vindo ao EHChuva vamos fazer o seu LOGIN!")
            login = input("Me diga o seu usuario> ")
            senha = getpass.getpass("Me diga a sua senha> ")
            if login not in usuario or senha not in senha_do_usuario:
                print("Os seus dados não constam no sistema")
                decisao = input("Você deseja fazer um cadastro?(sim/não) ").lower()
                if decisao == "sim":
                    func_cadastro()                
            elif login in usuario and senha in senha_do_usuario:
                tela_principal()
    login()

if __name__ == "__main__":
    main()
    

