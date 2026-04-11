# Objetivo aqui é criar, manipular e formatar dados básicos utilizando variáveis e tipos de dados em Python.

def main():
      # 01 -Criando variáveis para armazenar informações pessoais
      nome = "MARIA SILVA DOS SANTOS"
      idade = "25"
      salario = "3500.00"
      ativo = "True"

      # 02 - Convertendo os tipos e formatos de dados para os tipos corretos
      nome = nome.title()
      idade = int(idade)
      salario = float(salario)
      ativo = ativo.lower() == "true"

      # 03 - Exibindo as informações formatadas
      print()
      print("===== Informações Pessoais =====")
      print(f"Nome: {nome}\n"
            f"Idade: {idade} anos\n"
            f"Salário: R$ {salario:.2f}".replace(".", ",") + "\n"
            f"Ativo: {ativo}\n")

if __name__ == "__main__":
    main()
