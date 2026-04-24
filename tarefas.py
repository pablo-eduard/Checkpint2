import json
import time
import os

tempo=2

lista_tarefas=[]

def adicionar_tarefas(descricao):
    nova_tarefa={
        "descrição" : descricao,
        "concluida" : False
    }
    lista_tarefas.append(nova_tarefa)
    salvar_dados()

def listar_tarefas():
    for i, tarefa in enumerate(lista_tarefas):
        if tarefa["concluida"]==True:
            simbolo="[X]"
        else:
            simbolo="[]"
        print(f"{i+1}){simbolo} {tarefa["descrição"]}")

def concluir_tarefa(indice):
    try:
        posicao=indice-1

        lista_tarefas[posicao]["descrição"]=True
        print("Tarefa marcada como feita!") 
        time.sleep(2)
        os.system('cls')
    except:
        print("Número dá tarefa invalido")

def salvar_dados():
    with open("tarefas.json", "w") as arquivo:
        json.dump(lista_tarefas, arquivo)


def carregar_dados():
        global lista_tarefas
        try:
            with open("tarefas.json", "r") as arquivo:
                lista_tarefas = json.load(arquivo)
        
        except(FileNotFoundError, json.JSONDecodeError):
            lista_tarefas = []


