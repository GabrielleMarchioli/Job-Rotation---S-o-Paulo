num = int(input("Digite um número inteiro positivo: "))
fib = [0, 1]  # começa com os valores iniciais da sequência

# calcula a sequência de Fibonacci até o valor informado
while fib[-1] < num:
    prox = fib[-1] + fib[-2]
    fib.append(prox)

# verifica se o número informado pertence à sequência
if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")


    ##Explicação do código

# Na primeira linha, pedimos ao usuário que informe um número inteiro positivo e armazena esse valor na variável "num".
# Após isso a lista "fib" é inicializada com os dois primeiros valores da sequência de Fibonacci (0 e 1).
# O laço de repetição while calcula os próximos valores da sequência de Fibonacci até que o último valor calculado seja maior ou igual ao número informado pelo usuário. A cada iteração, o programa calcula o próximo valor da sequência somando os dois últimos valores da lista fib e adiciona esse valor à lista.
# Após o laço, nosso programa verifica se o número informado pertence à sequência de Fibonacci verificando se ele está na lista fib. Se estiver, o programa exibe uma mensagem informando que o número pertence à sequência. Caso contrário, exibe uma mensagem informando que o número não pertence à sequência.