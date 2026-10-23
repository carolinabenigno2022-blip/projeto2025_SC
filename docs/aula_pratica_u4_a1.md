# Aula Prática – U4_A1 – Gerenciamento de Configuração

**Curso:** Projeto de Software
**Unidade:** U4 – Projeto de Software Avançado
**Aula:** A1 – Gerenciamento de Configuração
**Solução digital:** GitHub e Git
**Repositório:** https://github.com/carolinabenigno2022-blip/projeto2025_SC
**Conta GitHub:** carolinabenigno2022-blip

---

## 1. Objetivo

Demonstrar a gestão dos artefatos gerados no desenvolvimento de software por meio de uma
ferramenta de gerenciamento de configuração (Git + GitHub), compreendendo o funcionamento de um
repositório de artefatos compartilhado pelo time, obtendo os artefatos no computador local a partir
do repositório remoto, modificando/criando artefatos e publicando as alterações de volta no
repositório remoto.

## 2. Ambiente utilizado

| Item | Valor |
| --- | --- |
| Conta GitHub | carolinabenigno2022-blip |
| Repositório remoto | `projeto2025_SC` (público) |
| Sistema operacional | Windows |
| Ferramentas | Git 2.55 e Git Credential Manager |
| Autenticação | Git Credential Manager (HTTPS) |

## 3. Procedimento executado

### 3.1 Criação/configuração do repositório remoto (GitHub)
- Criada a conta GitHub `carolinabenigno2022-blip`.
- Criado o repositório **`projeto2025_SC`** (público, branch padrão `main`).

### 3.2 Configuração do Git (computador local)
```bash
git config user.name  "carolinabenigno2022-blip"
git config user.email "carolinabenigno2022-blip@users.noreply.github.com"
```

### 3.3 Obtenção dos artefatos do repositório remoto (clone)
A URL HTTPS do projeto foi copiada no botão **Code** do GitHub e usada no clone:
```bash
git clone https://github.com/carolinabenigno2022-blip/projeto2025_SC.git
```
Assim os artefatos foram baixados do repositório remoto (GitHub) para uma pasta no computador local.

### 3.4 Criação da estrutura inicial do projeto
Artefatos criados no computador local e enviados no **commit inicial**:

```
projeto2025_SC/
├── README.md
├── .gitignore
└── src/
    └── novo.py            # artefato base
```

```bash
git add .
git commit -m "Commit inicial: estrutura do projeto e artefato base novo.py"
git push -u origin main
```

### 3.5 Modificação e criação de artefatos (solicitações dos clientes)
- **Modificado** o artefato `src/novo.py` (v1.0 → v1.1): inclusão da função `despedida`
  e registro da mudança `# mudanças realizadas 03:09`, atendendo à solicitação do time de operações.
- **Criado** o artefato `src/nova_funcionalidade.py`: novo módulo com as funções `media()` e
  `resumo()`, que não existia no repositório remoto.

### 3.6 Atualização do repositório remoto (status → add → commit → push)
```bash
git status
git add .
git commit -m "U4_A1: modifica novo.py (v1.1) e cria nova_funcionalidade.py"
git push
```

## 4. Evidências / Rastreabilidade

| Commit | Descrição |
| --- | --- |
| `7dca420` | Commit inicial: estrutura do projeto e artefato base `novo.py` |
| `f8437b4` | Modificação de `novo.py` (v1.1) e criação de `nova_funcionalidade.py` |

Consulta do histórico:
```bash
git log --oneline
```

## 5. Questão Reflexiva

**Descreva o resultado obtido com a prática e um resumo das habilidades desenvolvidas.**

A prática permitiu vivenciar o ciclo completo de gerenciamento de configuração de software (SCM)
usando Git e GitHub. Inicialmente, compreendi a diferença entre o **repositório remoto** (GitHub),
que é a fonte única e compartilhada dos artefatos, e o **repositório local** (clone no computador),
onde o trabalho efetivamente acontece. Ao executar o `git clone`, obtive todos os artefatos na
versão mais atual do projeto.

Em seguida, ao **modificar** o artefato `novo.py` e **criar** o artefato `nova_funcionalidade.py`,
percebi como o Git rastreia cada alteração: o comando `git status` mostrou claramente quais itens
eram novos/itens de configuração alterados; o `git add .` preparou essas mudanças na *staging area*;
o `git commit` registrou cada conjunto de alterações com uma mensagem de documentação, criando um
ponto de rastreabilidade; e o `git push` publicou tudo no repositório remoto, deixando a versão mais
atual disponível para todo o time.

Habilidades desenvolvidas e/ou aperfeiçoadas:
- Criar e configurar um repositório remoto no GitHub e um repositório local com o Git.
- Obter artefatos de um repositório remoto (clone) e publicar alterações (push).
- Entender o fluxo de trabalho com versionamento: `status → add → commit → push`.
- Compreender o conceito de *item de configuração*, de controle de versão e de rastreabilidade
  das mudanças (histórico de commits).
- Reconhecer a importância de um repositório único e remoto para trabalho colaborativo, permitindo
  que vários membros do time compartilhem a mesma versão dos artefatos e integrem suas mudanças.

Como melhoria/aprendizado adicional, observei que o uso de uma mensagem de commit clara é
fundamental para a documentação e para a rastreabilidade, e que práticas colaborativas mais
avançadas (como *branches* e *Pull Requests*) permitem isolar o desenvolvimento e revisar o código
antes da integração final. O resultado obtido foi um repositório remoto contendo a versão mais
atualizada dos artefatos, demonstrando que é possível controlar tanto a obtenção dos artefatos
quanto o envio das modificações/criações para o repositório compartilhado.

## 6. Checklist de Verificação (entrega)

- [x] **Projeto criado no ambiente remoto com sucesso**
  - Repositório público `carolinabenigno2022-blip/projeto2025_SC` (HTTP 200), branch `main`.
- [x] **Artefatos do repositório remoto obtidos/atualizados no computador local**
  - `git clone` + `git pull --ff-only` (fast-forward até `4684bd9`); `git status` sem diferenças.
- [x] **Artefatos modificados/criados inseridos/atualizados no repositório remoto**
  - `src/novo.py` modificado (v1.1) e `src/nova_funcionalidade.py` criado; `git push` concluído.
- [x] **Solicitações do Roteiro revisadas** (ver detalhamento abaixo).
- [x] **Resultado submetido** (repositório remoto atualizado + este relatório).

### 6.1 Revisão das solicitações do Roteiro de Aula Prática

| # | Solicitação do roteiro | Situação | Evidência |
| --- | --- | --- | --- |
| 1 | Criar conta GitHub e instalar o Git | OK | Conta `carolinabenigno2022-blip` / Git 2.55 |
| 2 | Configurar nome de usuário no Git | OK | `git config user.name` = `carolinabenigno2022-blip` |
| 3 | Criar o projeto (repositório) no GitHub | OK | `projeto2025_SC` (público, `main`) |
| 4 | Copiar a URL HTTPS (botão *Code*) | OK | `https://github.com/carolinabenigno2022-blip/projeto2025_SC.git` |
| 5 | Obter os artefatos no local (clone) | OK | `git clone` realizado |
| 6 | Modificar/criar artefatos no computador local | OK | `novo.py` (v1.1) + `nova_funcionalidade.py` |
| 7a | `git status` | OK | itens alterados/novos identificados |
| 7b | `git add .` | OK | mudanças na *staging area* |
| 7c | `git commit -m "..."` | OK | commits `7dca420`, `f8437b4`, `c0a1fa0` |
| 7d | `git push` | OK | `main` publicada no GitHub |
| 8 | Verificar no repositório remoto | OK | `novo.py` com `# mudanças realizadas 03:09` e `nova_funcionalidade.py` presentes |
| 9 | Questão reflexiva | OK | Seção 5 deste relatório |

Consulta do estado:
```bash
git status -sb          # ## main...origin/main  (sincronizado)
git log --oneline       # histórico de commits
```
