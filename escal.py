from classes.process import Process
from classes.scheduler import Scheduler
from classes.algorithms import Raffle, Priority, Cyclic
from pprint import pprint



# lê o arquivo com a lista de processos e retorna dict com lista de processos e informacoes
def lerProcessos(path_arquivo):
    with open(path_arquivo, 'r') as texto:
        linhas = texto.readlines()
    
    # algoritmo / cpu
    meta = linhas[0].split("|")

    return {
        "tipo": (meta[0], float(meta[1])),
        "processos": [Process.fromString(linha) for linha in linhas[1:]]
    }

def demoPrioridade():
    
    # lista de processos que será iterada sobre
    for alg in [Cyclic, Priority, Raffle]:
        escalonador = lerProcessos("examples/loteria.txt")
        print("KEK")
        A = Scheduler(
            escalonador['processos'],
            8,
            Cyclic
        )
        A.run()

demoPrioridade()


