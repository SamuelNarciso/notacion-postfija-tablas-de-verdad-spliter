from funAND import FunAND
from funOR import FunOR
from funNOT import FunNOT
from funYOY import FunYOY
from funBI import FunBI

outputArr = []
operadores = {
    ')': {"simbolo": ")", "valor": None},
    '(': {"simbolo": "(", "valor": None},
    ']': {"simbolo": "]", "valor": None},
    '[': {"simbolo": "[", "valor": None},
    '~': {"simbolo": "~", "valor": 3, "funcion": FunNOT()},
    '^': {"simbolo": "^", "valor": 2, "funcion": FunAND()},
    '@': {"simbolo": "@", "valor": 2, "funcion": FunOR()},
    '>': {"simbolo": ">", "valor": 2, "funcion": FunYOY()},
    '<': {"simbolo": "<", "valor": 2, "funcion": FunBI()},
}


def simplificaOperaciones(input):
    operacionSimplificada = input.replace('<->', '<')
    operacionSimplificada = operacionSimplificada.replace('->', '>')
    operacionSimplificada = operacionSimplificada.replace('v', '@')
    return operacionSimplificada


def contadorLetras(input):
    letras = {}
    for char in input:
        if(char.isalpha()):
            letras[char] = []
    return letras


def creadorTablasVerdad(letras, informacion):
    vueltas = 1
    for letra in letras:
        verdadPorColumna = 2**(informacion['columnas']-vueltas)

        while(len(letras[letra]) < informacion['filas']):
            for i in range(verdadPorColumna):
                letras[letra].append(True)

            for j in range(verdadPorColumna):
                letras[letra].append(False)
        vueltas = vueltas+1
    return letras


def vaciarPila(pilaTemporal, notacion):
    while(len(pilaTemporal) > 0):
        popeado = pilaTemporal.pop()
        outputArr.append(popeado['simbolo'])
        notacion.append(popeado)
    return [pilaTemporal, notacion]


def precedencia(caracter, pilaTemporal, notacion):
    ultimaPosicion = len(pilaTemporal)-1

    if(caracter['valor'] >= pilaTemporal[ultimaPosicion]['valor']):
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

            elif(caracter['simbolo'] == ')' or caracter['simbolo'] == ']'):
                [pilaTemporal, notacion] = vaciarPila(pilaTemporal, notacion)

    [pilaTemporal, notacion] = vaciarPila(pilaTemporal, notacion)

    return notacion


def resolverNotacion(notacion, letras):
    resultado = []

    while(len(notacion) > 0):
        tablaResultado = ''
        while(not(type(notacion[0]) is dict)):
            # Es una letra: Agregalo a resolver
            resultado.append(letras.get(notacion.pop(0)))

        resultado.append(notacion.pop(0))  # Agrega el simbolo///
        
        try:
            if(resultado[-1]['simbolo'] == '~'):
               tablaResultado = resultado[-1]['funcion'].funcion(resultado[-2])
            #    print( '~',resultado[-2], ' ::Tabla resultado:: ',tablaResultado)
               resultado.pop()
               resultado.pop()
               resultado.append(tablaResultado)
                
            
            else:
                tablaResultado = resultado[-1]['funcion'].funcion(resultado[-3], resultado[-2])
                # print( resultado[-3],resultado[-1]['simbolo'],resultado[-2], 'Tabla resultado ',tablaResultado)
                resultado.pop()
                resultado.pop()
                resultado.pop()
                resultado.append(tablaResultado)
            
        except:
            return('Ihhhh error cuando resuelve la notacion... :c GG')

    return(resultado[0])


input = '[(p->q)^p]->p'
operacionSimplificada = simplificaOperaciones(input)
letras = contadorLetras(operacionSimplificada)

informacion = {'filas': 2**len(letras), 'columnas': len(letras)}
letras = creadorTablasVerdad(letras, informacion)


notacion = crearNotacion(operacionSimplificada)
resultado = resolverNotacion(notacion, letras)

print('input:: ',input)
print(letras)
print('NOTACION:  :', outputArr)
print('resultado:: ', resultado)
