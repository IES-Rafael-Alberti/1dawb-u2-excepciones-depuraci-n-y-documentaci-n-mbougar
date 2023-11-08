"""
Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"
"""


def comprobar_Contraseña(contraseña: str):
    try:
        intento = input("Introduzca la contraseña: ")
        if intento != contraseña:
            raise NameError("Incorrect Password!!")
    except NameError as e:
        print("Error: ", e)


def main():
    contraseña = "contraseña"
    comprobar_Contraseña(contraseña)
    

if __name__ == "__main__":
    main()  