def negarVazio(var,msg,msgErro):
    while len(var) < 3:
        print(msgErro)
        var = input(msg) 
    return

    
def forcaOpcao(msg,listaOpcao):
    opcoes = ', '.join(listaOpcao)
    escolha = input(f"{msg}\n{opcoes}\n->")
    while not escolha in listaOpcao:
        escolha = input(f"{msg}\n{opcoes}\n->")
    return escolha

def verificaNumero(msg):
    num = input(msg)
    while not num.isnumeric():
        print("Erro!")
        num = input(msg)
    return int(num)

usuarios = []
jogadoras = []
telefones = []
posiçoes = []
emailJogadoras = ["goleira","zagueira","lateral-direita","lateral-esquerda","meio-campo","atacante"]
idades = []
times = []
experiencias = []




adminEmail = "admin@gmail.com"
adminSenha = "senha123"
print("Olá seja Bem-Vindo(a) ao Passa a Bola")
emailUsuario = input("Digite seu email: ")
senhaUsuario = input("Digite sua senha: ")
while emailUsuario == "" or senhaUsuario == "":
    print("Preencha todos os requisitos")
    emailUsuario = input("Digite seu email: ")
    senhaUsuario = input("Digite sua senha: ")
usuarios.append(emailUsuario)

inscrever = input("Voce deseja iniciar a incrição? (s/n): ")
while inscrever != "s" and "n":
    print("Voce deve digitar s(sim) ou n(nao) ")
    inscrever = input("Voce deseja iniciar a incrição? (s/n): ") 
if inscrever == "s":
    jogadora = input("Digite seu nome completo: ")
    negarVazio(jogadora,"Digite seu nome completo","Digite um nome com mais de 2 caracteres" )
