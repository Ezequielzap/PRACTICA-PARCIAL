#
def verificar_tesoro(mapa:list,x:int,y:int)->int:
    if mapa[x][y] == 1:
        respuesta = 0
    else:
        distancia = (x - 1) + (y - 3)
        respuesta = distancia
    return respuesta

mapa = [[0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0] ]

seguir = "s"
while seguir ==  "s":
    x = int(input("ingrese la fila (0-4): "))
    while x < 0 or x > 4:
        x = int(input("error,ingrese la fila (0-4): "))
    y = int(input("ingrese la columna (0-4): "))
    while y < 0 or y > 4:
        y = int(input("error,ingrese la columna (0-4): "))
    respuesta = verificar_tesoro(mapa,x,y)

    if respuesta == 0:
        print("¡Encontraste el tesoro!")
        break
    else:
        print(f"Fallaste. El tesoro está a {respuesta} casilleros de distancia.")

    seguir = input("quiere seguir buscando el tesoro ?: ")

