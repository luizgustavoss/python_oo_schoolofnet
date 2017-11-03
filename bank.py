class Bank(object):

    def __init__(self, numero):
        self.numero = numero
        self.__total = 0

    def deposito(self, valor):
        self.__total += valor

    def sacar(self, valor):
        self.__total -= valor
        self.__total -= 1

    def total(self):
        return self.__total


class Bradesco(Bank):

    def __init__(self, numero, cvv):
        super(Bradesco, self).__init__(numero)
        self.cvv = cvv


    def sacar(self, valor):
        self._Bank__total -= valor
        self._Bank__total -= 2