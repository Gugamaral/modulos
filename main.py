import math
import os
from modulos import *

if __name__ == '__main__':
    while True:
        exibir_menu()
        opcao = input('Opção desejada: ')
        os.system('cls')

        match opcao:
            case '1':
                b = int(input('Base do quadrilátero: '))
                h = int(input('Altura do quadrilátero: '))
                print(f'Área: {calcular_quadrilateros(b, h)}')
                continue
            case '2':
                r = int(input('Raio do círculo: '))
                print(f'Área: {calcular_circulo(r)} ')
                continue
            case '3':
                b = int(input('Base do triângulo: '))
                h = int(input('Altura do triângulo: '))
                print(f'Área: {calcular_triangulo(b, h)}')
                continue
            case '4':
                b_menor = int(input('Base do trapézio: '))
                b_maior = int(input('Base do trapézio: '))
                h = int(input('Altura do trapézio: '))
                print(f'Área: {calcular_trapezio(b_menor, b_maior, h)}')
                continue
            case _:
                break



                
