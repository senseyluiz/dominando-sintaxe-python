"""
Exercício 05: Strings, Regex e Limpeza de Dados
Objetivo: Padronizar e validar campos de texto.
"""
import re

# Dados "sujos" de entrada (Simulando um extract de banco legado)
dados_sujos = [
    {"nome": "  joao  SILVA  ", "email": "Joao.Silva@Email.com", "cpf": "123.456.789-00", "telefone": "(11) 99887-7665"},
    {"nome": "MARIA   souza", "email": "maria.souza@email", "cpf": "987.654.321-00 ", "telefone": "21987654321"},
    {"nome": "  pedro almeida  ", "email": "  pedro@hotmail.com  ", "cpf": " 11122233344", "telefone": "(31) 91234-5678"},
]

def limpar_nome(nome: str) -> str:
    """
    Padroniza o nome: Remove espaços extras e coloca em Title Case.
    Ex: "  joao  SILVA  " -> "Joao Silva"
    """   
    nome = nome.strip()
    partes_nome = nome.split()
    nome_limpo = " ".join(partes_nome).title()
    return nome_limpo

def limpar_cpf(cpf: str) -> str:
    """
    Remove pontuação do CPF, deixando apenas números.
    Ex: "123.456.789-00" -> "12345678900"
    """
    cpf_limpo = re.sub(r'\D', '', cpf)
    return cpf_limpo

def formatar_telefone(telefone: str) -> str:
    """
    Formata o telefone para o padrão (XX) XXXXX-XXXX.
    Assume que o número tem 11 dígitos (DDD + 9 dígitos).
    Ex: "11998877665" -> "(11) 99887-7665"
    """  
    telefone_limpo = re.sub(r'\D', '', telefone)
    ddd = telefone_limpo[:2]
    parte1 = telefone_limpo[2:7]
    parte2 = telefone_limpo[7:11]
    telefone_formatado = f"({ddd}) {parte1}-{parte2}"
    return telefone_formatado

def validar_email(email: str) -> bool:
    """
    Valida se o email tem um formato básico aceitável.
    Regra simples: Deve ter '@' e um '.' depois do '@'.
    Ex: "nome@email.com" -> True
    Ex: "nome@email" -> False
    """    
    if '@' in email and '.' in email.split('@')[-1]:
        return True
    return "Email inválido"
    

def processar_dados(lista_dados: list) -> list:
    """
    Orquestra a limpeza de todos os registros.
    """
    dados_limpos = []
    
    for registro in lista_dados:        
        novo_nome = limpar_nome(registro['nome'])        
        if validar_email(registro['email']) == True:
            novo_email = registro['email'].strip()
        else:
            novo_email = "Email Inválido"        
        novo_cpf = limpar_cpf(registro['cpf'])
        novo_telefone = formatar_telefone(registro['telefone'])        
        novo_registro = {
            "nome": novo_nome,
            "email": novo_email,
            "cpf": novo_cpf,
            "telefone": novo_telefone
        }
        dados_limpos.append(novo_registro)
    return dados_limpos

# ==========================================
# BLOCO DE TESTES
# ==========================================

if __name__ == "__main__":
    print("=== DADOS ORIGINAIS (SUJOS) ===")
    for r in dados_sujos:
        print(r)

    print("\n=== PROCESSANDO LIMPEZA ===")
    dados_tratados = processar_dados(dados_sujos)

    print("\n=== DADOS FINALIZADOS (LIMPOS) ===")
    for r in dados_tratados:
        print(r)
        
    # Teste rápido de email inválido
    print("\n=== VALIDAÇÃO DE EMAIL ===")
    print(f"maria.souza@email é válido? {validar_email('maria.souza@email')}")