# Objetivo aqui é criar, manipular e formatar dados básicos utilizando variáveis e tipos de dados em Python.

# 01 -Criando variáveis para armazenar informações pessoais
nome = "MARIA SILVA DOS SANTOS"
idade = "25"
salario = "3500.00"
ativo = "True"

# 02 - Convertendo os tipos e formatos de dados para os tipos corretos
nome = nome.title()
idade = int(idade)
salario = float(salario)
ativo = ativo == "True"

# 03 - Exibindo as informações formatadas
print("\n")
print("===== Informações Pessoais =====")
print(f"Nome: {nome}\n"
      f"Idade: {idade} anos\n"
      f"Salário: R$ {salario:.2f}\n"
      f"Ativo: {ativo}\n")
