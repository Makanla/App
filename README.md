# Guía de despliegue - App prueba

Guia de despliegue para esta App de prueba

## Recursos Utilizados

- Bootstrap: Se utiliza el framework Bootstrap para agregar estilos y componentes predefinidos a la aplicación.
- Flask: Flask es el framework web utilizado para construir la aplicación.
- Jinja2: Se utiliza el motor de plantillas Jinja2 para generar dinámicamente las páginas HTML.
- CSS personalizado: Se utiliza un archivo CSS personalizado para agregar estilos adicionales y personalizados a la aplicación.

## Tecnologias Utilizadas

- Python: Lenguaje de programación utilizado como base para el desarrollo de la aplicación.
- Flask: Framework web de Python utilizado para construir la aplicación.
- HTML: Lenguaje de marcado utilizado para estructurar y presentar el contenido de las páginas web. 
- CSS (Cascading Style Sheets): Lenguaje utilizado para describir el aspecto visual y la presentación de las páginas web.
- Bootstrap: Framework CSS utilizado para la creación de interfaces de usuario responsivas y modernas.
- Jinja2: Motor de plantillas utilizado en Flask para generar dinámicamente las páginas HTML.

## Requisitos previos

Asegúrate de tener instalado lo siguiente:

- Python (versión 3.6 o superior)
- Flask (puedes instalarlo ejecutando `pip install flask`)

## Configuración inicial

1. Clona este repositorio o descarga los archivos de la aplicación en tu máquina local.

2. Abre una terminal y navega hasta el directorio del proyecto.


3. Activa el entorno virtual ejecutando el comando apropiado para tu sistema operativo:
   - Windows: `env\Scripts\activate`
   - macOS/Linux: `source env/bin/activate`

4. Instala las dependencias requeridas ejecutando el siguiente comando:
   ```
   pip install -r requirements.txt
   ```

## Despliegue local

1. En la terminal, asegúrate de estar en el directorio raíz de la aplicación (donde se encuentra App.py) y activa el entorno virtual.

2. Ejecuta el siguiente comando para iniciar el servidor Flask localmente:
   ```
   flask run
   ```

3. Abre tu navegador web y visita `http://localhost:5000` o `http://127.0.0.1:5000/`  para ver la aplicac en funcionamiento.

## Despliegue en un servidor web

1. Configura tu servidor web siguiendo las instrucciones específicas para tu servidor. Asegúrate de tener Python y las dependencias requeridas instaladas en el servidor.

2. Transfiere los archivos de la aplicación al servidor en la ubicación deseada.

3. Abre una terminal en el servidor y navega hasta el directorio de la aplicación.

4. Activa el entorno virtual ejecutando el comando apropiado para tu sistema operativo.

5. Ejecuta el siguiente comando para iniciar el servidor Flask:
   ```
   flask run
   ```

6. Configura tu servidor web para redirigir las solicitudes al servidor Flask. Consulta la documentación de tu servidor web para obtener instrucciones detalladas sobre cómo hacerlo.

7. Visita la URL del servidor en tu navegador web para ver la aplicación en funcionamiento.

## Personalización y ajustes adicionales

- Puedes modificar las plantillas HTML en el directorio "templates" para personalizar el aspecto de la aplicación.
- Realiza pruebas exhaustivas en tu entorno de desarrollo antes de realizar el despliegue en producción.
- Asegúrate de proteger tu aplicación en producción mediante el uso de medidas de seguridad apropiadas, como autenticación y autorización adecuadas, validación de formularios, etc.
