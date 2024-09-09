Verificador de URL de Phishing

Este proyecto es una aplicación web creada con Flask que permite verificar si una URL es potencialmente un sitio de phishing o es segura. Utiliza un modelo de aprendizaje automático basado en Naive Bayes para realizar la predicción, y un gráfico interactivo para mostrar los resultados.

Funcionalidades:

Entrada de URL: El usuario puede introducir una URL en un formulario para su análisis.

Detección de Phishing: El sistema analiza la URL ingresada y predice si es de phishing o no.

Gráfico dinámico: Un gráfico de barras que visualiza el resultado de la detección.

Interfaz amigable: Una interfaz sencilla con estilos CSS personalizados.

Estructura de archivos:

app.py: Archivo principal que maneja las rutas y la lógica del servidor Flask.

phishing_model.py: Entrenamiento del modelo de Naive Bayes con los datos de URLs de phishing y seguras.

templates/index.html: Página principal donde el usuario ingresa la URL y se muestran los resultados.

static/styles.css: Hoja de estilos para la apariencia del sitio.

phishing_data.csv: Dataset con ejemplos de URLs y su clasificación (0 = No Phishing, 1 = Phishing).

model.pkl y vectorizer.pkl: Archivos serializados del modelo entrenado y el vectorizador de características.

Instrucciones:

Entrena el modelo ejecutando phishing_model.py.

Inicia la aplicación con app.py.

Accede a la interfaz web y verifica URLs.
