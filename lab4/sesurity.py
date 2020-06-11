import os
import hashlib
import pyAesCrypt  # type: ignore
import random


def pass_hash(password: str, acc_name: str) -> bytes:
    salt = list(acc_name)
    salt.reverse()
    salt_1 = ''.join(salt)
    need_hash = str(password) + str(salt_1)
    need_hash_1 = need_hash.encode('utf-8')  ## type: ignore
    xesh = hashlib.sha256(need_hash_1)  ## type: ignore
    xesh = xesh.hexdigest()  # type: ignore
    return xesh  # type: ignore


def create_hash_file(password: str, acc_name: str, way: str) -> str:
    xesh = pass_hash(password, acc_name)
    with open(way, 'w') as system:
        system.write(xesh)  # type: ignore
    return way


def master_key(password: str) -> str:
    m_key = list(password)
    size_m_key = len(m_key)
    if size_m_key % 2 == 0:
        pass
    elif size_m_key % 2 == 1:
        size_m_key -= 1
    for j in range(int(size_m_key / 2)):
        for i in range(j, size_m_key - j, 2):
            m_key[i], m_key[i + 1] = m_key[i + 1], m_key[i]
    m_key_1 = ''.join(m_key)

    return m_key_1


def genkey() -> str:
    string_chars = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ls = list(string_chars)
    random.shuffle(ls)
    password = ''.join([random.choice(ls) for i in range(15)])
    return password


def create_genkey_enfile(key: str, m_key: str, way: str) -> str:
    with open(way, 'w') as key_en:
        key_en.write(key)
    enkey_file = encrypt(way, m_key)
    return key


def create_genkey_defile(way: str, m_key: str) -> str:
    dekey_file = decrypt(way, m_key)
    with open(dekey_file, 'r') as key_de:
        key = key_de.read()
    os.remove(dekey_file)
    return key


def encrypt(way: str, key: str) -> str:
    byffsize = 512 * 1024
    encrypt_file_way = way + '.aes'
    pyAesCrypt.encryptFile(way, encrypt_file_way, key, byffsize)
    os.remove(way)
    return encrypt_file_way


def decrypt(way: str, key: str) -> str:
    byffsize = 512 * 1024
    decrypt_file = way.rstrip('.aes')
    pyAesCrypt.decryptFile(way, decrypt_file, key, byffsize)
    return decrypt_file


def check_pass(way: str, acc_name: str, password: str) -> bool:
    with open(way, 'r')as system:
        old_xesh = system.read()
    os.remove(way)
    new_xesh_1 = pass_hash(password, acc_name)
    if new_xesh_1 == old_xesh:  # type: ignore
        return True
    else:

        return False


if __name__ == '__main__':
    print('Это модуль')
