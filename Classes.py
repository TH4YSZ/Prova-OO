class ToDoList():
    def __init__(self, nome):
        self.tarefas = {}
    
    def adicionar_tarefa(self, num, tarefa):
        self.tarefa = tarefa
        self.tarefas[num] = [self.tarefa]

    def listar_tarefa(self):
        for chave, valor in self.tarefas.items():
            print(f"{chave}. {valor}")
    
    def excluir_tarefa(self, indice):
        self.indice = indice