![Banner do Projeto BTC](imgs/carteira_btc.webp)

---

# Projeto completo: Geração de Carteira + Simulação de Transação Bitcoin (Testnet)

📍 **Autor:** Luciano Magalhães  
📍 **Local:** Belo Horizonte, MG — Brasil  
📍 **Área:** Desenvolvimento de Software / Blockchain  
📍 **Versão:** 1.2  
📍 **Data:** Setembro, 2025  

---

## 🧩 Visão geral

Este repositório **reúne dois módulos** complementares que cobrem o ciclo completo de uso de Bitcoin em ambiente de testes (testnet):

1) Geração de Carteira Bitcoin Bech32 (Testnet)  

2) Simulação de Transação Bitcoin na Testnet

A Parte 1 cria uma carteira Bech32 no padrão BIP84 para testnet. A Parte 2 utiliza essa carteira para enviar satoshis na testnet, validando e monitorando a transação.

---

## 🧠 Parte 1 — Geração de carteira Bitcoin Bech32 (Testnet)

### 📌 Descrição

Geração de carteiras Bitcoin no padrão Bech32 (BIP84) para a rede de testes (testnet), utilizando BIP39 para mnemônicos e BIP84 para derivação hierárquica de chaves. Estrutura modular, clara e orientada a fins educacionais e validações técnicas.

---

### 4. 📦 Funcionalidades

- Geração de frase mnemônica (BIP39)
- Derivação da seed e da chave privada (BIP32)
- Criação de endereço Bech32 (BIP84) para testnet (`tb1...`)
- Exportação da chave privada no formato WIF
- Encapsulamento em `dataclass(frozen=True)` para imutabilidade

---

### 5. 📘 Execução

#### 💻 Via VS Code com Poetry

#### Clonar o repositório

#### 1) Clonar o repositório
```bash
git clone https://github.com/luciano-analytics/btc_wallet.git

# Instalar Poetry (se necessário)
curl -sSL https://install.python-poetry.org | python3 -

# Instalar dependências e ativar o ambiente
poetry install
poetry shell

# Executar o script principal de geração
python src/btc_wallet_testnet/create_wallet.py

````
### 💻📓 Via Jupyter Notebook
```bach
# Ativar o ambiente
poetry shell

# (Se necessário) adicionar kernel
poetry add ipykernel
python -m ipykernel install --user --name btc_wallet_testnet_py --display-name "Python (btc_wallet_testnet_py)"

# Abrir o notebook
jupyter notebook notebooks/geracao_carteira_btc_testnet.ipynb
```

### 6. 📌 Observações técnicas

- O endereço gerado segue o padrão Bech32 da testnet (tb1...).
- A chave privada é exportada em formato WIF, compatível com carteiras e bibliotecas comuns.
- O módulo expõe a função gerar_carteira_bech32() para uso em notebooks e scripts.

### 7. 🔐 Considerações sobre segurança

As credenciais geradas neste projeto — como a chave privada e a frase mnemônica — são utilizadas exclusivamente em ambiente de testes (testnet) e não possuem valor real. Ainda assim, recomenda-se que essas informações não sejam reutilizadas em ambientes de produção, nem compartilhadas fora do contexto técnico deste projeto, evitando confusões ou uso indevido em aplicações reais.

### 8. 🔁 Integração com a simulação de transação

A carteira gerada aqui (chave privada WIF, chave pública e endereço Bech32) pode ser usada diretamente para realizar transações reais na testnet.

- Consulta de saldo e UTXOs
- Criação, assinatura e transmissão da transação
- Validação do TXID e monitoramento da confirmação em exploradores públicos

Pasta e arquivo: **notebooks/simular_transacao_testnet.ipynb** 

Levantamento de Requisitos e planejamento do projeto de Simulação: **docs/requisitos_simulacao.md**

## 🔄 Parte 2 — Simulação de transação Bitcoin na testnet

### 📌 Descrição

Envio de satoshis entre endereços gerados na testnet, utilizando a carteira criada na Parte 1.

O fluxo contempla:

* verificação de saldo, 
* definição de parâmetros (destinatário, valor, taxa), 
* criação + assinatura, 
* transmissão, 
* obtenção do TXID 
* monitoramento com redundância de exploradores.


## 1. 📦 Funcionalidades

- Verificação de saldo e listagem de UTXOs via APIs públicas

- Definição de parâmetros da transação (endereço, valor, taxa) com cálculo do máximo enviável

- Criação e assinatura digital da transação

- Transmissão e retorno do TXID

- Registro histórico em JSON

- Monitoramento da confirmação (mempool.space e Blockstream)

## 2. 📘 Execução

**Pré-requisito:** carteira gerada na Parte 1

**Arquivo principal da simulação:** notebooks/simular_transacao_testnet.ipynb

### Passos no notebook:

 1) Verificação/obtenção de saldo (faucet + API)

 2) Definição dos parâmetros (destino, valor, taxa)
 3) Criação, assinatura e transmissão da transação
 4) Validação do TXID e monitoramento da confirmação

## 3. 📌 Observações técnicas

- Endereços válidos na testnet devem começar com tb1 (Bech32).

- A taxa (sat/kB) é utilizada para estimar o custo total com base no tamanho (vbytes).

- O fluxo trata cenários com e sem troco, evitando valores abaixo do limite de poeira (dust).

## 4. 📁 Banco de dados e persistência

- Banco SQLite da biblioteca **bitcoinlib**:

   data/bitcoinlib_testnet.db

- Histórico de transações (JSON):
   
   data/historico_transacoes_testnet.json


## 5. 🔐 Avisos de segurança

- Use este módulo exclusivamente na rede de testes (testnet).

- Nunca use dados reais de carteiras (chave privada ou frase mnemônica) neste ambiente.
- Proteja informações sensíveis e evite compartilhá-las publicamente.
- Verifique se os endereços começam com tb1 (Bech32 testnet).

## 6. 📥 Importação da carteira no Electrum

1) Inicie o Electrum com --testnet

2) Crie nova carteira > “Importar chave ou endereço Bitcoin”
3) Cole a chave privada (WIF) gerada na Parte 1
4) Confirme e aguarde a sincronização
📚 Documentação complementar
Planejamento e requisitos da simulação: docs/requisitos_simulacao.md


## 7. ✅ Requisitos projeto Simulacao

- Python 3.12.3

- Poetry

- VS Code (extensões: Python, Jupyter)

- Jupyter Notebook (opcional)


## 8. 📜 Licença
Este projeto está licenciado sob a Apache License 2.0.

## ⚠️ Projeto destinado a fins educacionais e validação técnica. Não utilize em produção ou com fundos reais.