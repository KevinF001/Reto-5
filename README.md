# Reto-5
# Caso 1
Para este caso se crea una carpeta que contiene dos elementos; por un lado una carpeta llamada Paquete_figura que contiene el modulo ClassShape y __init__.py, en ClassShape es donde se desarrolla todo el programa principal. Además de Paquete_figura tambien hay otro modulo correspondiente a main, en este se ejecuta el codigo con una importación desde ClassShape. De esta manera el codigo esta contenido en un solo paquete. 
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
En este caso hay una carpeta principal en la cual estan contenidos todos los modulos, para empezar el modulo __init__.py que es el encargado de hacer saber a Python que se esta creando un paquete; luego el programa principal esta partido en tres modulos: Shape, Rectangle y Triangle, en ellos se ejecuta paso a paso el codigo que al final es llamado con el modulo main. De esta manera tambien se crea un solo paquete pero con mayor modularidad.
```
Caso_2/
├── Shape/
│   ├── __init__.py
│   │── point.py
│   │── line.py
│   │── shape.py
│   └── Polygons/
│   │   │   │── __init__.py
│   │   │   │── Equilateral.py
│   │   │   │── Isosceles.py
│   │   │   │── Rectangle.py
│   │   │   │── Scalene.py
│   │   │   │── Square.py
│   │   │   │── Triangle.py
│   │   │   
```

