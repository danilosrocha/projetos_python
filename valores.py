class Valores:
    __distancia: float
    __consumo: float

    def __init__(self, distancia, consumo):
        self.distancia = distancia
        self.consumo = consumo

    @property
    def distancia(self):
        return self.__distancia

    @property
    def consumo(self):
        return self.__consumo

    @distancia.setter
    def distancia(self, distancia):
        try:
            self.__distancia = float(distancia)
        except ValueError:
            print("O valor informado da distancia é inválido!") 
            exit()
        
    @consumo.setter
    def consumo(self, consumo):
        try:
            self.__consumo = float(consumo)
        except ValueError:
            print("O valor informado do consumo é inválido!") 
            exit()
