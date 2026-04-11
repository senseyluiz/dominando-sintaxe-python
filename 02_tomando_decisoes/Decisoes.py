# Tomando decisões em Python utilizando estruturas condicionais
# Objetivo: Classificar dados usando condições

def formatar_valor_brl(valor):
    """Formata um valor numérico para o formato de moeda brasileira (exemplo: R$ 1.234,56)."""
    return f"R$ {valor:.2f}".replace(".", ",")

def main():
    pedidos = [
        {"id": 1, "status": "pago", "valor": 150.00},
        {"id": 2, "status": "pendente", "valor": 200.00},
        {"id": 3, "status": "cancelado", "valor": 50.00},
        {"id": 4, "status": "pago", "valor": 300.00},
        {"id": 5, "status": "pendente", "valor": 120.00}
    ]

    total_pedidos = len(pedidos)
    pedidos_pagos = 0
    pedidos_pendentes = 0
    pedidos_cancelados = 0
    faturament_total = 0.0


    for pedido in pedidos:
        if pedido["status"] == "pago":
            pedidos_pagos += 1
            faturament_total += pedido["valor"]
            print(f"Pedido {pedido['id']} liberado para envio. Valor: {formatar_valor_brl(pedido['valor'])}")
        elif pedido["status"] == "pendente":
            pedidos_pendentes += 1
            print(f"Pedido {pedido['id']} aguardando pagamento. Valor: {formatar_valor_brl(pedido['valor'])}")
        elif pedido["status"] == "cancelado":
            pedidos_cancelados += 1
            print(f"Pedido {pedido['id']} foi cancelado. Valor: {formatar_valor_brl(pedido['valor'])}")
        else:
            print(f"Pedido {pedido['id']} tem um status desconhecido. Valor: {formatar_valor_brl(pedido['valor'])}")


    print("\n===== Resumo dos Pedidos =====")
    print()
    print(f"Total de pedidos: {total_pedidos}")
    print(f"Pedidos pagos: {pedidos_pagos}")
    print(f"Pedidos pendentes: {pedidos_pendentes}")
    print(f"Pedidos cancelados: {pedidos_cancelados}")
    print(f"Faturamento total: {formatar_valor_brl(faturament_total)}")

if __name__ == "__main__":
    main()