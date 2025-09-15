# 📋 Levantamento de Requisitos e Planejamento — Simulação de Transação Bitcoin (Testnet)

## 🧭 Visão Geral do Projeto

**Título:** Simulação de Transação Bitcoin na Rede de Testes (Testnet)  

**Objetivo:** Demonstrar, de forma prática e segura, como realizar uma transação Bitcoin utilizando uma carteira Bech32 gerada previamente, operando exclusivamente na testnet.

---

## 🔹 Requisitos Funcionais (RF)

| Código | Descrição |
|--------|-----------|
| RF01 | Gerar ou importar uma carteira Bitcoin Bech32 (testnet) |
| RF02 | Consultar saldo disponível via explorador público |
| RF03 | Definir parâmetros da transação (destinatário, valor, taxa) |
| RF04 | Criar e assinar digitalmente a transação |
| RF05 | Transmitir a transação para a rede testnet |
| RF06 | Retornar e exibir o TXID da transação |
| RF07 | Monitorar a confirmação da transação via explorador |

---

## 🔸 Requisitos Não Funcionais (RNF)

| Código | Descrição |
|--------|-----------|
| RNF01 | O projeto deve operar exclusivamente na rede de testes (testnet) |
| RNF02 | Nenhuma chave privada ou mnemônico real deve ser utilizado |
| RNF03 | O código deve ser modular e reutilizável |
| RNF04 | O projeto deve registrar logs ou histórico da transação |
| RNF05 | O ambiente deve ser compatível com Jupyter Notebook, VS Code e Python 3.11+

---

## 🧱 Arquitetura e Componentes

O projeto foi desenvolvido para rodar em ambientes Jupyter Notebook e VS Code, com estrutura modular e persistência local. A arquitetura inclui:

- **Notebook principal:** `simular_transacao_testnet.ipynb`
- **Editor alternativo:** VS Code (com suporte a Jupyter e Python 3.11+)
- **Módulo externo:** `gerar_carteira_bech32` importado de `src/`
- **Banco de dados:** `bitcoinlib_testnet.db` (SQLite), armazenado em `data/`
- **Biblioteca principal:** `bitcoinlib`
- **Persistência de histórico:** JSON opcional (`historico_transacao_testnet.json`)
- **Gerenciador de dependências:** `Poetry`
- **Ambiente:** Compatível com JupyterLab, VS Code e execução local via terminal

---

## 🔐 Regras de Negócio

- A transação só será criada se houver saldo suficiente
- O endereço de destino deve ser válido e começar com `tb1`
- A taxa mínima deve respeitar o limite da rede testnet
- O projeto não realiza transações reais (mainnet)

---

## 🧪 Plano de Testes

| Teste | Objetivo | Resultado Esperado |
|-------|----------|---------------------|
| T01 | Gerar carteira Bech32 | Endereço `tb1...` válido |
| T02 | Consultar saldo | Retorno positivo via API |
| T03 | Criar transação | TXID gerado com sucesso |
| T04 | Transmitir transação | Confirmação via explorador |
| T05 | Reutilizar carteira | Persistência via SQLite |


