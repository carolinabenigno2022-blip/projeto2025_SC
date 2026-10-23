"""Módulo base do projeto2025_SC.

Este artefato representa um item de configuração já existente no repositório.
Durante a atividade prática ele será MODIFICADO para simular uma solicitação
de mudança feita pelo time de operações (stakeholders).

Versão inicial: 1.0
"""


def saudacao(nome: str) -> str:
    """Retorna uma saudação simples para o nome informado."""
    return f"Olá, {nome}! Bem-vindo ao projeto2025_SC."


def main() -> None:
    print(saudacao("time de desenvolvimento"))


if __name__ == "__main__":
    main()
