from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#nombre de usuario Test para posibles funciones que no se implementaron
usuario = 'Test'

#funcion para ir a la pestaña perfil
@app.route('/')
def perfil():
    return render_template('perfil.html', nombre_usuario=usuario)

#funcion para ir a la pestaña aplicacion
@app.route('/aplicacion')
def aplicacion():
    return render_template('aplicacion.html', nombre_usuario=usuario)

#funcion que muestra los resultados de la busqueda y recoge los datos de las palabras y la matriz
@app.route('/buscar-palabras', methods=['POST'])
def buscar_palabras():
    palabras = [palabra.strip().lower() for palabra in request.form['palabras'].split(',')]
    matriz_str = request.form.get('matriz').lower()
    matriz = cargar_matriz(matriz_str)
    

    palabras_encontradas, palabras_no_encontradas = encontrar_palabras(palabras, matriz)

    return render_template('resultado.html', palabras_encontradas=palabras_encontradas, palabras_no_encontradas=palabras_no_encontradas, matriz=matriz, palabras=palabras, nombre_usuario=usuario)

#Funcion para cargar las filas y las columnas
def cargar_matriz(matriz_str):
    matriz = []
    filas = matriz_str.split(";")
    for fila in filas:
        columna = fila.split(",")
        matriz.append(columna)
    return matriz

#funcion encontrar_palabras para hallar las palabras ingresadads por el usuario
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
    def busc_palabra(palabra):
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
        if busc_palabra(palabra):
            palabras_encontradas.append(palabra)
        else:
            palabras_no_encontradas.append(palabra)

    return palabras_encontradas, palabras_no_encontradas
    

if __name__ == '__main__':
    app.run(debug=True)
