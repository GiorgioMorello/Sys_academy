import json
from functions import exibirM, clear_s, add_user, listar_alunos, buscar_aluno, filtrar_aluno_imc
from random import randint
option = 0
# O arquivo .JSON deve conter um array vazia antes de executar o arquivo "main.py"


while (option != 5):


    exibirM()
    try:
        option = int(input("Digite a opção: "))
    except:
        print("Digite apenas números")

    if option == 1:
        # Abriremos o arquivo JSON e pegamos os dados dele e adicionamos em uma variavel
        with open('dados_alunos.json') as f:
            dados = json.load(f)  # a variavel "dados" é uma lista

        user = add_user()  # Vai receber o resultado da função que é um dic
        # Vai me retornar um número aleatório entre 0 a 999 e colocar no ID do usuário
        user['ID'] = randint(0, 999)

        # Adicionamos na lista os dados que o usuário cadastrou
        dados.append(user)

        # Abriremos o arquivo JSON e adicionamos a variavel "dados" dentro do arquivo JSON
        with open('dados_alunos.json', 'w', encoding='utf8') as file:
            json.dump(dados, file, indent=4, ensure_ascii=True)


    elif option == 2:
        # Executamos a função listar_alunos
        listar_alunos('dados_alunos.json')



    elif option == 3:
        # Pedimos para o usuário digitar o ID do usuário que deseja buscar
        id = int(input("Digite o ID do usuário: "))
        buscar_aluno(id)


    elif option == 4:
        # Executamos a função filtra_aluno_imc
        filtrar_aluno_imc()

    elif option == 5:
        break
    else:

        clear_s()
