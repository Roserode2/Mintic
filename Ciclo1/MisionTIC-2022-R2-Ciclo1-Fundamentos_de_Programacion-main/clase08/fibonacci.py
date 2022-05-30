from turtle import Vec2D


n = int(input("Ingrese número para calcular el fibonacci: "))
def fibonacci(n):
    a = 0
    b = 1
    sum = 0
    i = 2
    # Validar
    if n < 0:
        return "Número erróneo"
    # Algoritmo
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:        
        while i <= n:
            sum = a + b
            a = b
            b = sum
            i += 1
        return b
    
print(fibonacci(n))