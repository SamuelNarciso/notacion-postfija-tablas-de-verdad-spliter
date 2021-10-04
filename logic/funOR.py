class FunOR:
    def __init__(self):
        self.tablaNueva = []

    def funcion(self, tabla1, tabla2):
        self.tablaNueva = []
        for i in range(len(tabla1)):
            if(tabla1[i] or tabla2[i]):
                self.tablaNueva.append(True)
            else:
                self.tablaNueva.append(False)

        return self.tablaNueva
