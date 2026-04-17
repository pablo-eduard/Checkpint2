import os
import time


def menu_inicial():
    print("-----------Lista da Tarefas-----------")
    print("Opção Disponivéis: ")
    print("1) Criar nova tarefa.")
    print("2) Ver tarefas.")
    print("3) Atualizar tarefa.")
    print("4) Deletar tarefa.")
    print("-----------Por Pablo Éduard-----------")

    opcao=int(input("Escolha uma opção: "))
    return opcao

def escolher_opcao(opcao):
    match opcao:
        case 1:
        adicionar_tarefa=str(input("O que você gostaria de adicionar com tarefa? "))