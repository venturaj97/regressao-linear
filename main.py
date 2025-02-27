#list comprehension


#variavel especial com letra maiscula????
X = [1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2] #alturas

y = [60, 62, 64, 66, 68, 70, 72, 74] #pesos

#supondo que seja um mundo ideal, os vetores precisam ter o mesmo tamanho

n = len(X)
somatorio_x = sum(X)
somatorio_y = sum(y)
sxy = sum([X[i] * y[i] for i in range(n)]) # soma dos produtos de altura e peso
sx2 = sum([X[i] ** 2 for i in range(n)]) # soma dos quadrados do valores da altura


# inclinaçao da reta, também conhecida como "coeficiente angular"
m = (n * sxy - somatorio_x * somatorio_y) / (n * sx2 - (somatorio_x ** 2)) # m = inclinaçao

# interseçao da reta no eixo y, também conhecida como "coeficiente linear"
b = (somatorio_y / n) - m * (somatorio_x / n) # b = interseçao  

def predict_peso(altura): #x = altura
    return m * altura + b

print(predict_peso(1.73))   