"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.
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
    """Crea una string con todos los números desde 'numero' hasta 0.

    Args:
        numero (int): integer que representa el principio de la cuenta atras hasta 0.
    
    Returns:
        numeroStr: cadena de caracteres con todos los números desde 'numero' hasta 0 separados por comas.    
    """
    numeroStr = ""
    for i in range(numero, -1, -1):
        numeroStr += str(i)
        if i != 0:
            numeroStr += ", "
    numeroStr += "."
    return numeroStr


def main():
    numero = input("Introduzca un número entero positivo: ")
    while comprobar_Numero(numero) != True:
        numero = input("Error. Introduzca un número entero positivo: ")
    numero = int(numero)
    print(f"La cuenta atrás desde {numero} hasta cero separados por comas es: {cadena_Numeros(numero)}")

if __name__ == "__main__":
    main()   