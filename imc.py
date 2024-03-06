
import estado_imc as calcular

peso = 0
altura = 0.0
nome = ""

nome = input("Qual é o nome do paciente? ")

erro = True

while erro:
    try:
        peso = int(input("Qual é o peso do paciente? "))
        erro = False
    except:
        print("Valor do Peso Invalido!")

erro = True

while  erro:
    try:
        altura = float(input("Qual é a altura do paciente? "))
        erro = False
    except:
        print("Valor da Altura Invalido!")


calcular.calcular_imc(peso, altura)
