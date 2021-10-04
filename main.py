# import arithmetics
from logic2 import Spliter 
from arithmetics.aritmeticos import aritmetico

aritmetico()


opc = 0

while(opc != 4):

    print('1). resolver problema aritmetico')
    print('2). resolver problema logico')
    print('3). resolver problema logico 2')
    print('4). salir')

    print('\n')
    print('Que quiere hacer?')
    opc = int(input())

    if(opc == 1):
        print('1). resolver problema aritmetico')
    elif (opc == 2):
        print('2). resolver problema logico')
        print('')
    elif (opc == 3):
        print('3). resolver problema logico 2')
       
        print('\n')
        Spliter.spliter()
        print('\n')
    elif (opc == 4):
        print('Adios :3')
