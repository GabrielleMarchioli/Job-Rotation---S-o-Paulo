faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = valor / total_faturamento * 100
    print(f"{estado}: {percentual:.2f}%")

# Explicação do Código

#A variável "faturamento" associa cada estado ao valor de faturamento mensal correspondente.
#A variável "total_faturamento" é calculada somando todos os valores do faturamento.
#Em seguida, é feito um loop pelos itens do aturamento, ou seja, pelo estado-valor. 
# Para cada item, nosso percentual é calculado dividindo o valor pelo total de faturamento e multiplicando por 100. 
# O resultado é exibido na tela usando a função print e utilizo o f-strings para formatar a mensagem de saída.