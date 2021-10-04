class FunYOY:
    def __init__(self):
        self.tablaNueva = []

    def funcion(self, tabla1, tabla2):
        self.tablaNueva = []
        for i in range(len(tabla1)):
            if(tabla1[i] == True and tabla2[i] == False):
                self.tablaNueva.append(False)
            else:
                self.tablaNueva.append(True)
        return self.tablaNueva
