#Em um país imaginario denominado Lisarbtodos os cidadãos ficam felizes em pagar seus impostos, pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em benéficio da população, sem qualquer desvio. A moeda desse país é o Rombus, e o símbolo é o R$.

#peço para o usuario inserir seu salário para descobrir o iposto em que ele deverá pagar
print("OLÁ CIDADÃO, VOCÊ IRÁ DESCOBRIR O QUANTO DE IMPOSTO VOCÊ DEVERÁ PAGAR")
salario = float(input("Por favor, digite o seu salário atual: "))
#O programa serve para verificar o salário ja enviado pelo usuario, se ele for menor que 2000, a pessoa será isenta de impostos.
if salario < 2000.00:
    print(f"Isento de imposto")
#O programa serve para verificar o salário ja enviado pelo usuario, se ele for igual ou maior que 2000 e menor que 3000, deverá um imposto que é 0.08 vezes o seu salário
elif salario >= 2000.01 and salario < 3000.00:
    imposto = salario*0.08
    print(f"Você deverá pagar: R${imposto:.2f}")
#O programa serve para verificar o salário ja enviado pelo usuario, se ele for igual ou maior que 3000 e menor que 4500, deverá um imposto que é 0.18 vezes o seu salário
elif salario >= 3000.01 and salario <= 4500.00:
    imposto = salario*0.18
    print(f"Você deverá pagar: R${imposto:.2f}")
#O programa serve para verificar o salário ja enviado pelo usuario, se ele for maior que 4500, ele deverá pagar um imposto de 0.28 vezes o seu salário
elif salario > 4500.01:
    imposto = salario*0.28
    print(f"Você deverá pagar: R${imposto:.2f}")