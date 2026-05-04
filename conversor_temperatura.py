# Solicita ao usuário a temperatura em Celsius e realiza a conversão para número decimal
# A função input() retorna uma string, por isso utilizamos float() para converter o valor para tipo numérico (ponto flutuante)
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Aplica a fórmula de conversão de Celsius para Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Exibe o resultado formatado com duas casas decimais
print(f"A temperatura convertida é {temperatura_fahrenheit:.2f} graus Fahrenheit.")