class FunBI:
    def __init__(self):
        self.tablaNueva = []

    def funcion(self, tabla1, tabla2):
        self.tablaNueva = []        
        for i in range(len(tabla1)):
            if(tabla1[i] and tabla2[i] or (not(tabla1[i]) and not(tabla2[i]))):
                self.tablaNueva.append(True)
            else:
                self.tablaNueva.append(False)

        return self.tablaNueva
