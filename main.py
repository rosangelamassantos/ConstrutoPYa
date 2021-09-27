def print_oi(name):
    print(f'Oi, {name}!')  # a aprtir do Python 3
    print('Oi, ' + name + "!")  # antes do Python 3


def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento


def calcular_area_do_quadrado(lado):
    return lado ** 2


def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2


def contagem_progressiva(fim):
    for num in range(fim):  # repetir o bloco de 0 ate o fim
        print(num)  # exibir o num

def apoiar_candidato(nome,vezes):
    for num in range(vezes):
        # cont = num + 1            -----> essas duas linhas foram substituidas pela linha 30
        # print(f'{cont} - {nome}')

        if num < 9:
            print(f'00{num}','-', nome) # ou print(f'0{num+1} - {nome}') para até 10
        elif num < 99:
            print(f'0{num + 1} - {nome}')
        else:
            print(num + 1, '-', nome)

def brincar_de_plim(fim):
    for num in range(fim):
        if num % 4 == 0:
            print('Plim!')
        else:
            print('{:0>9}'.format(num))


# Estrutura de identificacao / execução do script
if _name_ == '_main_':
    print_oi('Bea')

# Chamar a fucao de calculo da area do retangulo
resultado = calcular_area_do_retangulo(5, 3)
print(f'A área do retângulo é de {resultado} m²')

# Chamar a fucao de calculo da area do quadrado
resultado = calcular_area_do_quadrado(9)
print(f'A área do quadrado é de {resultado} m²')

# Chamar a fucao de calculo da area do triangulo
resultado = calcular_area_do_triangulo(8, 4)
print(f'A área do triângulo é de {resultado} m²')

# Executar uma contagem progessiva
contagem_progressiva(11)

# Exibir o nome do candidato x vezes
apoiar_candidato('Faker', 100)

# Brincar de PLIM
brincar_de_plim(100)