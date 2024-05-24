# lista de tarefas
tarefas = []

while True:
    # usuário informa o nome da nova tarefa
    nova_tarefa = input('Informe anova tarefa ou tecle Enter para encerrar e exibir a lista: ')
    
  # se a resposta for Sim, então adiciona novamente
    if nova_tarefa != '':
        # nova tarefa é inserida na lista
        tarefas.append(nova_tarefa)
        continue
    else: # senão, imprima as tarefas
        #print(tarefas)
        break
# exibe a lista de tarefas
for tarefa in tarefas:
    print(tarefa)