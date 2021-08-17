import math

def main():
    #escribe tu código abajo de esta línea
    ap = float(input("Area a pintar en metros: "))
    r = float(input("Rendimiento (m2/l): "))
    cl = math.ceil(ap/r)
    print("Litros a comprar:",cl)


if __name__ == '__main__':
    main()
