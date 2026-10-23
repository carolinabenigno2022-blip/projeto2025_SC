"""Nova funcionalidade criada durante a atividade prática U4_A1.

Este artefato NÃO existia no repositório remoto. Ele foi criado no computador
local e enviado (commit + push) para o repositório compartilhado, ficando
disponível para todo o time de desenvolvimento.

Controle de versão:
- v1.0: criado na atividade prática U4_A1 – Gerenciamento de Configuração.
"""

from typing import Iterable


def media(valores: Iterable[float]) -> float:
    """Calcula a média aritmética de uma sequência de valores.

    Levanta ValueError caso a sequência esteja vazia.
    """
    dados = list(valores)
    if not dados:
        raise ValueError("A sequência informada está vazia.")
    return sum(dados) / len(dados)


def resumo(valores: Iterable[float]) -> str:
    """Retorna um resumo textual simples dos indicadores do time de operações."""
    dados = list(valores)
    return (
        f"registros={len(dados)} | "
        f"soma={sum(dados):.2f} | "
        f"media={media(dados):.2f} | "
        f"minimo={min(dados):.2f} | "
        f"maximo={max(dados):.2f}"
    )


def main() -> None:
    amostra = [12.5, 8.0, 15.75, 10.25]
    print("Nova funcionalidade - resumo dos indicadores:")
    print(resumo(amostra))


if __name__ == "__main__":
    main()
