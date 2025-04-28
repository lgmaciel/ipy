import math

def calcular_area_circulo_de_raio(raio):
    return math.pi * raio ** 2

def somatorio(lista_de_valores):
    soma = 0
    for i in lista_de_valores:
        soma += i
    return soma

area1 = calcular_area_circulo_de_raio(10)
area2 = calcular_area_circulo_de_raio(20)
area3 = calcular_area_circulo_de_raio(5)
print(area1, area2, area3, sep=',  ')

valores_das_areas = [area1, area2, area3]
somatorio_das_areas = somatorio(valores_das_areas)

print(f' somatório das áreas = {somatorio_das_areas}')