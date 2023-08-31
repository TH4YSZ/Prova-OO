from Classes import *
import os

def main():
    os.system("cls")
    sair = False
    conttrf = 0

    to_do = ToDoList("TO-DO")
    while sair == False:
        try:
            print("BEM-VINDO AO TO-DO, UM SOFTWRE DE LISTA DE TAREFAS!")
            menu = int(input("[1] Adicionar tarefa \n[2] Listar tarefa \n[3] Excluir tarefa \n[4] Sair \nDigite a opção desejada: "))
            match menu:
                case 1:
                    os.system("cls")
                    conttrf += 1
                    num = conttrf
                    tarefa = input("Escreva a tarefa que deseja adicionar: ")
                    to_do.adicionar_tarefa(num, tarefa)
                    print("\n Tarefa adicionada com sucesso!")
                    os.system("pause")
                    os.system("cls")
                case 2:
                    os.system("cls")
                    print("Lista de tarefas: \n")
                    to_do.listar_tarefa()
                    os.system("pause")
                    os.system("cls")
                case 3:
                    os.system("cls")
                    print("Lista de tarefas: \n")
                    to_do.listar_tarefa()

                    indice = int(input("\nQual tarefa deseja excluir?: "))
                    to_do.excluir_tarefa(indice)
                    print("\nTarefa excluída com sucesso! ")
                    os.system("pause")
                    os.system("cls")
                case 4:
                    sair = True
        except Exception as erro:
            print("Opção inválida")
            print(erro.__class__.__name__)