"""
Ahora que ya sabemos como funciona el algoritmo de burbuja, pasemos a la práctica. Implementación en Python y utiliza el debugger para asegurarte que funciona adecuadamente y entiendes su funcionamiento.
"""
def algoritmo_Burbuja(list:list) -> list:
    """Ordena de menor a mayor todos los números de una lista.

    Args:
        list (list): una lista con los números que se van a ordenar de menor a mayor.
    
    Returns: 
        newList (list): lista con los números ordenados de menor a mayor.
    """
    for i in range(0, len(list) - 1):
        for j in range(0, len(list)-1 -i):
            if list[j] > list[j+1]:
                holder = list[j]
                list[j] = list[j+1]
                list[j+1] = holder
    newList = list
    return newList 


def main():
    list = [8, 3, 1, 19, 14, 100, 56, 78, 3, 12, 8]
    newList = algoritmo_Burbuja(list)            
    print(list)
    

if __name__ == "__main__":
    main()