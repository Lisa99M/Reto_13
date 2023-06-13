#Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
def crear_diccionario(clave, valor) -> dict:
    diccionario = {}  # Crear un diccionario vacío
    
    for i in range(tamaño):
        clave = input("Insertar clave " + str(i+1) + ": ")  # Solicitar al usuario la clave
        valor = int(input("Insertar valor entero para asignar a la clave " + clave + ": "))  # Solicitar al usuario el valor
        diccionario[clave] = valor  # Agregar la clave y valor al diccionario
    
    return diccionario

def orden_ascendente_valores(diccionario_nuevo: dict):
    diccionario_ordenado = {}  # Crear un diccionario vacío para almacenar el diccionario ordenado
    ordenar_valores = sorted(diccionario_nuevo.values())  # Ordenar los valores del diccionario

    for valor in ordenar_valores:
        for clave, valor_dic in diccionario_nuevo.items():
            if valor_dic == valor:  # Encontrar la clave correspondiente al valor
                diccionario_ordenado[clave] = valor  # Agregar la clave y valor al diccionario ordenado
                break
    
    return diccionario_ordenado

if __name__ == "__main__":
    clave = 0
    valor = 0
    tamaño = int(input("Insertar tamaño deseado para el diccionario: "))  # Solicitar al usuario el tamaño del diccionario
    diccionario_nuevo = crear_diccionario(clave, valor)  # Crear un diccionario utilizando la función crear_diccionario
    diccionario_valores_ordenados = orden_ascendente_valores(diccionario_nuevo)  # Ordenar el diccionario por valores
    
    print("Diccionario:", diccionario_nuevo)  # Imprimir el diccionario original
    print("Diccionario ordenado:", diccionario_valores_ordenados)  # Imprimir el diccionario ordenado por valores