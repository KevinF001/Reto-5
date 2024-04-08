from ClassShape.Shape import Shape, Point, Line
from ClassShape.Rectangle import Rectangle, Square
from ClassShape.Triangle import Triangle, Equilateral, Isosceles, Scalene, RectangleTriangle


def main():
    fo = Shape() 

    print("   -Bienvenido- \n El siguiente programa permite analizar cuadrados, rectangulos y triangulos a partir de sus vertices, por favor ingrese datos coherentes. \n")
    while True:
        x = int(input("Ingrese la cantidad de cordenadas de su figura (vertices), si desea salir selecione 1: \n ")) 
        if x == 4:
            fo.initialize_shape(x) 
            vertices = fo.get_vertices() 
            sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
            rectangulo = Rectangle()

            if sum(sides)/4 == sides[0]: 
                cu = Square()
                diagonal_1 = Line(Point(vertices[0][0], vertices[0][1]), Point(vertices[2][0], vertices[2][1])).length()
                diagonal_2 = Line(Point(vertices[1][0], vertices[1][1]), Point(vertices[3][0], vertices[3][1])).length()
                if diagonal_1 != diagonal_2:
                    raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

                print(f"\n La figura corresponde a un cuadrado de lados {sides[0]} con vertices en las cordenadas: {fo.get_vertices()} ")
                print(f"   Su perimetro es de: {cu.compute_perimeter()} y su área de {cu.compute_area()}")
                print(f"   Es una figura {cu.regular()}  y sus angulos internos son: {cu.compute_angles()} \n")

            elif sides[0] == sides[2] and sides[1] == sides[3]:
                diagonal_1 = Line(Point(vertices[0][0], vertices[0][1]), Point(vertices[2][0], vertices[2][1])).length()
                diagonal_2 = Line(Point(vertices[1][0], vertices[1][1]), Point(vertices[3][0], vertices[3][1])).length()
                if diagonal_1 != diagonal_2:
                    raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

                print(f"\n La figura corresponde a un rectangulo de lados {sides[0]} x {sides[1]} con vertices en las cordenadas: {fo.get_vertices()} ")
                print(f"   Su perimetro es de: {rectangulo.compute_perimeter()} y su área de: {rectangulo.compute_area()}")
                print(f"   Es una figura {rectangulo.regular()}  y sus angulos internos son: {rectangulo.compute_angles()} \n")

            else:
                raise ValueError("La figura no es un rectangulo ni un cuadrado, por favor ingrese datos validos")

        elif x == 3:  
            fo.initialize_shape(x)
            vertices = fo.get_vertices()
            sides = [Line(Point(vertices[i][0], vertices[i][1]), Point(vertices[(i + 1) % len(vertices)][0], vertices[(i + 1) % len(vertices)][1])).length() for i in range(len(vertices))]
            triangulo = Triangle()

            if triangulo.triangle_type() == "Equilatero":
                if sum(triangulo.compute_angles()) != 180 and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[1]) and round(triangulo.compute_angles()[0]) != round(triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    eq = Equilateral()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo equilátero con todos sus lados de valor {sides[0]} por lo que es una figura {triangulo.regular()}")
                    print(f" Su perímetro es de: {eq.compute_perimeter()} y su área de: {eq.compute_area()}")
                    print(f" Sus ángulos internos son: {eq.compute_angles()} \n")

            elif triangulo.triangle_type() == "Isosceles":
                if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] != triangulo.compute_angles()[1] and triangulo.compute_angles()[0] != triangulo.compute_angles()[2] and triangulo.compute_angles()[1] != triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    iso = Isosceles()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo isósceles de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()}  ")
                    print(f"   Su perímetro es de: {iso.compute_perimeter()} y su área es: {iso.compute_area()}")
                    print(f"   Sus ángulos internos son: {iso.compute_angles()} \n ")

            elif triangulo.triangle_type() == "Escaleno":
                if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] == triangulo.compute_angles()[1] or triangulo.compute_angles()[0] == triangulo.compute_angles()[2] or triangulo.compute_angles()[1] == triangulo.compute_angles()[2]):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    es = Scalene()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde con un triángulo escaleno de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()} ")
                    print(f"   Su perímetro es de: {es.compute_perimeter()} y su área es: {es.compute_area()}")
                    print(f"   Sus ángulos internos son: {es.compute_angles()} \n ")

            elif triangulo.triangle_type() == "Rectangulo":
                if round(sum(triangulo.compute_angles())) != 180 or (triangulo.compute_angles()[0] != 90 and triangulo.compute_angles()[1] != 90 and triangulo.compute_angles()[2] != 90):
                    raise ValueError("Los datos ingresados no corresponden a un triangulo")
                else:
                    rec = RectangleTriangle()
                    print(f"\n La figura con cordenadas: {fo.get_vertices()} corresponde a un triángulo rectángulo de lados: {sides[0]}, {sides[1]}, {sides[2]} por lo que es  una figura {triangulo.regular()} ")
                    print(f"   Su perímetro es de: {rec.compute_perimeter()} y su área de: {rec.compute_area()}")
                    print(f"   Sus ángulos internos son: {rec.compute_angles()} \n ")

            else:
                raise ValueError("Los datos ingresados no corresponden a un triangulo")

        elif x == 1:  
            break

        else:    
            raise ValueError("Opción no válida")
        
if __name__ == "__main__":
    main()

