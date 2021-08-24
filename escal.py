from classes.process import Process
from classes.scheduler import Scheduler
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
    for alg in ["loteria", "alternancia", "prioridade"]:
        escalonador = lerProcessos("examples/loteria.txt")
        print(alg.upper())
        A = Scheduler(alg, escalonador['processos'], 8)
        A.run()

demoPrioridade()


