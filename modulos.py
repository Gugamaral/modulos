from datetime import date

def exibir_menu():
    meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outrubro', 'Novembro', 'Dezembro')
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year

    print(f'\n{dia} de {meses[mes - 1]} de {ano}.\n')

    print('1 - Calcular quadrilátero')
    print('2 - Calcular círculo')
    print('3 - Calcular triângulo')
    print('4 - Calcular trapézio')
    print('5 - Sair do programa')

def calcular_quadrilateros(b, h):
    a = b * h
    return a

def calcular_circulo(r):
    a = 3.14*r**2
    return a

def calcular_triangulo(b, h):
    a = (b * h)/2
    return a

def calcular_trapezio(b_menor, b_maior, h):
    a = ((b_menor + b_maior)*h)/2
    return a






# from modulos import calcular_circulo

# b = int(input('Informe o valor da base: '))
# h = int(input('Informe o valor da altura: '))

# print(f'Área do Quadrilátero: {modulos.calcular_quadrilateros(b, h)}. ')

# r = str(input('Informe o valor do raio: ')).replace(',' , '.')
# r = float(r)

# print(f'Área do círculo: {calcular_circulo(r)}. ')

# b = int(input('Informe o valor da base: '))
#h = int(input('Informe o valor da altura: '))

# print(f'Área do Quadrilátero: {calcular_quadrilateros(b, h)}. ')

# print(f'Área do Triângulo: {calcular_triangulo(b, h)}. ')

