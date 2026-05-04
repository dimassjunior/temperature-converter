# 🌡️ Conversor de Temperatura (Celsius → Fahrenheit)

Este é um programa simples em Python que realiza a conversão de temperatura de **Celsius para Fahrenheit** a partir de um valor informado pelo usuário via terminal.

---

## 📌 Funcionalidades

- Solicita ao usuário uma temperatura em Celsius
- Converte o valor para Fahrenheit usando a fórmula padrão
- Exibe o resultado formatado com **duas casas decimais**

---

## 🧮 Fórmula Utilizada

A conversão é feita com base na seguinte fórmula:

F = (C × 9/5) + 32

Onde:
- C = temperatura em Celsius  
- F = temperatura em Fahrenheit  

---

## 💻 Código

```python
# Solicita ao usuário a temperatura em Celsius e realiza a conversão para número decimal
# A função input() retorna uma string, por isso utilizamos float() para converter o valor para tipo numérico (ponto flutuante)
temperatura_celsius = float(input("Digite a temperatura em Celsius: "))

# Aplica a fórmula de conversão de Celsius para Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# Exibe o resultado formatado com duas casas decimais
print(f"A temperatura convertida é {temperatura_fahrenheit:.2f} graus Fahrenheit.")
```

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado
2. Salve o código em um arquivo chamado:

```
conversor_temperatura.py
```

3. Execute no terminal:

```
python conversor_temperatura.py
```

4. Digite a temperatura quando solicitado e pressione Enter

---

## 📷 Exemplo de Uso

```
Digite a temperatura em Celsius: 25
A temperatura convertida é 77.00 graus Fahrenheit.
```

---

## ⚠️ Observações

- O programa espera um valor numérico válido
- Caso o usuário digite texto ou valores inválidos, ocorrerá erro (`ValueError`)

---

## 🚀 Possíveis Melhorias

- Adicionar tratamento de erro com `try/except`
- Permitir conversão Fahrenheit → Celsius
- Criar interface gráfica (GUI)
- Transformar em API

---