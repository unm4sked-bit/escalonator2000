from classes.process import Process
from classes.scheduler import Scheduler
from classes.algorithms import Raffle, Priority, Cyclic
from pprint import pprint

algSelector = {
    'loteria': Raffle,
    'prioridade': Priority,
    'alternanciaCircular': Cyclic
}

# lê o arquivo com a lista de processos e retorna dict com lista de processos e informacoes
def lerProcessos(path_arquivo):
    with open(path_arquivo, 'r') as texto:
        linhas = texto.readlines()
    
    # algoritmo / cpu
    meta = linhas[0].split("|")

    return {
        "alg": meta[0],
        'time': float(meta[1]),
        "processos": [Process.fromString(linha) for linha in linhas[1:]]
    }

def demo():
    loteria = lerProcessos("examples/loteria.txt")
    alternancia = lerProcessos("examples/alternancia.txt")
    prioridade = lerProcessos("examples/prioridades.txt")

    LOT = Scheduler(
        loteria['processos'],
        loteria['time'],
        algSelector[loteria['alg']]
    )
    ALT = Scheduler(
        alternancia['processos'],
        alternancia['time'],
        algSelector[alternancia['alg']]
    )
    PRI = Scheduler(
        prioridade['processos'],
        prioridade['time'],
        algSelector[prioridade['alg']]
    )

    #print("LOTERIA")
    #LOT.run()

    #print("ALTERNANCIA")
    #ALT.run()

    print("PRIORIDADE")
    PRI.run()

demo()


