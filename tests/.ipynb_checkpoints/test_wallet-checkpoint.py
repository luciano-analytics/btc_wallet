"""
Arquivo test_wallet.py

Este módulo contém testes automatizados para validar a função `gerar_carteira`,
responsável por criar uma carteira Bitcoin Bech32 para a testnet (BIP84).

Os testes garantem que os dados retornados estejam no formato correto e que
os componentes essenciais da carteira sejam gerados conforme esperado.

Autor: Luciano Magalhães / BH / MG / Brasil
Versão: 1.0
Data: 2025-08
"""

import sys
import os

# Adiciona o diretório 'src' ao caminho de importação
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from btc_wallet_testnet.create_wallet import gerar_carteira_bech32

def test_gerar_carteira():
    """
    Testa se a função retorna um dicionário do tipo Carteira com endereço Bech32 válido.
    """
    carteira = gerar_carteira_bech32()
    assert hasattr(carteira, "endereco")
    assert isinstance(carteira.endereco, str)
    assert carteira.endereco.startswith("tb1")  # Prefixo Bech32 para testnet

def test_chave_privada_e_mnemonico():
    """
    Valida se a chave privada WIF e o mnemônico estão presentes e seguem o formato esperado.
    """
    carteira = gerar_carteira_bech32()

    # Chave privada WIF
    chave_privada = carteira.chave_privada_wif
    assert chave_privada is not None
    assert isinstance(chave_privada, str)
    assert len(chave_privada) >= 51  # WIF geralmente tem entre 51 e 52 caracteres

    # Frase mnemônica
    mnemônico = str(carteira.mnemônico)  # Converte para string
    assert mnemônico is not None
    assert isinstance(mnemônico, str)
    assert len(mnemônico.split()) in (12, 24)  # BIP39 padrão

def test_caminho_bip84():
    """
    Verifica se o caminho de derivação segue o padrão BIP84 para testnet.
    """
    carteira = gerar_carteira_bech32()
    caminho = carteira.caminho
    assert caminho is not None
    assert isinstance(caminho, str)
    assert caminho.startswith("m/84'/1'/0'/0/")
