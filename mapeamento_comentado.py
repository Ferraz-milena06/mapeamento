# Simulador de algoritmos de substituição de páginas
# Autora: Milena Ferraz, Leonardo Pereira, Eduardo Erthal  
# Algoritmos implementados: FIFO, LRU e MRU

from collections import deque  

# ---------- FIFO ----------
def fifo(paginas, quantidade_quadros):
    quadros = deque()  # aqui vão ficar as páginas na memória
    faltas = 0  # contador de faltas de página (quando precisa carregar uma nova)

    for pagina in paginas:
        # se a página não está na memória, deu falta
        if pagina not in quadros:
            faltas += 1
            # confere se tem espaço livre
            if len(quadros) < quantidade_quadros:
                quadros.append(pagina)
            else:
                # se já estiver cheio, tira a mais antiga (a que entrou primeiro)
                quadros.popleft()
                quadros.append(pagina)
    # devolve as páginas que ficaram na memória e quantas faltas deu
    return list(quadros), faltas


# ---------- LRU ----------
def lru(paginas, quantidade_quadros):
    quadros = []  # páginas carregadas na memória
    recentes = {}  # guarda o índice da última vez que cada página foi usada
    faltas = 0

    for indice, pagina in enumerate(paginas):
        if pagina in quadros:
            # se a página já tá na memória, só atualiza o “último uso”
            recentes[pagina] = indice
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                # ainda tem espaço na memória, só adiciona
                quadros.append(pagina)
                recentes[pagina] = indice
            else:
                # precisa tirar a página menos usada recentemente
                pagina_lru = min(recentes, key=recentes.get)
                # substitui a velha pela nova
                quadros[quadros.index(pagina_lru)] = pagina
                # remove do dicionário e atualiza o novo uso
                del recentes[pagina_lru]
                recentes[pagina] = indice
    return list(quadros), faltas


# ---------- MRU ----------
def mru(paginas, quantidade_quadros):
    quadros = []
    recentes = {}  # igual no LRU, mas aqui a lógica é o contrário
    faltas = 0

    for indice, pagina in enumerate(paginas):
        if pagina in quadros:
            # se já tá na memória, atualiza o “último uso”
            recentes[pagina] = indice
        else:
            faltas += 1
            if len(quadros) < quantidade_quadros:
                # ainda tem espaço, só adiciona
                quadros.append(pagina)
                recentes[pagina] = indice
            else:
                # agora tiramos a mais recentemente usada (MRU)
                pagina_mru = max(recentes, key=recentes.get)
                quadros[quadros.index(pagina_mru)] = pagina
                del recentes[pagina_mru]
                recentes[pagina] = indice
    return list(quadros), faltas


# ---------- Testes ----------
#  sequências diferentes pra testar os algoritmos
sequencias = {
    "a": [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7],
    "b": [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11],
    "c": [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]
}

# qual página vamos procurar no final
consultas = {"a": 7, "b": 11, "c": 11}
quantidade_quadros = 8  # ou seja, a memória tem 8 espaços

# pra cada sequência, roda os três algoritmos e mostra o resultado
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
