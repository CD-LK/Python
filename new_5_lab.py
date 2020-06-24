import multiprocessing as mlp
import time
import math
import os
import sys
from typing import Tuple, List


def Atkin(limit: int, file: str, start: int) -> None:
    sieve = [False] * (limit + 1)
    t = time.time()
    print("Процесс №:00-" + str(start) + " запущен.")
    for x in range(start, int(math.sqrt(limit)) + 1, 3):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
            if time.time() - t >= 5:
                print('Процесс №:00-' + str(start) + '. x - ' + str(x) + '|y - ' + str(y))
                t = time.time()
    with open(file, 'w') as file_w:
        for i in range(len(sieve)):
            file_w.write(str(sieve[i]) + '\n')
    print("Процесс №:00-" + str(start) + " закончен.")


def creat_path(name: str) -> str:  # Создает файл с name, возвращает путь к файлу.
    path = os.getcwd()
    full_path = os.path.join(path, name)
    with open(full_path, 'w') as file:
        pass
    return full_path


def pool_creat_path(name_1: str = 'Process_1.txt', name_2: str = 'Process_2.txt',
                    name_3: str = 'Process_3.txt') -> List[str]:
    with mlp.Pool(processes=3) as pl:
        pool_file = pl.map(creat_path, iterable=[name_1, name_2, name_3])
        pl.close()
    return pool_file


def pool_Atkin(limit: int, file_1: str, file_2: str, file_3: str) -> None:
    with mlp.Pool(processes=3) as pl:
        pool = pl.starmap(Atkin, iterable=[
            [limit, file_1, 1],
            [limit, file_2, 2],
            [limit, file_3, 3]
        ])
        pl.close()


def read_file(path_file: str, start: int) -> List[str]:  # Считывае инормацию из процессов
    print("Процесс №:00-" + str(start) + " чтение данных.")
    with open(path_file, 'r') as file_read:
        prime_list = file_read.read().rstrip('\n').replace('\n', ' ').split(' ')
    return prime_list


def pool_read_file(file_1: str, file_2: str, file_3: str) -> List[List[str]]:
    with mlp.Pool(processes=3) as pl:
        pool_list = pl.starmap(read_file, iterable=[[file_1, 1], [file_2, 2], [file_3, 3]])
        pl.close()
    return pool_list


def finaly(list_1: List[str], list_2: List[str], list_3: List[str]) -> List[bool]:
    lens = len(list_1)
    finaly_list = [False] * lens
    print("Оброботка данных.")
    for i in range(0, lens):
        if list_1[i] == 'False':
            p_1 = False
        else:
            p_1 = True
        if list_2[i] == 'False':
            p_2 = False
        else:
            p_2 = True
        if list_3[i] == 'False':
            p_3 = False
        else:
            p_3 = True
        finaly_list[i] = (p_1 + p_2 + p_3) % 2
    prime_list = [False] * len(finaly_list)
    for num, chek in enumerate(finaly_list):
        if chek == 1:
            if num % 5 == 0:
                pass
            else:
                prime_list[num] = num
    for x in range(5, int(math.sqrt(len(finaly_list)))):
        if prime_list[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                prime_list[y] == False
    return prime_list


"""def start_list():
    path = os.getcwd()
    name = 'Prime.txt'
    full_path = os.path.join(path, name)
    with open(full_path, 'r') as prime:
        start_list = prime.read().rstrip('\n').replace('\n', ' ').split(' ')
    if start_list == ['']:
        return [2, 3, 5]
    else:
        return start_list"""

if __name__ == '__main__':
    try:
        z = time.time()
        start_list = [2, 3, 5]
        proggram, (argv_1) = sys.argv
        limit = int(argv_1)
        # start_prime_list = start_list()
        file1, file2, file3 = pool_creat_path()
        pool_Atkin(limit, file1, file2, file3)
        list1, list2, list3 = pool_read_file(file1, file2, file3)
        prime_list = finaly(list1, list2, list3)
        while len(prime_list) > limit:
            prime_list.pop()
        f_list = []
        for index, num in enumerate(prime_list):
            if num is not False:
                f_list.append(num)
        f_list.sort()
        print("Время работы: " + str(time.time() - z) + 'секунды')
        path = creat_path('Prime.txt')
        with open(path, 'w')as file:
            file.write('2\n3\n5\n')
            for i, val in enumerate(f_list):
                file.write(str(f_list[i]) + '\n')
    except ValueError:
        print("Недостаточно входных данных")
    except MemoryError:
        print("Входные данные велики.")
    except BaseException:
        print("Досрочный выход.")
