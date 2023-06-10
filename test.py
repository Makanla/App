################
#   TEST DE LOGICA  #
###############
def encontrar_palabras(palabras, matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    palabras_encontradas = []
    palabras_no_encontradas = []

    # Función auxiliar para verificar si una palabra está presente en una dirección específica
    def verificar_direccion(palabra, i, j, di, dj):
        for letra in palabra:
            if i < 0 or i >= filas or j < 0 or j >= columnas or matriz[i][j] != letra:
                return False
            i += di
            j += dj
        return True

    # Función para buscar una palabra en todas las direcciones
    def buscar_palabra(palabra):
        for i in range(filas):
            for j in range(columnas):
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di != 0 or dj != 0:
                            if verificar_direccion(palabra, i, j, di, dj):
                                return True
        return False

    # Verificar cada palabra
    for palabra in palabras:
        if buscar_palabra(palabra):
            palabras_encontradas.append(palabra)
        else:
            palabras_no_encontradas.append(palabra)

    return palabras_encontradas, palabras_no_encontradas

# Ejemplo
palabras = ['HOLA', 'MUNDO', 'PYTHON', 'SOPA', 'JABON']
matriz = [
    ['H', 'O', 'L', 'A', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'U', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'H', 'W', 'W', 'W', 'M', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'T', 'W', 'W', 'W', 'U', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'Y', 'W', 'W', 'W', 'N', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'P', 'W', 'W', 'W', 'D', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'O', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W']
]

encontradas, no_encontradas = encontrar_palabras(palabras, matriz)

print("Palabras encontradas:", encontradas)
print("Palabras no encontradas:", no_encontradas)
