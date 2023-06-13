#Desarrollar una función que reciba dos diccionarios como parámetros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

def crear_diccionario(clave, valor) -> dict:
    diccionario = {}
    tamaño = int(input("Insertar tamaño deseado para el diccionario: "))  # Solicitar tamaño al usuario
    
    # Iterar para obtener las claves y valores del usuario
    for i in range(tamaño):
        clave = input("Insertar clave " + str(i+1) + ": ")
        valor = int(input("Insertar valor entero para asignar a la clave " + clave + ": "))
        diccionario[clave] = valor
    
    return diccionario


def mix_diccionarios(dic1, dic2) -> dict:
    diccionario_mezclado = dic1.copy()  # Crear una copia del primer diccionario
    
    # Iterar sobre las claves y valores del segundo diccionario
    for clave, valor in dic2.items():
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
    
    return diccionario_mezclado


if __name__ == "__main__":
    clave = 0
    valor = 0
    tamaño = 0
    
    # Llamar a la función crear_diccionario para obtener los diccionarios del usuario
    diccionario1 = crear_diccionario(clave, valor)
    diccionario2 = crear_diccionario(clave, valor)
    
    # Llamar a la función mix_diccionarios para mezclar los diccionarios
    diccionario_mezclado = mix_diccionarios(diccionario1, diccionario2)
    
    # Imprimir los diccionarios resultantes
    print("Diccionario 1: " + str(diccionario1))
    print("Diccionario 2: " + str(diccionario2))
    print("Diccionario mezclado: " + str(diccionario_mezclado))