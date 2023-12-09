#!/usr/bin/env python3

import base64
from encodings import utf_8
import json
import gmpy2
from random import randint


# conversie string in numar
def str_to_number(text):
    return int.from_bytes(text.encode("latin1"), 'big')

# conversie numar in string
def number_to_str(num):
    num = int(num)
    return num.to_bytes((num.bit_length() + 7) // 8, byteorder='big').decode('latin1')

# criptare mesaj cu cheie publica e si n 
def encrypt(pub_k, msg_num):
    cipher_num = gmpy2.powmod(msg_num, pub_k["e"], pub_k["n"])
    cipher_b64 = base64.b64encode(gmpy2.to_binary(cipher_num))
    return cipher_b64

def decrypt(priv_k, cipher):
    pass

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

if __name__ == "__main__":
    # mesajul meu 
    m = "eyJuIjogMTA5MzU4Njk3NzM2MjMzNjU0ODQzNzM0MzgxNzQ0NTE0ODUxNjE3MjUzMDI4ODI3MTM1NzY2MjM0MjExNDIyNjY0OTI5ODY5MDYzNTc0MDk3OTE5NDQ2MzE4NTM4OTQyNDE5ODc3NDUwMzI3OTI1NTg4MzU2NTEwODc5MDUyOTI5NDI1NTg1NDM1NDM1MDA3MTUzOTMwOTEzMDYxMjY3ODA1MzQ3MzQ4MDYwMDQ0NjIzNDQxNzA0MTMyMjU1NTkxMDA4MTI2MjQ2ODIwMDgwNzQ5NTIxNDcwODA4NDA4NTcxNTEwNjMxMTY4ODQwMjk3MTExNjcxMjM1MDg4NTEwNDQ5ODU3NjQ1MDg2NDk5MjkzOTU0NjY5NjM5NjI3NDY3ODkxOTA3Mjk4OTY0MTMxMjgxNjU0MjIzODkxMjM3NDU3MDQ5MzQ5OTQzMzc2ODUyMzgzMDQ1MTQyNjk0OTE5NDUxNTc3Njg5Nzk5MDk4NTM4NzA5MTE2NzM2MjQwNTgyMTAzNjA5MzQxMDI4MDg3NTY4NjQ3MTYxNzYwODgzMTc1NTg2ODQ0OTAzMDY4NjU5ODE4MDIxNTgxOTkyMzI4MDc1NTY2NTgwMTgyMjk5MTMyNTUzNzgyNDY4OTYzMzA1MTI1MzI1MDA1OTk5OTA1NjgyNDYyNzUyMzQ0MDc4MjMxNTUxODAzNzU3MTgwNTY5MDI5ODExODE3MzkwOTI4MTA3MjY0MDgyOTM4NTQyMDMwMTc2MjYzMjY5NTE4MDM2MDYyMzY2ODQ1Mzc1NDQ1MjkwNTIyOTE2NDQ4NzQ3Njc4NjIwMTQyMzMsICJlIjogNDMzNzE5LCAiZmxhZyI6ICJBUUVGK20rZXU5R29CU0NRczlleXN1aDJwYkN5a2lGSXZmVEt2MVpNT0s5V0F2Ykg0RWNRdzFSZFp1dGErNGVSNHJ1eURyb0pLZEtmdlNrbXhsZExDaDJuMndjQnk5aE1vSVZZbnNZS2p6V0xYeUgybDhqejJzVzRFbGpycG4zM1d2UzlZS1R6TTQ4WWRvTmZ5UE95dTlMQ2ZuQU5uNXBMNUJqbHgvZTJBamRZN1p3RlUxNzVwdHUwV0g1UVEzdlY1c1M5V3ZOWDFRbXVKbVNPck9BWkgrUWpOSDUrak56Y1dPaWdwRGl1eVBvNjB1M0xTZzZRUHRrR0hyTUJVME5zSm92VUExZVk0S3gxQ3Z6NlljWWJ4Mmo2K2lmNVcza0xaUURpT1RVSVZiV1l5d3djclI5enF1NnEzb2ZiNVFkZGkrdkJTdWRaTWhYSDJ5QWFSWjk1SXJBTyJ9"
    # nr random folosit pentru impartire
    r = 3
    # d stocheaza mesajul decodat din base64
    d = json.loads(base64.b64decode(m))
    # se creeaza cypher_dash ul utilizand formula specifica algoritmului
    cypher_dash = (gmpy2.from_binary(base64.b64decode(d['flag'])) * (gmpy2.powmod(r ,d['e'], d['n']))) % d['n']
    
    # completez cu valorile decodate din base64
    msg = {
        "n": 10935869773623365484373438174451485161725302882713576623421142266492986906357409791944631853894241987745032792558835651087905292942558543543500715393091306126780534734806004462344170413225559100812624682008074952147080840857151063116884029711167123508851044985764508649929395466963962746789190729896413128165422389123745704934994337685238304514269491945157768979909853870911673624058210360934102808756864716176088317558684490306865981802158199232807556658018229913255378246896330512532500599990568246275234407823155180375718056902981181739092810726408293854203017626326951803606236684537544529052291644874767862014233,
        "e": 433719,
        "flag": base64.b64encode(gmpy2.to_binary(cypher_dash)).decode('utf-8')}

    # se trimite la server mesajul 
    send_this = base64.b64encode(json.dumps(msg).encode())
    # acesta este rezultatul serverului la mesajul meu trimis
    d_unicode = b'\xfaQ0<Z8\xd3E$6q\xf7*\x0b\xe7\xa0\x00\x02\xa8\xdc\x0b\xde\xdch\x94<<Q-\x05\xc9\xdcA\xe1\xc3\xc4k\xfaZG\xee6\x06w'
    # se foloseste decode unicode 
    d_decode = d_unicode.decode("unicode_escape")
    # mesajul se converteste la numar
    d = str_to_number(d_decode)
    # se imparte la r conform formulei algoritmului
    res = d // r
    # se printeaza flagul obtinut convertit din nou la string
    print(number_to_str(res))
    