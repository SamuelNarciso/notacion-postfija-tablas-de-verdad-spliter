from funDIV import FunDIV
from funMUL import FunMUL
from funSUM import FunSUM
from funRES import FunRES
from funPOT import FunPOT

# from arithmetics import *

def aritmetico():
    outputArr = []
    operadores = {
        ')': {"valor": False, "simbolo": ')'},
        '(': {"valor": False, "simbolo": '('},
        '^': {"valor": 3, "funcion": FunPOT(), "simbolo": '^'},
        '/': {"valor": 2, "funcion": FunDIV(), "simbolo": '/'},
        '*': {"valor": 2, "funcion": FunMUL(), "simbolo": '*'},
        '-': {"valor": 1, "funcion": FunRES(), "simbolo": '-'},
        '+': {"valor": 1, "funcion": FunSUM(), "simbolo": '+'},
    }


    def inputToArray(input=''):
        inputTemporal, cifra, operador = [], '', ''
        caracteresArr = list(input)
        while(len(caracteresArr) > 0):
            if(caracteresArr[0].isnumeric()):
                cifra += caracteresArr.pop(0)
                continue
            operador = caracteresArr.pop(0)
            inputTemporal.append(cifra)
            inputTemporal.append(operador)
            cifra, operador = '', ''

        inputTemporal.append(cifra)
        inputTemporal.append(operador)

        return list(filter(lambda char: char.strip(), inputTemporal))


    def vaciarPila(pilaTemporal, notacion):
        while(len(pilaTemporal) > 0):
            popeado = pilaTemporal.pop()
            outputArr.append(popeado['simbolo'])
            notacion.append(popeado)
        return [pilaTemporal, notacion]


    def precedencia(caracter, pilaTemporal, notacion):
        ultimaPosicion = len(pilaTemporal)-1

        if(caracter['valor'] == pilaTemporal[ultimaPosicion]['valor']):
            elementoTop = pilaTemporal.pop()
            outputArr.append(elementoTop['simbolo'])
            notacion.append(elementoTop)
            pilaTemporal.append(caracter)
        elif(caracter['valor'] > pilaTemporal[ultimaPosicion]['valor']):
            pilaTemporal.append(caracter)
        elif(caracter['valor'] < pilaTemporal[ultimaPosicion]['valor']):
            [pilaTemporal, notacion] = vaciarPila(pilaTemporal, notacion)
            pilaTemporal.append(caracter)
        return [pilaTemporal, notacion]


    def crearNotacion(operacion):
        notacion, pilaTemporal = [], []

        for elemento in operacion:
            caracter = operadores.get(elemento)
            if(not(bool(caracter))):
                notacion.append(elemento)
                outputArr.append(elemento)

            else:
                if(caracter['valor']):
                    if(len(pilaTemporal) == 0):
                        pilaTemporal.append(caracter)
                    else:
                        [pilaTemporal, notacion] = precedencia(
                            caracter, pilaTemporal, notacion)

                elif(caracter['simbolo'] == ')'):
                    [pilaTemporal, notacion] = vaciarPila(pilaTemporal, notacion)

        [pilaTemporal, notacion] = vaciarPila(pilaTemporal, notacion)

        return notacion


    def resolverOperacion(operacion):
        arrTmp = []
        while(len(operacion) > 0):
            resultado = ''
            # mientras que no sea un diccionario
            while(not(type(operacion[0]) is dict)):
                arrTmp.insert(0, operacion.pop(0))

            arrTmp.insert(0, operacion.pop(0))
            try:
                resultado = arrTmp[0]['funcion'].funcion(arrTmp[2], arrTmp[1])
            except:
                return None

            for x in range(3):
                arrTmp.pop(0)

            arrTmp.insert(0, resultado)

        return(float(arrTmp[0]))


    inputUser = '(6+2)*3/2^2-4'

    inputArray = inputToArray(inputUser)
    notacion = crearNotacion(inputArray)
    resultado = resolverOperacion(notacion)

    print('Entrada', inputUser)
    print('Notacion postfija', outputArr)
    print('resultado', resultado)

aritmetico()