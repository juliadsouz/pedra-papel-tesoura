nome1 = input("Olá! Qual o nome do primeiro jogador?")

print(f"Prazer em te conhecer, {nome1}!")

nome2 = input("Olá! Qual o nome do segundo jogador?")

print(f"Prazer em te conhecer, {nome2}!")

escolha1 = input(f"{nome1}, escolha entre pedra, papel e tesoura: ").lower()
escolha2 = input(f"{nome2}, escolha entre pedra, papel e tesoura: ").lower()

opcoes_validas = ['pedra', 'papel', 'tesoura']

if escolha1 not in opcoes_validas or escolha2 not in opcoes_validas:
    print("Opa, uma das escolhas está inválida. Tente de novo!")

elif (escolha1 == 'tesoura' and escolha2 == 'papel') or (escolha1 == 'pedra' and escolha2 == 'tesoura') or (escolha1 == 'papel' and escolha2 == 'pedra'):
    print(f"{nome1} ganhou!")

elif (escolha2 == 'tesoura' and escolha1 == 'papel') or (escolha2 == 'pedra' and escolha1 == 'tesoura') or (escolha2 == 'papel' and escolha1 == 'pedra'):
    print(f"{nome2} ganhou!")

else:
    print("Deu empate!")

