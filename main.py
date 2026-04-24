import os
import time
from tarefas import adicionar_tarefas, listar_tarefas, concluir_tarefa, carregar_dados


tempo= 2
carregar_dados()

while True:
    
    print("------Bem Vindo a Lista de Tarefas------")
    print("1)Adicionar")
    print("2)Listar")
    print("3)Concluir")
    print("4)Sair")

    opcao=input("Digite uma opção valida: ")
    
    match opcao:
        case "1":
            tarefa = input("Qual a nova tarefa? ")
            adicionar_tarefas(tarefa)
            print("Tarefa adicionada✅")
            time.sleep(tempo)
            os.system('cls')
        
        case "2":
            listar_tarefas()
            time.sleep(tempo)
            os.system('cls')
        case "3":
            numero=int(input("Digite um número dá Tarefa: "))
            concluir_tarefa(numero)
        case "4":
            print("Desligando sistema")
            break

