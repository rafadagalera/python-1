# Crie um programa para ajudar a gerenciar as consultas em um hospital. O programa deve permitir que os funcionários do hospital cadastrem novos pacientes, agendem consultas, cancelem consultas e visualizem a lista de consultas para um determinado dia.
# O programa deve incluir funções como:
# - Cadastro de pacientes com informações básicas (nome, idade, número de telefone).
# - Agendamento de consultas com data e hora.
# - Verificação de disponibilidade para agendar uma nova consulta.
# - Cancelamento de consultas.
# - Visualização da lista de consultas para um dia específico.
# Além disso, você deve criar um algoritmo com funções, em especial, função def.
# Utilize estruturas inputs para usuários, estrutura de repetição e condição.
# Entregue o arquivo em python e mostre o que faz cada parte do código desenvolvido.

import pandas as pd

cadastro = {"Nome do paciente": [],
            "Idade": [],
            "Telefone": [],
            "Data da consulta": [],
            "Horário da consulta": []
            }

def cadastrar_paciente(nome,idade,telefone,data,horario):
    nome = str(input("Digite o nome do paciente: "))
    idade = int(input("Digite a idade do paciente: "))
    telefone = int(input("Digite o telefone do paciente: "))
    data = int(input("Para quando deseja marcar a consulta?"))
    horario = int(input("Qual o horário da consulta?"))
    cadastro["Nome do paciente"].append(nome)
    cadastro["Idade"].append(idade)
    cadastro["Telefone"].append(telefone)
    if data not in cadastro["Data da consulta"]:
        cadastro["Data da consulta"].append(data)
        cadastro["Horário da consulta"].append(horario)
    else:
        if horario not in cadastro["Horário da consulta"]:
            cadastro["Data da consulta"].append(data)
            cadastro["Horário da consulta"].append(horario)
        else:
            print("Este horário já está ocupado!")
    

