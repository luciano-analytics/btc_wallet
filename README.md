
![Banner do Projeto BTC](imgs/carteira_btc.webp)

---

# Geração de Carteira Bitcoin Bech32 (Testnet) em Python

📍 **Autor**: Luciano Magalhães  
📍 **Local**: Belo Horizonte, MG — Brasil  
📍 **Área**: Desenvolvimento de Software / Blockchain  
📍 **Versão**: 1.0  
📍 **Data**: Setembro, 2025  

---

## 📌 Descrição do Projeto

Este projeto tem como objetivo gerar carteiras Bitcoin no padrão Bech32 (BIP84) para a rede de testes (testnet), utilizando padrões reconhecidos como BIP39 para mnemônicos e BIP84 para derivação hierárquica de chaves. A estrutura é modular, clara e voltada para fins educacionais, validações técnicas e simulações seguras.

---

## 🧠 Como a carteira é construída — Etapas Técnicas

1. **Geração da mnemônica (BIP39)**  
   → Criação de uma frase de 12 ou 24 palavras com entropia criptográfica.

2. **Derivação da seed**  
   → Conversão da mnemônica em bytes para uso com algoritmos de derivação.

3. **Aplicação do caminho BIP84**  
   → Geração da chave privada e endereço Bech32 (`tb1...`) para testnet.

4. **Encapsulamento dos dados**  
   → Uso de `dataclass(frozen=True)` para garantir imutabilidade da estrutura `Carteira`.

5. **Importação modular**  
   → O pacote `btc_wallet_testnet` permite uso direto em notebooks e scripts externos.

---

## 🧪 Exemplos de Testes

- Validação do prefixo `tb1` para garantir rede de testes.
- Geração de múltiplas carteiras com diferentes mnemônicos.
- Verificação da integridade da estrutura imutável `Carteira`.

---

## 📂 Estrutura do Projeto

```text

🟦 btc_wallet/
├── 🟨 imgs/
│   └── 📄 carteira_btc.jpg
│       → Imagem ilustrativa usada no topo do README
│
├── 🟨 notebooks/
│   └── 📄 geracao_carteira_btc_testnet.ipynb
│       → Notebook principal com explicações e execução do projeto
│
├── 🟨 src/
│   └── 🟨 btc_wallet_testnet/
│       ├── 📄 __init__.py
│       └── 📄 create_wallet.py
│           → Módulo com toda a lógica de geração da carteira
│
├── 🟨 tests/
│   └── 📄 test_wallet.py
│       → Teste automatizado com pytest para validar a função gerar_carteira_bech32()
│
├── 📄 README.md
│   → Documento explicativo com descrição, etapas e testes
│
├── 📄 pyproject.toml
│   → Configuração do projeto e dependências gerenciadas via Poetry
│
├── 📄 poetry.lock
│   → Registro das versões exatas das dependências instaladas

🔎 Legenda: 
🟦 Raiz do projeto
🟨 Pasta
📄 Arquivo
→ Descrição funcional

```
---

## ⚙️ Preparando o ambiente com Poetry

Este projeto utiliza [Poetry](https://python-poetry.org/) para gerenciamento de dependências e ambiente virtual. Siga os passos abaixo para configurar corretamente:

### Acesse a pasta do projeto
cd btc_wallet


### Inicialize o projeto com Poetry (caso ainda não tenha o pyproject.toml)
poetry init --name "btc_wallet_testnet" \
            --description "Geração de carteira BTC Bech32 para testnet" \
            --author "Luciano Magalhães" \
            --python "^3.12"


### Instale as dependências principais
poetry add bip-utils ipykernel

### Ative o ambiente virtual
poetry shell

---

## 🚀 Como Executar

## 💻 Via VS Code com Poetry

### Clonar o repositório principal
git clone https://github.com/luciano-analytics/projetos.git
cd projetos/p7

### Instalar o Poetry (caso ainda não tenha)
curl -sSL https://install.python-poetry.org | python3 -

### Instalar dependências e ativar ambiente virtual
poetry install
poetry shell

### Executar o script principal
python src/btc_wallet_testnet/create_wallet.py


## 💻 📓 Via Jupyter Notebook

### Ativar o ambiente Poetry
poetry shell

### Adicionar kernel Jupyter (se necessário)
poetry add ipykernel
python -m ipykernel install --user --name btc_wallet_testnet_py --display-name "Python (btc_wallet_testnet_py)"

### Abrir o notebook
jupyter notebook notebooks/geracao_carteira_btc_testnet.ipynb

---

✅ Requisitos

- Python 3.12.3
- [Poetry](https://python-poetry.org/docs/#installation)
- [Visual Studio Code](https://code.visualstudio.com/)

  - Extensões recomendadas:
    - Jupyter
    - Python
- Jupyter Notebook (opcional, se não usar VS Code)

---

## 📜 Licença

Este projeto está licenciado sob a [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

---

⚠️ Este projeto é destinado a fins educacionais e de validação técnica. Não deve ser utilizado em ambientes de produção ou com fundos reais.
