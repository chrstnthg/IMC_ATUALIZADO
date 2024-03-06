
def definir_estado_imc(imc):
    estado= ""
    if imc < 18.5:
        estado = "Abaixo do Peso"
    elif imc >= 18.5 and imc < 25.0:
        estado = "Peso Ideal"
    elif imc >= 25.0 and imc < 30:
        estado = "Levemente Acima do Peso"
    elif imc >= 30 and imc < 35:
        estado = "Obesidade Grau 1 "
    elif imc >= 35 and imc < 40:
        estado = "Obesidade Grau 2 "
    else:
        estado = "Obesidade Grau 3 "

    print(f"O IMC do Paciente é: {imc} - {estado}.")

def calcular_imc(peso, altura):
    imc = peso / altura **2

    definir_estado_imc(imc)
