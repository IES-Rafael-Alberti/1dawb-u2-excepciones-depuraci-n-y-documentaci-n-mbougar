"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""
def comprobar_Numero(numero: str) -> bool:
    """Comprueba que en numero introducido es un integer mayor que 0.

    Args:
        numero (str): string que toma el valor del número introducido.
    
    Returns: 
        True o False dependiendo de si el argumento 'numero' es un integer mayor que 0.
    """
    try:
        if int(numero) <= 0:
            return False
        else:
            return True
    except ValueError:
        return False
    

def cadena_Numeros(numero: int) -> str:
    """Crea una string con todos los números impares desde 1 hasta 'numero'.

    Args:
        numero (int): integer que representa el final del rango en el que el programa calcula los números impares.
    
    Returns:
        numeroStr: cadena de caracteres con todos los números impares desde 1 hasta número separados por comas.    
    """
    numeroStr = ""
    for i in range(1, numero+1):
        if i % 2 != 0:
            numeroStr += str(i)
            if i != numero and i != numero-1:
                numeroStr += ", "
    numeroStr += "."
    return numeroStr


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero) != True:
        numero = input("Error. Introduzca un número entero positivo: ")
    numero = int(numero)
    print(f"Todos los números impares desde 1 hasta {numero} separados por comas son: {cadena_Numeros(numero)}")

if __name__ == "__main__":
    main()   
