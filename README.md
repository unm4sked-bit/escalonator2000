# Escalonador de Processos

Neste trabalho, implementamos três algoritmos de escalonamento de processos, sendo eles: alternância circular, prioridade e loteria.


# Classes

O projeto é composto de cinco classes, a **Scheduler**, a **Process** e uma classe pra cada algoritmo, **Raffle** para o algoritmo de loteria, **Priority** para o de prioridade e **Cyclic** para o de alternância circular.

## Process (classes/process.py)

Essa classe é utilizada para guardar as informações de cada um dos processos. 

| Atributo       |Valor                         |
|----------------|-------------------------------|
|`name`|O nome do processo.|
|`pid`|O id do processo ou _process id_.|
|`execTime`|O tempo de execução que o processo precisa.|
|`priority`|A prioridade ou número de bilhetes (caso da loteria) do processo.|
|`uid`|O id do usuário dono do proceso.|
|`memory`|Quantidade de memória que o processo demanda para execução.|

## Algorithms (classes/algorithms.py)

As classes de algoritmos todas segue o padrão de métodos da tabela a seguir:

| Método       | Utilidade                      |
|----------------|-------------------------------|
|`fromString`|Gera um processo em função de uma string onde os atributos são separados por `|`. O padrão é: `nomeProcesso|PID|tempoDeExecução|prioridade (ou bilhetes)|UID|qtdeMemoria`|
|`insert`|Insere um processo na lista.|
|`next`|Escolhe um processo e remove da lista..|

Além disso, elas tem apenas um atributo:
| Atributo       | Valor                      |
|----------------|-------------------------------|
|`PROCESSES`|Mantém os processos. O tipo depende do algoritmo, é uma lista no **Raffle** e no **Cyclic**, mas é uma _priority queue_ no **Priority**.|

### Cyclic
No caso desse algoritmo, os processos são mantidos em uma lista, cada **insert** apenas insere um novo processo no fim da lista enquanto uma chamada de **next** remove o primeiro item da lista para execução.

### Priority
Nessa implementação, usamos uma fila de prioridade (_priority queue_) para adicionar ou escolher os processos. Usamos a prioridade mais alta como fator decisivo, por isso salvamos tuplas com valor (-prioridade do processo, referência do processo), afinal, a *heapq* implementada por padrão no Python é uma _min priority queue_.

### Raffle
No algoritmo de loteria, somamos todas quantidades de bilhetes para termos um total, em seguida, sorteamos um valor entre 1 e esse total. Após isso, iteramos os processos da lista somando a quantidade de bilhetes de cada um, quando essa quantidade alcança ou ultrapassa o valor sorteado, o processo da iteração atual é escolhido.

## Scheduler

Essa classe é responsável por aceitar entrada de novos processos, além de utilizar as classes anteriores para executar os processos.

Ela é composta por dois atributos:
| Atributo       | Valor                      |
|----------------|-------------------------------|
|`table`|Mantém referência para a classe do algoritmo escolhido.|
|`cputime`|O tempo que cada processo recebe quando é escolhido para execução.|

Os métodos são:
| Método       | Utilidade                      |
|----------------|-------------------------------|
|`run`|Executa os processos pendentes até eles acabarem.|
|`inputListener`|Lê novos processos do arquivo `newprocess.txt` quando o usuário aperta `Enter` no terminal.|
