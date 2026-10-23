# projeto2025_SC

Repositório de artefatos do projeto **projeto2025_SC**, criado para a atividade prática
**U4_A1 – Gerenciamento de Configuração** (Unidade U4 – Projeto de Software Avançado).

## Objetivo

Demonstrar o uso de uma ferramenta de gerenciamento de configuração (**Git + GitHub**) para
controlar os artefatos gerados no desenvolvimento de software, permitindo que todos os
membros do time compartilhem um repositório remoto único com a versão mais atual de cada
artefato.

## Estrutura do projeto

```
projeto2025_SC/
├── README.md                        # Visão geral do projeto
├── .gitignore                       # Arquivos ignorados pelo controle de versão
├── docs/
│   └── aula_pratica_u4_a1.md        # Relatório da prática e questão reflexiva
└── src/
    ├── novo.py                      # Artefato existente (modificado na prática)
    └── nova_funcionalidade.py       # Artefato novo (criado na prática)
```

## Artefatos

| Artefato | Descrição |
| --- | --- |
| `src/novo.py` | Módulo base do projeto. Foi **modificado** durante a prática para simular uma solicitação de mudança. |
| `src/nova_funcionalidade.py` | Novo módulo **criado** durante a prática. |

## Como obter os artefatos (clone)

```bash
git clone https://github.com/carolinabenigno2022-blip/projeto2025_SC.git
```

## Ciclo de atualização (commit e push)

```bash
git status
git add .
git commit -m "mensagem de documentação da mudança"
git push
```

## Autoria

- Luiz Antônio da Silva Júnior
