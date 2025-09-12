def negarVazio(msg):
   while True:
       nome = input(msg)
       if len(nome) >= 3:
           return nome  # Retorna o nome válido e encerra a função
       else:
           print("Entrada inválida. Tente novamente.")




def verificaTelefone(msg):  # telefone tinha que verificar se é um numero e verificar se entre 9 e 13 caracteres
   while True:
       num = input(msg)
       if num.isnumeric():
           if len(num) >= 10 and len(num) <= 13:
               return num  # Retorna o número válido e sai da função.
           else:
               print("Entrada inválida. O número deve ter entre 10 e 13 dígitos.")
       else:
           print("Entrada inválida. Por favor, digite apenas números.")




def forcaOpcao(msg, listaOpcao):
   opcoes = ', '.join(listaOpcao)
   escolha = input(f"{msg}\n{opcoes}\n->")
   while not escolha.title() in listaOpcao:
       escolha = input(f"{msg}\n{opcoes}\n->")
   return escolha




def verificaNumero(msg):
   num = input(msg)
   while not num.isnumeric():
       print("Erro!")
       num = input(msg)
   return int(num)




def maiorIdade(msg):
   while True:
       idade = verificaNumero(msg)
       if idade > 2019:
           print("Necessario ser maior que 6 anos para se inscrever")


       else:
           return idade
       
def listarInscricoesLinha():
    if not jogadoras:
        print("Ainda não há jogadoras inscritas.")
        return
    print("\n--- Lista de Inscrições ---")
    
    for i in range(len(jogadoras)):
        print(
            f"Nome: {jogadoras[i]} | Telefone: {telefones[i]} | Posição: {posicaoJogadora[i]} | Time: {times[i]} | E-mail: {emailJogadoras[i]} | Idade: {idades[i]} | Experiência: {experienciaJogadora[i]} | Observações: {observacoes[i]}")


usuarios = []
jogadoras = []
telefones = []
emailJogadoras = []
posicoes = ["Goleira", "Zagueira", "Lateral-direita", "Lateral-esquerda", "Meio-campo", "Atacante"]
posicaoJogadora = []
idades = []
times = []
experienciaJogadora= []
experiencias = ["Iniciante","Amadora","Semi-profissional","Profissional"]
observacoes = []



print("Olá seja Bem-Vindo(a) ao Passa a Bola")
while True:
    print("\nMENU:")
    print("1 - Fazer Inscrição")
    print("2 - Ver Inscrições")
    print("3 - Sair")
    
    try: 
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            print("Voce sera enchaminhada para a area de inscrição de jogadoras")
            inscrever = input("Voce deseja iniciar a incrição? (s/n): ")
            while inscrever.lower() not in ["s","n"]:
                print("Voce deve digitar s(sim) ou n(nao) ")
                inscrever = input("Voce deseja iniciar a incrição? (s/n): ")
            if inscrever == "s":

                jogadora = negarVazio("Digite seu nome completo: ")
                jogadoras.append(jogadora)


                telefone = verificaTelefone("Digite seu numero para contato: ")
                telefones.append(telefone)


                posicao = forcaOpcao("Digite em qual posição voce joga: ", posicoes).lower()
                posicaoJogadora.append(posicao)

                time = negarVazio("Digite seu time: ")
                times.append(time)


                emailJogadora = negarVazio("Digite seu email para contato: ")
                emailJogadoras.append(emailJogadora)


                idade = maiorIdade("Digite seu ano de nascimento: ")
                idades.append(idade)


                experiencia =forcaOpcao("Digite sua experiência no futebol: ", experiencias).lower()
                experienciaJogadora.append(experiencia)


                observacao = negarVazio("Digite se voce tem alguma observação no futebol: ")
                observacoes.append(observacao)

        elif escolha == 2:
            listarInscricoesLinha()

        elif escolha == 3:
            print("Muito obrigada, ate breve!!!")
            break
            
        else: 
            print("Escolha invalida")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")






