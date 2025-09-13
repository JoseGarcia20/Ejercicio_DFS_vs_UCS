import heapq

# Laberinto

# '.': Camino libre
# '#': Obstaculo
LABERINTO_OFIC = [
    ['.', '.', '#', '#', '#'],
    ['#', '.', '.', '.', '#'],
    ['#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#']
]
PUNTO_INICIAL = (0, 0)
PUNTO_FINAL = (3, 4)

'''
# LABERINTO_PRUEBA
LABERINTO_OFIC = [
    ['.', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '#'],
    ['.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#']
]
PUNTO_INICIAL = (0, 0)
PUNTO_FINAL = (4, 2)
'''

# Algoritmos de busqueda

def es_valido(fila, col):
    """Verifica si una casilla esta dentro de los limites del laberinto y no es un obstaculo"""
    return 0 <= fila < 5 and 0 <= col < 5 and LABERINTO_OFIC[fila][col] == '.'

def obtener_vecinos(fila, col):
    """Obtiene los vecinos validos de una casilla"""
    vecinos = []
    # Define los movimientos del agente: arriba, abajo, izquierda, derecha
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nueva_fila, nueva_col = fila + dr, col + dc
        if es_valido(nueva_fila, nueva_col):
            vecinos.append((nueva_fila, nueva_col))
    return vecinos

def imprimir_laberinto_con_camino(camino):
    """Imprime el laberinto mostrando el camino encontrado."""
    laberinto_visual = [list(row) for row in LABERINTO_OFIC]
    for i, (fila, col) in enumerate(camino):
        if (fila, col) == PUNTO_INICIAL:
            laberinto_visual[fila][col] = 'A'
        elif (fila, col) == PUNTO_FINAL:
            laberinto_visual[fila][col] = 'B'
        else:
            # Marca el camino recorrdio por el agente con numeros del 1 al ...
            laberinto_visual[fila][col] = str(i % 10) 
            
    print("Paso a paso en el laberinto:")
    for row in laberinto_visual:
        print(" ".join(map(str, row)))

# Busqueda en Profundidad (DFS)
def dfs(inicio, final):
    """Encuentra un camino usando DFS y muestra el paso a paso."""
    pila = [(inicio, [inicio])]
    visitados = {inicio}

    while pila:
        (fila, col), camino = pila.pop()

        if (fila, col) == final:
            print("--- Resultado con DFS ---")
            print(f"Camino encontrado: {camino}")
            imprimir_laberinto_con_camino(camino)
            return

        for vecino in obtener_vecinos(fila, col):
            if vecino not in visitados:
                visitados.add(vecino)
                pila.append((vecino, camino + [vecino]))
    
    print("--- Resultado con DFS ---")
    print("No se encontro un camino.")

# Busqueda de Costo Uniforme (UCS)
def ucs(inicio, final):
    """Encuentra el camino de menor costo usando UCS y muestra el paso a paso."""
    frontera = [(0, inicio, [inicio])]  # (costo, (fila, col), camino)
    visitados = {inicio}

    while frontera:
        costo, (fila, col), camino = heapq.heappop(frontera)

        if (fila, col) == final:
            print("--- Resultado con UCS ---")
            print(f"Camino de menor costo encontrado: {camino}")
            print(f"Costo del camino: {costo}")
            imprimir_laberinto_con_camino(camino)
            return

        for vecino in obtener_vecinos(fila, col):
            if vecino not in visitados:
                visitados.add(vecino)
                nuevo_costo = costo + 1  # Costo uniforme de 1 por paso
                heapq.heappush(frontera, (nuevo_costo, vecino, camino + [vecino]))

    print("--- Resultado con UCS ---")
    print("No se encontro un camino.")


# Ejecucion Principal
if __name__ == "__main__":
    print("Laberinto Inicial:")
    for row in LABERINTO_OFIC:
        print(" ".join(map(str, row)))
    print(f"Punto Inicial (A): {PUNTO_INICIAL}")
    print(f"Punto Final (B): {PUNTO_FINAL}\n")
    
    # Validar que el punto inicial y final no sean obstaculos
    if LABERINTO_OFIC[PUNTO_INICIAL[0]][PUNTO_INICIAL[1]] == '#' or \
       LABERINTO_OFIC[PUNTO_FINAL[0]][PUNTO_FINAL[1]] == '#':
        print("Error: El punto inicial o final se encuentra en un obstaculo.")
    else:
        dfs(PUNTO_INICIAL, PUNTO_FINAL)
        print("\n" + "="*30 + "\n")
        ucs(PUNTO_INICIAL, PUNTO_FINAL)