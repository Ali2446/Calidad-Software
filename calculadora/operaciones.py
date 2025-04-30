def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def sumar_diez(a):
    return a + 10

def multiplicar_lista(numeros):
    """
    Multiplica todos los números de la lista.
    Ejemplo: multiplicar_lista([2, 3, 4]) -> 24
    """
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado
