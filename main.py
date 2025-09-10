# preencherRequisitos()
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


adminEmail = "admin@gmail.com"
adminSenha = "senha123"
print("Olá seja Bem-Vindo(a) ao Passa a Bola")
emailUsuario = input("Digite seu email")
senhaUsuario = input("Digite sua senha")
while emailUsuario == "" or senhaUsuario == "":
    print("Preencha todos os requisitos")
    emailUsuario = input("Digite seu email")
    senhaUsuario = input("Digite sua senha")



