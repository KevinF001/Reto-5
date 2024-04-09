# Reto-5
# Caso 1
En este caso, se organiza el código de manera sencilla y eficiente en un único paquete. Se crea una carpeta principal llamada Caso_1, que contiene dos elementos principales. Por un lado, una subcarpeta llamada Paquete_figura, que contiene el módulo ClassShape.py y un archivo __init__.py. En ClassShape.py se encuentra todo el código principal del programa. Además, fuera de la subcarpeta Paquete_figura, se encuentra el archivo main.py, desde donde se ejecuta el código principal mediante una importación desde ClassShape.py. De esta manera, todo el código está contenido en un solo paquete.
```
Caso_1/
|
├── Paquete_figura/
|      |
│      ├── __init__.py
│      └── ClassShape.py
└── main.py
```
# Caso 2
En este caso, se organiza el código en una estructura de paquetes y módulos. Se crea una carpeta principal llamada Caso_2, que contiene un archivo __init__.py. Dentro de esta carpeta, hay una subcarpeta llamada ClassShape, que contiene los módulos necesarios para definir las figuras geométricas. Cada figura geométrica tiene su propio archivo, como Shape.py, Rectangle.py y Triangle.py. Estos archivos contienen las clases correspondientes a cada figura geométrica. Además, en la carpeta ClassShape se incluye un archivo __init__.py. Finalmente, fuera de la carpeta ClassShape, se encuentra el archivo main.py, desde donde se ejecuta el código principal.
```
Caso_2/
|
├── __init__.py
|
├── ClassShape/
|   |
│   ├── __init__.py
│   ├── Shape.py
│   ├── Rectangle.py
│   └── Triangle.py
│    
└── main.py      
```

