# 📄 Levantamento de Requisitos e Planejamento  
**Projeto:** Geração de Carteira Bitcoin Bech32 (Testnet) em Python

---

## 🎯 Visão Geral
- **Objetivo:** Criar, de forma reprodutível e segura, carteiras Bitcoin compatíveis com a rede de testes (testnet), utilizando padrões BIP39 e BIP84, com endereços Bech32.
- **Resultado Esperado:** Função pública para geração de carteira e estrutura imutável contendo endereço, WIF, mnemônico e caminho de derivação.

---

## 📌 Escopo

**Inclui:**
- Geração de mnemônico (BIP39)
- Derivação de seed
- Derivação de chaves e endereço (BIP84 testnet)
- Encapsulamento imutável da carteira
- Função pública de geração
- Exemplo de uso em notebook

**Não Inclui:**
- Envio de transações
- Monitoramento de TXID
- Integração com mainnet
- Persistência em banco de dados
- Interface gráfica

---

## ✅ Requisitos Funcionais

| Código | Descrição |
|--------|-----------|
| RF01 | Gerar mnemônico BIP39 com 12 palavras |
| RF02 | Derivar seed a partir do mnemônico |
| RF03 | Derivar chave privada e endereço público no caminho BIP84 testnet, gerando endereço Bech32 (tb1...) |
| RF04 | Expor função pública `gerar_carteira_bech32()` |
| RF05 | Retornar estrutura imutável com address, wif, mnemonic e path |
| RF06 | Permitir uso direto em Jupyter/VS Code via import do pacote |

---

## ⚙️ Requisitos Não Funcionais

| Código | Descrição |
|--------|-----------|
| RNF01 | Operar exclusivamente em testnet |
| RNF02 | Código modular e reutilizável (pacote `src/btc_wallet_testnet`) |
| RNF03 | Imutabilidade dos dados da carteira (dataclass frozen) |
| RNF04 | Compatível com Python 3.11+, Jupyter e VS Code |
| RNF05 | Documentação mínima e exemplo de uso em notebook |
| RNF06 | Sem telemetria ou dependências desnecessárias |

---

## 📜 Regras de Negócio
- Endereços devem começar com `tb1` (Bech32 testnet)
- Mnemônico com 12 palavras (BIP39)
- Caminho de derivação padrão BIP84 testnet: `m/84'/1'/0'/0/0`
- Objeto carteira imutável após criação
- Uso exclusivo para testes

---

## 🏗 Arquitetura e Componentes
- **Notebook principal:** `notebooks/geracao_carteira_btc_testnet.ipynb`
- **Pacote:** `src/btc_wallet_testnet/`
  - `__init__.py` → expõe `gerar_carteira_bech32` e a dataclass `Carteira`
  - `create_wallet.py` → implementação da geração (BIP39, derivação, BIP84)
- **Estrutura de dados:** `dataclass` imutável `Carteira` (address, wif, mnemonic, path)
- **Integração:** Import direto no notebook
- **Saída:** Impressão controlada de dados para validação

---

## 🔄 Fluxo de Alto Nível
1. Gerar mnemônico (BIP39)
2. Derivar seed
3. Derivar chave privada e endereço (BIP84 testnet)
4. Montar dataclass `Carteira` (frozen)
5. Expor via `gerar_carteira_bech32()`
6. Consumir no notebook e exibir resultados

---

## 🧪 Plano de Testes

| Teste | Objetivo | Procedimento | Critério de Aceitação |
|-------|----------|--------------|-----------------------|
| T01 | Validar geração do mnemônico | Chamar `gerar_carteira_bech32()` | Mnemônico com 12 palavras válidas |
| T02 | Validar endereço Bech32 testnet | Inspecionar `carteira.address` | Inicia com `tb1` e é válido |
| T03 | Validar WIF | Inspecionar `carteira.wif` | WIF válido para testnet |
| T04 | Validar caminho de derivação | Inspecionar `carteira.path` | Igual a `m/84'/1'/0'/0/0` |
| T05 | Imutabilidade | Tentar alterar atributo | Lança exceção |
| T06 | Import do pacote | `from btc_wallet_testnet import gerar_carteira_bech32` | Import sem erro |

---

## 📏 Critérios de Aceitação
- Execução de `gerar_carteira_bech32()` retorna objeto imutável com address, wif, mnemonic e path
- Endereço conforme Bech32 testnet e caminho conforme BIP84
- Notebook executa sem erros
- Código organizado em pacote e importável

---

## ⚠️ Riscos e Mitigação
- **Exposição indevida de credenciais:** Limitar escopo à testnet e reforçar avisos
- **Quebra de compatibilidade:** Fixar versões mínimas de dependências
- **Uso incorreto do caminho de derivação:** Testes automatizados validam path

---

## 🔐 Avisos de Segurança
- Somente testnet
- Tratar chaves e mnemônicos com cuidado
- Sem persistência automática

---
