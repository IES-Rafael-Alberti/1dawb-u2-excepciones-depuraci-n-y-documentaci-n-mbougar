"""
Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.
"""

def pedir_Numero() -> int:
    """Pide un número entero al usuario y comprueba si el valor introducido es un número entero.
    
    Returns:
        numero: valor introducido si es entero y 'None' si el valor no es valido
    """
    try:
        numero = int(input("Introduzca un número entero: "))
        return numero
    except ValueError:
        print("La entrada no es correcta.")
        return None 
    

def main():
    numero = pedir_Numero()
    if numero != None:
        print(f"{numero} es un número entero.")




if __name__ == "__main__":
    main() 