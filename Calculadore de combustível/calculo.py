class Calculo:
    def __init__(self):
        self.__valor_gasolina = 4.80
        self.__valor_alcool = 3.80
        self.__valor_diesel = 3.90

    def calcular_gasto(self, valores):
        if (valores.distancia <= 0 or valores.consumo <= 0):
            print ('O valor recebido não pode ser menor ou igual a zero')
            exit()
            
        else:
            gasto_gasolina = round(
                (valores.distancia / valores.consumo) * self.__valor_gasolina, 2)
            gasto_alcool = round(
                (valores.distancia / valores.consumo) * self.__valor_alcool, 2)
            gasto_diesel = round(
                (valores.distancia / valores.consumo) * self.__valor_diesel, 2)

            return """ 
            O valor total gasto será de:

            Gasolina: R$ {} 
            Álcool:   R$ {}
            Diesel:   R$ {}
            """.format(
                gasto_gasolina, gasto_alcool, gasto_diesel
            )
