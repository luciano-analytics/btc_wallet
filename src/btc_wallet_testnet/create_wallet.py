"""
Arquivo: create_wallet.py

- Geração de frase mnemônica BIP39
- Derivação de chave privada e endereço Bech32 (tb1...)

Autor: Luciano Magalhães / BH / MG / Brasil
Versão: 1.0
Data: 2025-08
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from bip_utils import (
    Bip39MnemonicGenerator,
    Bip39SeedGenerator,
    Bip39WordsNum,
    Bip84,
    Bip84Coins,
    Bip44Changes,
)

CAMINHO_PADRAO = "m/84'/1'/0'/0/0"

@dataclass(frozen=True)
class Carteira:
    endereco: str
    chave_privada_wif: str
    mnemônico: str
    caminho: str

def gerar_mnemonico(qtd_palavras: int = 12) -> str:
    if qtd_palavras not in (12, 24):
        raise ValueError("Número de palavras deve ser 12 ou 24.")
    enum_palavras = Bip39WordsNum.WORDS_NUM_24 if qtd_palavras == 24 else Bip39WordsNum.WORDS_NUM_12
    return Bip39MnemonicGenerator().FromWordsNumber(enum_palavras)

def gerar_carteira_bech32(
    mnemônico: Optional[str] = None,
    senha: str = "",
    caminho: str = CAMINHO_PADRAO
) -> Carteira:
    frase = mnemônico or gerar_mnemonico()
    semente = Bip39SeedGenerator(frase).Generate(senha)
    bip84 = Bip84.FromSeed(semente, Bip84Coins.BITCOIN_TESTNET)
    no = bip84.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)

    endereco = no.PublicKey().ToAddress()
    chave_privada = no.PrivateKey().ToWif()

    if not endereco.startswith("tb1"):
        raise RuntimeError("Endereço gerado não é Bech32 testnet (tb1...).")

    return Carteira(endereco=endereco, chave_privada_wif=chave_privada, mnemônico=frase, caminho=caminho)

def main() -> None:
    carteira = gerar_carteira_bech32()
    print("\n✅ Carteira gerada com sucesso:")
    print(f"- Endereço Bech32: {carteira.endereco}")
    print(f"- Chave privada WIF: {carteira.chave_privada_wif}")
    print(f"- Frase mnemônica: {carteira.mnemônico}")
    print(f"- Caminho derivado: {carteira.caminho}\n")

if __name__ == "__main__":
    principal()
