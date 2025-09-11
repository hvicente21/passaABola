def negarVazio(msg):
    while True:
        nome = input(msg)
        if len(nome) >= 3:
            return nome  # Retorna o nome válido e encerra a função
        else:
            print("Entrada inválida. Tente novamente.")

    
def verificaTelefone(msg):  #telefone tinha que verificar se é um numero e verificar se entre 9 e 13 caracteres
    while True:
        num = input(msg)
        if num.isnumeric():
            if len(num) >= 10 and len(num) <= 13:
                return num  # Retorna o número válido e sai da função.
            else:
                print("Entrada inválida. O número deve ter entre 10 e 13 dígitos.")
        else:
            print("Entrada inválida. Por favor, digite apenas números.")

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
emailJogadoras = []
posicoes= ["goleira","zagueira","lateral-direita","lateral-esquerda","meio-campo","atacante"]
posicaoJogadora = []
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
    jogadora = negarVazio("Digite seu nome completo: ")
    jogadoras.append(jogadora)
    telefone = verificaTelefone("Digite seu numero para contato: ")
    telefones.append(telefone)
    posicao = forcaOpcao("Digite em qual posicao voce joga: ", posicoes)
    posicaoJogadora.append(posicao)



