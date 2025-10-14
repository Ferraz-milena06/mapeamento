from collections import deque

def fifo(paginas, quantidade_quadros):
    quadros = deque()
    faltas = 0

    for pagina in paginas:
        if pagina not in quadros:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                quadros.popleft() 
                quadros.append(pagina)
    return list(quadros), faltas


def lru(paginas, quantidade_quadros):
    quadros = []
    recentes = {}  
    faltas = 0

    for indice, pagina in enumerate(paginas):
        if pagina in quadros:
            recentes[pagina] = indice
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
                recentes[pagina] = indice
            else:
                pagina_lru = min(recentes, key=recentes.get)
                quadros[quadros.index(pagina_lru)] = pagina
                del recentes[pagina_lru]
                recentes[pagina] = indice
    return list(quadros), faltas


def mru(paginas, quantidade_quadros):
    quadros = []
    recentes = {}  
    faltas = 0

    for indice, pagina in enumerate(paginas):
        if pagina in quadros:
            recentes[pagina] = indice
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
                recentes[pagina] = indice
            else:
                pagina_mru = max(recentes, key=recentes.get)
                quadros[quadros.index(pagina_mru)] = pagina
                del recentes[pagina_mru]
                recentes[pagina] = indice
    return list(quadros), faltas


sequencias = {
    "a": [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7],
    "b": [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11],
    "c": [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
}

consultas = {"a": 7, "b": 11, "c": 11}
quantidade_quadros = 8

for nome, paginas in sequencias.items():
    print(f"\n=== SEQUÊNCIA {nome} ===")
    for nome_algoritmo, funcao in [("FIFO", fifo), ("LRU", lru), ("MRU", mru)]:
        quadros, faltas = funcao(paginas, quantidade_quadros)
        pagina_consulta = consultas[nome]
        posicao = quadros.index(pagina_consulta) + 1 if pagina_consulta in quadros else None
        print(f"{nome_algoritmo}: Faltas = {faltas}, Quadros finais = {quadros}")
        if posicao:
            print(f" → Página {pagina_consulta} está no quadro {posicao}")
        else:
            print(f" → Página {pagina_consulta} não está na memória")
