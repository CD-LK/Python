import multiprocessing as mlp
import math
import os
import time
import sys
from typing import Tuple, List
from typing import TypeVar, Generic


def Atkin(
        num: int) -> bool:  # Алгорит Аткина для одного числа, не убирает числа делимые на полный квадрат простых чисел
    count_1, count_2, count_3 = 0, 0, 0
    for x in range(1, int(math.sqrt(num)) + 1):
        for y in range(1, int(math.sqrt(num)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n == num and num % 4 == 1:
                count_1 += 1
            n = 3 * x ** 2 + y ** 2
            if n == num and num % 6 == 1:
                count_2 += 1
            n = 3 * x ** 2 - y ** 2
            if x > y and n == num and num % 12 == 11:
                count_3 += 1
    # print(str(num) + ' ' + str(count_1) + ' ' + str(count_2) + ' ' + str(count_3))
    if count_1 % 2 == 1 or count_2 % 2 == 1 or count_3 % 2 == 1:
        # print(str(num) + ' True')
        return True
    else:
        # print((str(num) + ' False'))
        return False


def split(low_limit: int, upp_limit: int) -> Tuple[
    List[int], List[int], List[int]]:  # Разделяет список от нижнего до верхнего придела на 3 списка
    list_1 = []
    list_2 = []
    list_3 = []
    for i in range(low_limit, upp_limit, 3):
        list_1.append(i)
        list_2.append(i + 1)
        list_3.append(i + 2)
    return list_1, list_2, list_3


def str_in_int(data_list: List[str]) -> List[int]:  # Переводит все строчные типы в интовские типы
    new_data_list = []
    for i in range(len(data_list)):
        char = int(data_list[i])
        new_data_list.append(char)
    return new_data_list


def int_in_str(data_list: List[int]) -> List[str]:  # Переводит все строчные типы в интовские типы
    new_data_list = []
    for i in range(len(data_list)):
        char = str(data_list[i])
        new_data_list.append(char)
    return new_data_list


def prime_and_squares_prime(data_list: List[int],
                            path_data_file: str) -> None:  # Получение списка простых и делимых на простые чисел из списка чисел
    t = time.time()
    try:
        for i in range(len(data_list)):
            is_prime = Atkin(data_list[i])
            if is_prime == True:
                if time.time() - t >= 1.0:
                    t = time.time()
                    print(str(data_list[i]) + ' is prime')
                with open(path_data_file, 'a') as file:
                    file.write(str(data_list[i]) + '\n')
    except IndexError:
        pass


def read_process_prime_lists(prime_file_name: str) -> List[str]:  # Считываем результаты вычисления из процессов
    with open(prime_file_name, 'r') as file:
        prime_list = file.read().rstrip('\n').replace('\n', ' ').split(' ')
        return prime_list


def read_old_prime_list(prime_file_name: str) -> List[str]:  # Получаем начальный список простых чисел
    start_prime_list = ['2', '3', '5']
    with open(prime_file_name, 'r') as file:
        prime_list = file.read().rstrip('\n').replace('\n', ' ').split(' ')
    if prime_list[0] == '':
        return start_prime_list
    else:
        # prime_list = str_in_int(prime_list)
        return prime_list


def create_file(name: str) -> str:  # Получаем путь к файлу куда записываюсть значения
    path = os.getcwd()
    path_txt = os.path.join(path, name)
    with open(path_txt, 'w')as file:
        pass
    return path_txt


def sort_and_del_squares(start_list: List[int], list_1: List[int], list_2: List[int],
                         list_3: List[int]) -> List[int]:  # избовляемся от всех делим на полный квадрат и сортируем
    full_list = start_list + list_1 + list_2 + list_3
    full_list = sorted(full_list)
    len_list = len(full_list)
    for i in range(len_list - 1, 0, -1):
        char = full_list[i]
        count = full_list.count(full_list[i])
        if count > 1:
            full_list.remove(full_list[i])
        for x in range(0, i - 1):
            n = full_list[x]
            if char % n ** 2 == 0:
                full_list.remove(char)
                break
    return full_list


def write_prime(prime_file: str, data_list: List[int]) -> None:  # Записываем все простые числа в файл
    with open(prime_file, 'w') as file:
        for i in range(len(data_list)):
            file.write(str(data_list[i]) + '\n')


if __name__ == '__main__':
    ppp, arg_1 = sys.argv
    upp_limit = int(arg_1)
    prime_txt = create_file('Prime.txt')
    lisss = read_old_prime_list(prime_txt)
    start_prime_list = str_in_int(lisss)
    low_limit = start_prime_list[len(start_prime_list) - 1]
    list_1, list_2, list_3 = split(low_limit, upp_limit)
    file_process_1 = create_file('Process_1.txt')
    file_process_2 = create_file('Process_2.txt')
    file_process_3 = create_file('Process_3.txt')
    try:
        process_1 = mlp.Process(target=prime_and_squares_prime, name='Process_1', args=(list_1, file_process_1))
        process_2 = mlp.Process(target=prime_and_squares_prime, name='Process_2', args=(list_2, file_process_2))
        process_3 = mlp.Process(target=prime_and_squares_prime, name='Process_3', args=(list_3, file_process_3))

        process_1.start()
        process_2.start()
        process_3.start()

        process_1.join()
        process_2.join()
        process_3.join()
    except BaseException:
        pass
    finally:
        k1 = read_process_prime_lists('Process_1.txt')
        k2 = read_process_prime_lists('Process_2.txt')
        k3 = read_process_prime_lists('Process_3.txt')

        l1 = str_in_int(k1)
        l2 = str_in_int(k2)
        l3 = str_in_int(k3)
        final_list = sort_and_del_squares(start_prime_list, l1, l2, l3)
        write_prime(prime_txt, final_list)
