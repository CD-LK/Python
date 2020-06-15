import os
import hashlib
import pyAesCrypt  # type: ignore


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
    xesh_1 = str(xesh)
    with open(way, 'w') as system:
        system.write(xesh_1)  ## type: ignore
    return way


def master_key(password: str) -> str:
    salt = 'this is salt'
    m_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000, dklen=32)
    m_key_1 = str(m_key)
    return m_key_1


def genkey() -> str:
    key = os.urandom(32)
    key_1 = str(key)
    return key_1


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
    new_xesh_2 = str(new_xesh_1)
    if new_xesh_2 == old_xesh:  ## type: ignore
        return True
    else:

        return False


if __name__ == '__main__':
    print('Это модуль')
