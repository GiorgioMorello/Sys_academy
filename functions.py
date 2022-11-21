import os
import json
import pprint
# O arquivo .JSON deve conter um array vazia antes de executar o arquivo "main.py"


def exibirM():
    print("[1] Cadastrar novo aluno")
    print("[2] Exibir lista de alunos")
    print("[3] Buscar aluno por ID")
    print("[4] Filtrar alunos pelo IMC > 30")
    print("[5] Sair")


def add_user():
    nome = input("Nome do usuário: ").title()
    telefone = int(input("Número de telefone: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
    mensal = float(input("Mensalidade: "))
    sexo = str(input("Sexo ('M' ou 'F'): "))

    # Adicionamos todos os dados em um dicionário
    user = {
        "ID": 0,
        "nome": nome,
        "telefone": telefone,
        "peso": peso,
        "altura": altura,
        "mensalidade": mensal,
        "sexo": sexo
    }

    return user


def listar_alunos(nome_arq_json):
    # Estamos abrindo o arquivo, pegamos os dados(lista e dicts) dele e transformamos em python e armazenamos em uma variavel
    with open(nome_arq_json) as file:
        dados = json.load(file)

    # Percorremos a lista e imprimimos os dados de todos os usuários
    for usuario in dados:
        print(f"Nome: {usuario['nome']} ID: {usuario['ID']}")
        print()


def buscar_aluno(id):
    with open('dados_alunos.json') as f:
        dados = json.load(f)

# Percorremos a lista e verificamos se o ID digitado pelo usuário existe dentro do arquivo.
    # Se existir ele vai nos retornar a uma lista com os dados do usuario(dict)
    ids = [user for user in dados if str(id) == str(user['ID'])]
    if ids:
        pprint.pprint(ids[0]) # Imprimindo os dados do usuário
        print()
    else:
    # Se a lista estiver vazia significa que o ID que o usuário digitou não existe
        print("ID inválido")
        print()






def filtrar_aluno_imc():
    print("Alunos com IMC > 30")
    with open('dados_alunos.json') as f:
        dados = json.load(f)
    for usuario in dados:
        # Cálculo do IMC
        alt = usuario['altura'] ** 2
        peso = usuario['peso']
        imc = peso / alt
        if imc > 30:  # Se o IMC do usuário for > 30 imprimimos na tela os dados do usuário
            print(f"Nome: {usuario['nome']} ID: {usuario['ID']}")




def clear_s():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

