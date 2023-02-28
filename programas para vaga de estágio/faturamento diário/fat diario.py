import json

# lê o arquivo com os dados de faturamento mensal
with open('faturamento_mensal.json', 'r') as file:
    faturamento = json.load(file)

# calcula o menor e o maior faturamento diário
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# calcula a média de faturamento diário, ignorando os dias sem faturamento
dias_com_faturamento = [f for f in faturamento if f > 0]
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

# calcula o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_faturamento)

# exibe os resultados
print(f"Menor faturamento diário: R${menor_faturamento:.2f}")
print(f"Maior faturamento diário: R${maior_faturamento:.2f}")
print(f"Média de faturamento diário: R${media_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")

#Explicação do código:

#Na primeira linha, o programa importa o módulo json solicitado para poder ler o arquivo com os dados de faturamento mensal.
#Em seguida, o programa abre o arquivo faturamento_mensal.json em modo de leitura e carrega os dados em uma variável chamada "faturamento".
#O menor e o maior faturamento diário são calculados usando as funções "min' e "max" aplicadas à lista faturamento.
#A média de faturamento diário é calculada da seguinte forma:
#É criada uma nova lista dias_com_faturamento contendo apenas os valores de faturamento maiores que zero, ou seja, ignorando os dias sem faturamento.
#A média é calculada somando-se os valores da lista dias_com_faturamento e dividindo-se pelo número de elementos dessa lista.

#O número de dias com faturamento acima da média mensal é calculado da seguinte forma:
#É criada uma expressão geradora que conta quantos valores da lista dias_com_faturamento são maiores que a média de faturamento.
#A função sum é aplicada à expressão geradora para obter a contagem total.

#Finalmente, o programa exibe os resultados calculados usando a função print. Onde utilizei f-strings para formatar as mensagens de saída.