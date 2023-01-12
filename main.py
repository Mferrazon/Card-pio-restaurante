# identificador pessoal
print('Bem vindo(a) a loja Michelle Ferraz de Oliveira Nogueira RU 4144573!\n')  

opcoes = {  #inicio código
   'b': ['Básica (Feijão + Paiol + Costelinha)', 1],
   'p': ['Premium (Feijão + Paiol + Costelinha + Partes de porco)', 1.25],
   's': ['Suprema (Feijão + Paiol + Costelinha + Partes do porco + Charque + Calabresa + Bacon)', 1.50]}

acompanhamentos = {
   0: ['Não desejo mais acompanhamentos (encerrar pedido)', 0],
   1: ['200g de arroz', 5],
   2: ['150g de farofa especial', 6],
   3: ['100g de couve cozida', 7],
   4: ['1 laranja descascada', 3]}

def volume():  # Função que solicita e valida o volume
   valor = 0
   while True:
       try:
           volume = float(input('Entre com a quantidade que deseja (ml): ').strip().upper())
           if volume < 300 or volume > 5000:
               print('\nNão aceitamos porções menores que 300ml ou maiores que 5L. Escolha novamente!\n')
           else:
               valor = volume * 0.08
               break
       except ValueError:
           print('\nDigite um volume válido.\n')
   return valor
def opcaoFeijoada():  # Função que solicita e valida a opção
   multiplicador = None
   while True:
       try:
           print('\nMenu opção Feijoada:')
           for key, values in opcoes.items():
               print(f'{key} - {values[0]}')
           opcao = input().strip().lower()
           if opcao not in opcoes.keys():
               print('\nOpção inválida\n')
           else:
               multiplicador = opcoes[opcao][1]
               break
       except ValueError:
           print('\nDigite um opcao válida.\n')
   return multiplicador
def acompanhamentoFeijoada():  # Função que solicita e valida os acompanhamentos
   total_acompanhamento = 0
   while True:
       try:
           print('\nDeseja mais algum acompanhamento:')
           for key, values in acompanhamentos.items():
               print(f'{key} - {values[0]}')
           opcao = int(input())
           if opcao not in acompanhamentos.keys():
               print('\nOpção inválida\n')
           elif opcao == 0:
               break
           else:
               total_acompanhamento += acompanhamentos[opcao][1]
       except ValueError:
           print('\nDigite um acompanhamento válido.\n')
   return total_acompanhamento
valor = volume()
opcao = opcaoFeijoada()
adicionais = acompanhamentoFeijoada()
total = (valor * opcao) + adicionais
print(f'\nValor total (R$):{total:.2f} (Volume = {valor:.2f} * opcao = {opcao:.2f} + Acompanhamento = {adicionais:.2f})')

