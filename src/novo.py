"""Módulo base do projeto2025_SC.

Este artefato representa um item de configuração já existente no repositório.
Durante a atividade prática ele foi MODIFICADO para simular uma solicitação
de mudança feita pelo time de operações (stakeholders).

Histórico de versões:
- v1.0: versão inicial (commit inicial).
- v1.1: modificado na atividade prática U4_A1.
        Alterações: inclusão da função `despedida` e do registro da mudança
        solicitada pelo time de operações.
"""

# mudanças realizadas 03:09
# Solicitação do time de operações: incluir saudação de despedida no módulo.


def saudacao(nome: str) -> str:
    """Retorna uma saudação simples para o nome informado."""
    return f"Olá, {nome}! Bem-vindo ao projeto2025_SC."


def despedida(nome: str) -> str:
    """Nova função incluída na versão 1.1 (mudança solicitada).

    Retorna uma mensagem de despedida para o nome informado.
    """
    return f"Até logo, {nome}! Obrigado por contribuir com o projeto2025_SC."


def main() -> None:
    print(saudacao("time de desenvolvimento"))
    print(despedida("time de operações"))


if __name__ == "__main__":
    main()
