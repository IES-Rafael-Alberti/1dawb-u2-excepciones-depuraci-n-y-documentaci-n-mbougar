"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""


def calcular_Años(edad: int) -> str:
    """Crea una string con los años cumplidos separados por un guion.

    Args:
        edad (int): integer que representa la edad del usuario.
    
    Returns:
        años: cadena de caracteres con todos los años desde 1 hasta edad separados por un guion.    
    """
    años = ""
    for i in range(1, edad+1):
        años += str(i)
        if i != edad:
            años += "-"
        else:
            años += "."
    return años


def comprobar_Numero(numero: str) -> bool:
    """Comprueba que el numero introducido es un integer mayor que 0.

    Args:
        numero (str): string que toma el valor del número introducido.
    
    Returns: 
        True o False dependiendo de si el argumento 'numero' es un integer mayor que 0.
    """
    try:
        if int(numero) < 1:
            return False
        else:
            return True
    except ValueError:
        return False


def main():
    edad = input("Introduzca su edad en años: ")
    while comprobar_Numero(edad) != True:
        edad = input("Error. Introduzca su edad en años: ")
    edad = int(edad)
    print(f"Esta es la cadena de todos los años que ha cumplido: \n{calcular_Años(edad)}")
    

if __name__ == "__main__":
    main()   
