# lista de tarefas
tarefas = []

while True:
    # usuário informa o nome da nova tarefa
    nova_tarefa = input('Informe o nome da nova tarefa: ')

    # nova tarefa é inserida na lista
    tarefas.append(nova_tarefa)
    
    # pergunta se quer continuar a inserção de tarefas
    retorno = input('Deseja cadastrar nova tarefa?(s/n)')

    # se a resposta for Sim, então adiciona novamente
    if retorno == 's':
        continue
    else: # senão, imprima as tarefas
        #print(tarefas)
        break

for tarefa in tarefas:
    print(tarefa)