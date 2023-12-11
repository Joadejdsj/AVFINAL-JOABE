#mostrei uma mensagem ao usuario, uma mensagem de sua empresa em qual trabalha
print("A empresa ABC irá conceder um aumento no salário de seus empregados, e o aumento irá se basear com o atual salário em que você obtêm")
#Solicitei ao usuario para inserir o seu salário
salario = float(input("Insira o seu salário atual:"))
#O programa verifica o salario do usuario, se for maior que 400 e menor que 800 deverá dar um aumento de 15%
if salario <= 400.00:
    print(f"Novo salário: {salario(salario*(15/100)):.2f}")
    print(f"Reajuste ganho:{salario*(15/100):.2f}")
    print("Em percentual: 15%")
#O programa verifica o salario do usuario, se for maior que 400 e menor que 800 deverá dar um aumento de 15%
elif salario > 400.01 and salario <= 800.00:
    print(f"Novo salário: {salario(salario*(12/100)):.2f}")
    print(f"Reajuste ganho:{salario*(12/100):.2f}")
    print("Em percentual: 12%")
#O programa verifica o salario do usuario, se for maior que 800 e menor que 1200 deverá dar um aumento de 10%
elif salario > 800.01 and salario <= 1200.00:
    print(f"Novo salário: {salario(salario*(10/100)):.2f}")
    print(f"Reajuste ganho:{salario*(10/100):.2f}")
    print("Em percentual: 10%")
#O programa verifica o salario do usuario, se for maior que 1200 e menor que 2000 deverá dar um aumento de 7%
elif salario > 1200.01 and salario <= 2000.00:
    print(f"Novo salário: {salario(salario*(7/100)):.2f}")
    print(f"Reajuste ganho:{salario*(7/100):.2f}")
    print("Em percentual: 7%")
#O programa verifica o salario do usuario, se for maior que 2000 deverá dar um aumento de 4%
elif salario > 2000.01:
    print(f"Novo salário: {salario(salario*(4/100)):.2f}")
    print(f"Reajuste ganho:{salario*(4/100):.2f}")
    print("Em percentual: 4%")