# n = número de peças dispostas no tabuleiro
# m = máximo de peças possíveis de ser retirar
print("O jogo é simples.\nVocê escolhe quantas peças quer no tabuleiro\nDepois escolhe quantas peças podem ser tiradas por vez\nVence quem tirar a última peça")

def computador_escolhe_jogada(n,m):
	lista = []
	for x in range(1,m+1):
		if (n - x) == 0:
			numero = x
			break
		elif (n-x) % (m+1) == 0 and (n-x) > m:
			lista.append(x)
		if lista != []:
			lista = sorted(lista)
			numero = lista[-1]
		else:
			numero = 1
	n -= numero 
	if numero > 1:
		print('\nO computador tirou', numero, 'peças')
	else:
		print('\nO computador tirou uma peça')	
	if n > 1:
		print('Agora restam', n,'peças no tabuleiro')
	elif n == 1:
		print('Agora resta apeenas uma peça no tabuleiro')
	return numero
def usuario_escolhe_jogada(n,m):
	bandeira = True
	while bandeira:
		r = int(input('\nQuantas peças você vai tirar? '))
		if r > m or r == 0:
			print('Oops! Jogada inválida! Tente de novo.')
			continue
		else:
			if r == 1:
				print('\nVoce tirou uma peça')
			else:
				print('\nVoce tirou',r, 'peças')
		if n-r == 1:
			print('Agora resta apenas uma peça no tabuleiro')
		else:
			print('Agora restam', n-r,'peças no tabuleiro')
		bandeira = False
	return r

def partida():
	n = int(input('\nQuantas peças? '))
	m = int(input('Limite de peças por jogada? '))
		
	flag = True
	if n % (m+1) == 0:
		print('\nVoce começa')
		while flag:
			removido = usuario_escolhe_jogada(n,m)
			n -= removido
			if n == 0:
				print('Fim do jogo! Voce ganhou!')
				flag = False
				vencedor = 'Usuario'
				break
			remover = computador_escolhe_jogada(n,m)
			n -= remover
			if n == 0:
				print('Fim do jogo! O computador ganhou!')
				flag = False
				vencedor = 'Computador'
				break
	else:
		print('\nComputador começa!')
		while flag:
			removido = computador_escolhe_jogada(n,m)
			n -= removido
			if n == 0:
				print('Fim do jogo! O computador ganhou!')
				flag = False			
				vencedor = 'Computador'
				break
			removido = usuario_escolhe_jogada(n,m)
			n -=removido
			if n == 0:
				print('Fim do jogo! Você ganhou')
				flag = False
				vencedor = 'Usuario'
				break
	return vencedor

def campeonato():
	vit_comput = 0
	vit_user = 0
	print('\n**** Rodada 1 ****')
	vencedor = partida()
	if vencedor == 'Computador':
		vit_comput += 1
	elif venedor == 'Usuario':
		vit_user += 1
	
	print('\n**** Rodada 2 ****')
	vencedor = partida()
	if vencedor == 'Computador':
		vit_comput += 1
	elif venedor == 'Usuario':
		vit_user += 1
		
	print('\n**** Rodada 3 ****')
	vencedor = partida()
	if vencedor == 'Computador':
		vit_comput += 1
	elif venedor == 'Usuario':
		vit_user += 1
	
	print('\n**** Final do campeonato! ****\n')
	print('Placar: Você', vit_user, 'X', vit_comput, 'Computador')
	

def jogo():
	prompt = '\nBem-vindo ao jogo do NIM! Escolha:\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato '
	band = True
	while band:
		resposta = input(prompt)		
		if resposta.strip() == '1':
			print('\nVocê escolheu uma partida isolada!')
			venceu = partida()
			band = False
		elif resposta.strip() == '2':
			print('\nVocê escolheu uma partida isolada!')
			campeonato()
			band = False
		else:
			print('\nDigite somente 1 ou 2')
jogo()
		
