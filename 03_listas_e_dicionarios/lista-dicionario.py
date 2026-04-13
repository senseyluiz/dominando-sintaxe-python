# Trabalhando com listas e dicionários

# Objetivo: Gerenciar um estoque simples.
def formatar_valor_brl(valor):
    """Formata um valor numérico para o formato de moeda brasileira (exemplo: R$ 1.234,56)."""
    return f"R$ {valor:.2f}".replace(".", ",")

def mostrar_estoque(estoque):
    print("\n===== Estoque Atual =====")
    for produto, detalhes in estoque.items():
        print(f"{produto.title()}: Quantidade: {detalhes['quantidade']} - Preco: {formatar_valor_brl(detalhes['preco'])}")

def adicionar_produto(estoque):
    nome_produto = input("Digite o nome do produto: ").lower()
    quantidade_produto = int(input("Digite a quantidade do produto: "))
    preco_produto = float(input("Digite o preco do produto: "))
    estoque[nome_produto] = {"quantidade": quantidade_produto, "preco": preco_produto}
    print(f"Produto {nome_produto.title()} adicionado ao estoque.")

def vender_produto(estoque):
    nome_produto = input("Digite o nome do produto a ser vendido: ").lower()
    if nome_produto in estoque:
        quantidade_venda = int(input("Digite a quantidade a ser vendida: "))
        if quantidade_venda <= estoque[nome_produto]["quantidade"]:
            estoque[nome_produto]["quantidade"] -= quantidade_venda
            valor_total = quantidade_venda * estoque[nome_produto]["preco"]
            print(f"Venda realizada! Valor total: {formatar_valor_brl(valor_total)}")
        else:
            print("Quantidade insuficiente em estoque.")
    else:
        print("Produto não encontrado no estoque.")

def main():
    estoque = {
        "notbook": {"quantidade": 5, "preco": 1500.00},
        "mouse": {"quantidade": 20, "preco": 89.90},
        "teclado": {"quantidade": 15, "preco": 150.00},
        "monitor": {"quantidade": 10, "preco": 1200.00}
    }

    print("\n===== MENU =====")
    print("1. Ver produtos em estoque")
    print("2. Adicionar novo produto")
    print("3. Vender produto")
    print("4. Sair")
    print()

    input_usuario = input("Escolha uma opcao: ")
    if input_usuario =="1":
        mostrar_estoque(estoque)
        
    elif input_usuario == "2":
        adicionar_produto(estoque)
        mostrar_estoque(estoque)
    elif input_usuario == "3":
        vender_produto(estoque)
        mostrar_estoque(estoque)
    elif input_usuario == "4":
        print("Saindo do programa...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()