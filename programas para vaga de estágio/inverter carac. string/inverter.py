texto = "Contratação!"
texto_invertido = ""

for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]

print(texto_invertido)

# Explicação do código 

#A variável texto contém a string a ser invertida.
#A variável texto_invertido é inicializada com uma string vazia.
#É feito um loop pelo índice dos caracteres da string texto, de trás para frente, ou seja, do último para o primeiro. O primeiro argumento da função range indica o índice final (o tamanho da string menos 1), o segundo argumento indica o índice inicial (0) e o terceiro argumento indica o passo do loop (-1).
#Em cada iteração do loop, o caractere correspondente ao índice é adicionado à variável "texto_invertido" usando o operador +=.
#Finalmente, a string texto_invertido invertida é exibida na tela usando a função print. Dessa vez não achei necessario o uso de f-strings



