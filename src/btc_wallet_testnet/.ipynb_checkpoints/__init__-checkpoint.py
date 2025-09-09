"""
Arquivo __ini__.py

Pacote btc_wallet_testnet

- Função principal para geração de carteira
- Utilitários para mnemônicos

Autor: Luciano Magalhães / BH / MG / Brasil
Versão: 1.0
Data: 2025 julho
"""

from .create_wallet import (
    Carteira,
    gerar_carteira_bech32,
    gerar_mnemonico,
    main
)

__all__ = [
    "Carteira",
    "gerar_carteira_bech32",
    "gerar_mnemonico",
    "main"
]