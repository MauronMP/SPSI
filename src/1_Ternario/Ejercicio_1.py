
class TernarioEquilibrado:

    numACadena = {1: '+', -1: '-', 0: '0'}

    #Inicializador que comprueba si es un entero o no.
    def __init__(self, inp):
        if isinstance(inp, int):
            self.digits = self._enteroATernario(inp)
        else:
            raise TypeError("Introducido un valor erroneo.")

    @staticmethod
    def _enteroATernario(n):
        if n == 0: return []
        if (n % 3) == 0: return [0] + TernarioEquilibrado._enteroATernario(n // 3)
        if (n % 3) == 1: return [1] + TernarioEquilibrado._enteroATernario(n // 3)
        if (n % 3) == 2: return [-1] + TernarioEquilibrado._enteroATernario((n + 1) // 3)

    #Metodo especial de python para representar objetos como cadenas de tipo string.
    def __repr__(self):
        if not self.digits: return "0"
        return "".join(TernarioEquilibrado.numACadena[d] for d in reversed(self.digits))



def main():
    
    print("\n*****************************************************")
    print("Denotamos al 1 como +, el -1 como - y el 0 como 0")

    print ("\nNumero decimal: ", 10, " ternario balanceado: ", TernarioEquilibrado(10))
    print ("Numero decimal: ", -10, " ternario balanceado: ", TernarioEquilibrado(-10))
    print ("Numero decimal: ", 0, " ternario balanceado: ", TernarioEquilibrado(0))
    print ("Numero decimal: ", 2, " ternario balanceado: ", TernarioEquilibrado(2))


    print("*****************************************************")


main()