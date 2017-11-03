class Car:

    tipo = "Automovel"

    # construtor
    def __init__(self, nome, fabricante, ano):
        self.nome = nome
        self.ano = ano
        self.fabricante = fabricante


    def drive(self):
        print("{} iniciado".format(self.nome))


    @staticmethod
    def static_method():
        print("Static Method")


    @classmethod
    def tipo_carro(cls):
        print(cls.tipo)