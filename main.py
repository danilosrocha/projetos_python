from calculo import Calculo
from valores import Valores


print(
    """
    Esta aplicação tem como finalidade demonstrar os valores que serão gastos 
    com combustível durante uma viagem, com base no consumo do seu veículo, e 
    com a distância determinada por você!
    """
)

print("Os combustíveis disponíveis para este cálculo são:")
print("\t° Álcool")
print("\t° Díesel")
print("\t° Gasolina")

print(" ")
valores = Valores (
    input("Distância em Quilômetros a ser percorrida\n"),
    input("Consumo de combustível do veículo (Km/l)\n")
)

calculo = Calculo()

print(
    calculo.calcular_gasto(valores)
)
    #try:
       # distancia = float(input("Distância em Quilômetros a ser percorrida\n"))
       # consumo = float(input("Consumo de combustível do veículo (Km/l)\n"))
       # calculo = Calculo()
      #  print(
      #      calculo.calcular_gasto(distancia, consumo)
      #  )
    #except ValueError as erro:
       # print("o valor recebido não é valido")
