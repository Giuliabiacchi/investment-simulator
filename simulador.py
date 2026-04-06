print("\n Simulador de Investimentos\n")
valor_inicial = float(input("Digite o valor inicial: "))
taxa = float(input("Digite a taxa (% ao ano): ")) / 100
tempo = int(input("Digite o tempo (anos): "))

valor_final = valor_inicial * (1 + taxa) ** tempo
lucro = valor_final - valor_inicial

print("\nResultado da Simulação: ")
print(f"Valor final: R$ {valor_final:.2f}")
print(f"Lucro: R$ {lucro:.2f}")
