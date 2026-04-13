"""
Exercício 04: Funções e Escopo
Objetivo: Criar funções reutilizáveis para cálculos financeiros.
"""

def formatar_moeda(valor: float) -> str:
    """
    Formata um valor numérico para o padrão brasileiro (R$ 1.234,56).
    
    Args:
        valor (float): O valor numérico a ser formatado.
        
    Returns:
        str: O valor formatado como string.
    """
    # TODO: Implemente sua lógica de formatação aqui
    # Dica: Use f-string e replace
    return f"R$ {valor:.2f}".replace(".", ",")   

def calcular_imposto(valor: float, taxa: float = 0.15) -> float:
    """
    Calcula o valor do imposto com base na taxa.
    
    Args:
        valor (float): Valor base.
        taxa (float): Taxa de imposto em decimal (padrão: 0.15).
        
    Returns:
        float: O valor do imposto calculado.
    """
    return valor * (1 + taxa)
    

def calcular_desconto(valor: float, percentual: float) -> float:
    """
    Aplica um desconto sobre um valor.
    
    Args:
        valor (float): Valor original.
        percentual (float): Percentual de desconto (ex: 10.0 para 10%).
        
    Returns:
        float: O novo valor com desconto aplicado.
    """
    return valor - (valor * (percentual / 100))
    pass

def calcular_salario_liquido(salario_bruto: float) -> dict:
    """
    Calcula o salário líquido aplicando INSS e IRRF simplificados.
    
    Regras:
    - INSS: 8% sobre o bruto.
    - IRRF: 15% sobre o bruto (se bruto > 2000), senão 0.
    
    Args:
        salario_bruto (float): Salário bruto do funcionário.
        
    Returns:
        dict: Dicionário com 'bruto', 'inss', 'irrf' e 'liquido'.
    """
    # TODO: Implemente a lógica
    # inss = ...
    # irrf = ...
    # liquido = ...
    # return {...}
    pass

# ==========================================
# BLOCO DE TESTES (NÃO ALTERE ABAIXO)
# ==========================================

if __name__ == "__main__":
    print("=== TESTANDO FUNÇÕES ===\n")

    # Teste 1: Formatação
    print("1. Formatação:")
    print(f"   {formatar_moeda(1500.50)}")
    print(f"   {formatar_moeda(12000.00)}")

    # Teste 2: Imposto (padrão 15%)
    print("\n2. Imposto (15%):")
    print(f"   Imposto sobre 1000: {formatar_moeda(calcular_imposto(1000))}")
    print(f"   Imposto sobre 5000: {formatar_moeda(calcular_imposto(5000))}")
    print(f"   Imposto sobre 5000 (com taxa 0.20): {formatar_moeda(calcular_imposto(5000, 0.20))}")

    # Teste 3: Desconto
    print("\n3. Desconto:")
    print(f"   500 com 10% de desconto: {formatar_moeda(calcular_desconto(500, 10))}")

    # Teste 4: Salário Líquido (Complexo)
    print("\n4. Salário Líquido:")
    salarios = [1500.00, 2500.00, 4000.00]
    
    for sal in salarios:
        resumo = calcular_salario_liquido(sal)
        print(f"   Bruto: {formatar_moeda(resumo['bruto'])}")
        print(f"   INSS: -{formatar_moeda(resumo['inss'])}")
        print(f"   IRRF: -{formatar_moeda(resumo['irrf'])}")
        print(f"   Líquido: {formatar_moeda(resumo['liquido'])}")
        print("   ---")