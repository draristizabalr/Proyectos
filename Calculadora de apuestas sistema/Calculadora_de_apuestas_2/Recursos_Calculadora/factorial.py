def factorial(numero):
    '''
    Calcula el factorial de un número entero
    '''
    try:
        numero = int(numero)
    except Exception as e:
        print(f'Se ha producido un error: {e}')

    if numero == 0:
        return 1
    else:
        resultado = numero * factorial(numero - 1)

    return resultado
