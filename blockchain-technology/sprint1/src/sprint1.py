import os
from ecdsa import SigningKey, SECP256k1
import hashlib
from web3 import Web3

web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-infura-project-id'))

def generar_clave_privada():
    clave_privada_bytes = os.urandom(32)
    clave_privada = int.from_bytes(clave_privada_bytes, byteorder='big')
    clave_privada_hex = clave_privada.to_bytes(32, byteorder='big').hex()
    return clave_privada_hex

def generar_clave_publica(clave_privada):
    clave_privada_int = int(clave_privada, 16)
    clave_privada_bytes = clave_privada_int.to_bytes(32, byteorder='big')
    clave_publica = SigningKey.from_string(clave_privada_bytes, curve=SECP256k1).verifying_key.to_string('compressed').hex()
    return clave_publica

def calcular_direccion_ethereum(clave_publica):
    clave_publica_bytes = bytes.fromhex(clave_publica)
    hash_resultado = hashlib.sha3_256(clave_publica_bytes).digest()
    direccion_ethereum = hash_resultado[-20:].hex()
    return direccion_ethereum

def validar_direccion_ethereum(direccion_ethereum):
    is_valid = web3.is_address(direccion_ethereum)
    return is_valid

# Generar clave privada
clave_privada = generar_clave_privada()
print("Clave privada generada:", clave_privada)

# Generar clave pública
clave_publica = generar_clave_publica(clave_privada)
print("Clave pública generada:", clave_publica)

# Calcular direccion Ethereum
direccion_ethereum = calcular_direccion_ethereum(clave_publica)
print("Dirección Ethereum generada:", direccion_ethereum)

# Validar dirección Ethereum
es_valida = validar_direccion_ethereum(direccion_ethereum)
print("¿Es una dirección Ethereum válida?", es_valida)