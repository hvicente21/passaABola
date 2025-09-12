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
   while not escolha in listaOpcao:
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


usuarios = []
jogadoras = []
telefones = []
emailJogadoras = []
posicoes = ["goleira", "zagueira", "lateral-direita", "lateral-esquerda", "meio-campo", "atacante"]
posicaoJogadora = []
idades = []
times = []
experienciaJogadora= []
experiencias = ["Iniciante","Amadora","Semi-profissional","Profissional"]
observaçoes = []



print("Olá seja Bem-Vindo(a) ao Passa a Bola")
print("Voce sera enchaminhada para a area de inscrição de jogadoras")
inscrever = input("Voce deseja iniciar a incrição? (s/n): ")
while inscrever != "s" and "n":
   print("Voce deve digitar s(sim) ou n(nao) ")
   inscrever = input("Voce deseja iniciar a incrição? (s/n): ")
if inscrever == "s":


   jogadora = negarVazio("Digite seu nome completo: ")
   jogadoras.append(jogadora)


   telefone = verificaTelefone("Digite seu numero para contato: ")
   telefones.append(telefone)


   posicao = forcaOpcao("Digite em qual posição voce joga: ", posicoes)
   posicaoJogadora.append(posicao
                          )
   time = negarVazio("Digite seu time: ")
   times.append(time)


   emailJogadora = negarVazio("Digite seu email para contato: ")
   emailJogadoras.append(emailJogadora)


   idade = maiorIdade("Digite seu ano de nascimento: ")
   idades.append(idade)


   experiencia =forcaOpcao("Digite sua experiência no futebol: ", experiencias)
   experienciaJogadora.append(experiencia)


   observacao = negarVazio("Digite se voce tem alguma observação no futebol: ")
   observaçoes.append(observacao)


   verInscricoes = negarVazio("Voce gostaria de ver as jogadoras inscritas? (s/n): ")
   while verInscricoes != "s" and "n":
       print("Voce deve digitar s(sim) ou n(nao) ")
       verInscricoes = negarVazio("Voce gostaria de ver as jogadoras inscritas? (s/n): ")
       if verInscricoes == "s":
           print(f"Temos inscrita a jogadora {jogadoras[0]}  {telefones[0]}, e a km é {posicaoJogadora[0]} {times[0]}, e a km é {emailJogadora[0]} {idades[0]}, e a km é {experienciaJogadora[0]} {observaçoes[0]}")


else:
   verInscricoes = negarVazio("Voce gostaria de ver as jogadoras inscritas? (s/n): ")
   print("Muito obrigado, até breve!!!")


print(jogadoras[0],telefones[0],posicaoJogadora[0],times[0],emailJogadoras[0],experienciaJogadora[0],observaçoes[0])



