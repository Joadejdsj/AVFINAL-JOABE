#o programa grava o valor da senha
senha = 1234
senhagv = int(input("Digite a senha: "))
#O programa irá verificar se a senha esta correta, e caso não esteja correta mostra que esta invalida
while senhagv != senha:
    print("SENHA INVALIDA")
    senhagv = int(input("Digite a sua senha: "))
#quando a senha for a correta enviar uma mensagem mostrando isso ao usuario
print("SENHA CORRETA")