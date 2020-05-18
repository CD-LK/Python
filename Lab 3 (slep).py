import random
from abc import ABC, abstractmethod


class Main(ABC):
    """Метод генерации ключа"""

    @abstractmethod
    def genkey(self):
        pass

    @abstractmethod
    def key_error(self, key_name):
        pass

    """Метод Шифрования"""

    @abstractmethod
    def encrypt(self):
        pass

    """Метод Расшифрования """

    @abstractmethod
    def decrypt(self):
        pass

    def _way_test(self, format):
        while True:
            way = input("Введите путь или имя файла  с расширением ." + str(format) + "\n"
                                                                                      "\t>>")
            try:
                file = open(way, 'r')
            except FileNotFoundError:
                print("Файл не найден!\n"
                      "Попробуйте сново.")
                continue
            except Exception:
                print("Файл не найден!\n"
                      "Попробуйте сново.")
                continue
            else:
                file.close()
                test = way.split('.')
                if test[len(test) - 1] == format:
                    break
                elif test[len(test) - 1] != format:
                    print("Недопустимый формат файла!\n"
                          "Попробуйте сново.")
                    continue
                else:
                    print("Неизвестная ошибка!")
                    exit()
        return way

    def _decrypt_file(self, file_decrypt_name):
        split_name = file_decrypt_name.split('.')
        file_text_name = [x for x in range(len(split_name) - 1)]
        if len(split_name) > 2:
            for i in range(len(split_name) - 1):
                file_text_name[i] = split_name[i]
        elif len(split_name) == 2:
            file_text_name[0] = split_name[0]
            file_text_name[1] = 'txt'
        else:
            print("Неизвестная ошибка!")
            exit()
        file_text_name = '.'.join(file_text_name)  # Название расшифровоного текста
        file_text = open(file_text_name, 'w')  # Создание расшифровоного файла
        file_text.close()
        return file_decrypt_name, file_text_name


"""Перестановка"""


class Method_2(Main):
    def genkey(self):
        while True:
            file_key_name = input("Введите названия файла-ключа для его создания.\n"
                                  "\t>>")
            file_key_name = file_key_name + '.key'
            try:
                key_file = open(file_key_name, 'w')
            except Exception:
                print("Неккоректный ввод.\n"
                      "Попробуйтесново")
                continue
            else:
                while True:
                    try:
                        len_key = int(input("Введите длину ключа:\n"
                                            "\t>> ")) + 1
                    except ValueError:
                        print("Вы ввели не целое число.\n"
                              "Попытайтесь снова.")
                    else:
                        if len_key <= 2:
                            print("Длина ключа должна быть больше 2.\n"
                                  "Попытайтесь снова.")
                            continue
                        elif len_key > 2:
                            break
                        else:
                            print("Неизвестная ошибка!")
                            exit()

                key_list = [x for x in range(1, int(len_key))]
                random.shuffle(key_list)
                for i in range(len_key - 1):
                    key_file.writelines(str(key_list[i]) + '\n')
                key_file.write("Перестановка")
                print("Ключ сгенирирован.\n"
                      "Возврат в главное меню.")
                key_file.close()
                break

    def key_error(self, key_name):
        while True:
            with open(key_name, 'r') as file_key:
                key_size = len(file_key.readlines()) - 1
                file_key.seek(0)
                for line in range(key_size):
                    file_key.readline()
                f = file_key.readline()
                if f == "Перестановка":
                    print('')
                elif f != "Перестановка":
                    print("Недопустимы тип ключа.\n"
                          "Пожалуйста сгенерируйте ключ.\n")
                    return False
                else:
                    print("Неизвестная ошибка!")
                    exit()
                file_key.seek(0)
                key_list = [x for x in range(key_size)]
                for index in range(0, key_size):
                    try:
                        key_list[index] = int(file_key.readline())
                    except ValueError:
                        print("В ключе обнаруженно значение отличающиеся от целочисленного.\n"
                              "Пожалуйста сгенерируйте ключ.")
                        return False
            return key_list

    def encrypt(self):
        while True:
            file_text_name = self._way_test('txt')
            file_name_encrypt = file_text_name + '.encrypt'  # название файла шифртекста
            file_en = open(file_name_encrypt, 'w')  # Открываем файл и очищаем его, или создаём файл
            file_en.close()  # Закрываем файл

            key_list = self.key_error(self._way_test('key'))
            if key_list == False:
                break

            while True:
                with open(file_text_name, 'r', encoding='utf-8') as file_txt:
                    key_app_qua = int(len(file_txt.read()) / len(key_list)) + 1  # Дробление текста по ключу
                    with open(file_name_encrypt, 'a', encoding='utf-8') as file_crypt:
                        file_crypt.write('Перестановка\n')
                        file_txt.seek(0)
                        for num in range(key_app_qua):
                            line = file_txt.read(len(key_list))
                            split_txt = list(line)
                            for i in range(len(split_txt)):
                                if split_txt[i] == '\n':
                                    split_txt[i] = ' '
                                else:
                                    continue
                            en_txt = [x for x in range(len(key_list))]
                            for i in range(len(key_list)):
                                try:
                                    en_txt[i] = split_txt[int(key_list[i]) - 1]
                                except IndexError:
                                    en_txt[i] = '@'
                                finally:
                                    # print(str(i + 1) + '-' + str(en_txt[i]))
                                    file_crypt.write(str(en_txt[i]))

                break
            print("Текст засшифрован\n"
                  "Возврат в главное меню.")
            break

    def decrypt(self):
        file_decrytp_text_name = self._decrypt_file(self._way_test('encrypt'))  # 0 - шифртекст, 1 - текст
        while True:

            while True:
                with open(file_decrytp_text_name[0], 'r', encoding='utf-8') as file_de:
                    file_de.seek(0)
                    if file_de.readline() == 'Перестановка\n':
                        print('')
                    elif file_de.readline() != 'Перестановка\n':
                        print("Файл шифртекста не совпадает с методом расшифровкию"
                              "Возврат в главное меню.")
                        break
                    else:
                        print("Неизвестная ошибка!")
                        exit()
                    split_key = self.key_error(self._way_test('key'))
                    key_app_qua = int(len(file_de.readline()) / len(split_key))
                    file_de.seek(0)
                    file_de.readline()
                    for num in range(key_app_qua):
                        line = file_de.read(len(split_key))
                        split_txt = list(line)
                        de_txt = [x for x in range(len(split_key))]
                        for i in range(len(split_key)):
                            de_txt[int(split_key[i]) - 1] = split_txt[i]
                        if num == key_app_qua - 1:
                            for i in range(len(split_key) - 1, 0, -1):
                                if de_txt[i] == '@':
                                    de_txt[i] = ''
                                else:
                                    break
                        # print(de_txt)
                        for i in range(len(split_key)):
                            with open(file_decrytp_text_name[1], 'a') as file_decript:
                                file_decript.write(str(de_txt[i]))
                break
            print("Текст расшифрован\n"
                  "Возврат в главное меню.")
            break


"""Замена"""


class Method_1(Main):
    def genkey(self):
        file_a_name = self._way_test('alph')
        with open(file_a_name, 'r', encoding='utf-8') as file_alph:
            size_alph = len(file_alph.readlines())
            alph_list = []
            file_alph.seek(0)
            for i in range(size_alph):
                char = file_alph.read(1)
                if char =='\n':
                    continue
                alph_list.append(char)
                file_alph.readline()
        for i in range(len(alph_list)):

            try:
                if alph_list.count(alph_list[i]) > 1:
                    del_sim = alph_list[i]
                    alph_list.reverse()
                    alph_list.remove(del_sim)
                    alph_list.reverse()
            except IndexError:
                continue
        key_list = alph_list.copy()
        random.shuffle(key_list)
        while True:
            file_key_name = input("Введине название файла-ключа, который хотите сгенирировать.\n"
                                  "\t>>")
            file_key_name = file_key_name + '.key'
            try:
                key_file = open(file_key_name, 'w', encoding='utf-8')
            except Exception:
                print("Неккоректный ввод.\n"
                      "Попробуйтесново")
                continue
            else:
                for i in range(len(alph_list)):
                    key_file.writelines(str(alph_list[i]) + " - " + str(key_list[i]) + '\n')
                key_file.writelines('Замена')
                print("Ключ сгенирирован.\n"
                      "Возврат в главное меню.")
                key_file.close()
                break

    def key_error(self, key_name):
        while True:
            with open(key_name, 'r', encoding='utf-8') as file_key:
                key_size = len(file_key.readlines()) - 1
                file_key.seek(0)
                for line in range(key_size):
                    file_key.readline()
                f = file_key.readline()
                if f == 'Замена':
                    pass
                elif f != 'Замена':
                    print("Недопустимы тип ключа.\n"
                          "Пожалуйста сгенерируйте ключ.\n")
                    return False
                else:
                    print("Неизвестная ошибка!")
                    exit()
                alph_list = []
                key_list = alph_list.copy()
                file_key.seek(0)
                for i in range(key_size):
                    line = file_key.readline().split(' - ')
                    if len(line) > 2 or len(line) < 2:
                        continue
                    elif len(line) == 2:
                        if len(line[0]) == 1:
                            alph_list.append(line[0])
                        elif len(line[0]) != 1:
                            print("Алфавитная часть ключа содержит элемент длинны больше двух.\n"
                                  "Пожалуйста сгенерируйте ключ.")
                            return False
                        else:
                            print("Неизвестная ошибка!")
                            exit()
                        line[1] = line[1].split('\n')
                        if len(line[1][0]) == 1:
                            key_list.append(line[1][0])
                        elif len(line[1][0]) != 1:
                            print(line)
                            print(line[1])
                            print("Шифрующая часть ключа содержит элемент длинны больше двух.\n"
                                  "Пожалуйста сгенерируйте ключ.")
                            return False
                        else:
                            print("Неизвестная ошибка!")
                            exit()
                    else:
                        print("Неизвестная ошибка!")
                        exit()
                for i in range(len(alph_list)):
                    try:
                        if alph_list.count(alph_list[i]) > 1:
                            print("В алфовитной части ключа есть повторение, дальнейшая работа невозможна.\n"
                                  "Пожалуйста сгенерируйте ключ.")
                            return False
                    except IndexError:
                        continue
                for i in range(len(alph_list)):
                    try:
                        if alph_list.count(key_list[i]) > 1:
                            print("В шифрующей части ключа есть повторение, дальнейшая работа невозможна.\n"
                                  "Пожалуйста сгенерируйте ключ.")
                            return False
                    except IndexError:
                        continue
            alph = alph_list.copy()
            key = key_list.copy()
            break
        return alph, key

    def _encrypt_writhe(self, file_text_name, file_name_encrypt, alph_key, encoding):
        with open(file_text_name, 'r', encoding=encoding) as file_txt:
            file_txt.seek(0)
            file_size = len(file_txt.read())
            file_txt.seek(0)
            with open(file_name_encrypt, 'a')as file_crypt:
                file_crypt.write('Замена\n')
                for i in range(file_size):
                    char = file_txt.read(1)
                    for key_size in range(len(alph_key[0])):
                        if char == alph_key[0][key_size]:
                            file_crypt.writelines(alph_key[1][key_size])
                            break
                        elif key_size == len(alph_key[0]) - 1 and char != alph_key[0][key_size]:
                            file_crypt.writelines(str(char))
                        elif char != alph_key[0][key_size]:
                            continue
        print("Текст засшифрован\n"
              "Возврат в главное меню.")

    def encrypt(self):
        file_text_name = self._way_test('txt')
        file_name_encrypt = file_text_name + '.encrypt'  # название файла шифртекста
        file_en = open(file_name_encrypt, 'w')  # Открываем файл и очищаем его, или создаём файл
        file_en.close()  # Закрываем файл
        alph_key = self.key_error(self._way_test('key'))
        if alph_key != False:
            try:
                self._encrypt_writhe(file_text_name, file_name_encrypt, alph_key, 'utf-8')
                print("Encoding: utf-8")
            except UnicodeDecodeError:
                self._encrypt_writhe(file_text_name, file_name_encrypt, alph_key, 'windows-1251')
                print("Encoding: windows-1251")
        elif alph_key == False:
            print('Возвращение в главное меню')
        else:
            print("Неизвестная ошибка!")
            exit()

    def decrypt(self):
        file_decrytp_text_name = self._decrypt_file(self._way_test('encrypt'))  # 0 - шифртекст, 1 - текст
        while True:
            with open(file_decrytp_text_name[0], 'r', encoding='windows-1251')as file_de:
                file_de.seek(0)
                if file_de.readline() == 'Замена\n':
                    pass
                elif file_de.readline() != 'Замена\n':
                    print("Файл шифртекста не совпадает с методом расшифровки.\n"
                          "Возврат в главное меню.")
                    break
                else:
                    print("Неизвестная ошибка!")
                    exit()
            alph_key = self.key_error(self._way_test('key'))
            if alph_key != False:
                with open(file_decrytp_text_name[0], 'r', encoding='windows-1251') as file_crypt:
                    file_size = len(file_crypt.read())
                    file_crypt.seek(0)
                    file_crypt.readline()
                    with open(file_decrytp_text_name[1], 'a')as file_txt:
                        for i in range(file_size):
                            char = file_crypt.read(1)
                            for key_size in range(len(alph_key[0])):
                                if char == alph_key[1][key_size]:
                                    file_txt.writelines(alph_key[0][key_size])
                                    break
                                elif key_size == len(alph_key[0]) - 1 and char != alph_key[1][key_size]:
                                    file_txt.writelines(str(char))
                                elif char != alph_key[1][key_size]:
                                    continue
            elif alph_key == False:
                print('Возврат в главное меню')
                break
            else:
                print("Неизвестная ошибка!")
                exit()
            print("Текст расшифрован\n"
                  "Возврат в главное меню.")
            break


"""Гаммирование"""


class Method_3(Main):
    def genkey(self):
        print("Необходимо ввести алфавит для которого будет генерироваться ключ.")
        file_alph_name = self._way_test('alph')
        with open(file_alph_name, 'r', encoding='utf-8')as file_alph:
            size_alph = len(file_alph.readlines())
            alph_list = [x for x in range(size_alph)]
            file_alph.seek(0)
            for i in range(size_alph):
                alph_list[i] = file_alph.read(1)
                file_alph.readline()
            for i in range(len(alph_list)):
                try:
                    char_count = alph_list.count(alph_list[i])
                    if char_count> 1:
                        del_sim = alph_list[i]
                        for i in range(char_count-1):
                            alph_list.reverse()
                            alph_list.remove(del_sim)
                            alph_list.reverse()
                except IndexError:
                    continue
            wrong_char_count_1 = alph_list.count('')
            wrong_char_count_2 = alph_list.count('\n')
            for i in range(wrong_char_count_1):
                alph_list.remove('')
            for i in range(wrong_char_count_2):
                alph_list.remove('\n')

        print(alph_list)
        mod = len(alph_list)
        while True:
            file_key_name = input("Введите имя файла ключа.\n"
                                  "\t>>")
            file_key_name = file_key_name + '.key'
            try:
                file_key = open(file_key_name, 'w', encoding='utf-8')
            except Exception:
                print("Неккоректный ввод.\n"
                      "Попробуйтесново")
                continue
            else:
                while True:
                    try:
                        len_key = int(input('Введите длину ключа.\n'
                                            '\t>>'))
                    except ValueError:
                        print("Необходимо ввести целочисленное значение.\n"
                              "Попробуйте сново.")
                        continue
                    else:
                        if len_key > 2:
                            key_list = [x for x in range(len_key)]
                            file_key.write(alph_list[0])
                            for i in range(1, len(alph_list)):
                                file_key.write(' - ' + str(alph_list[i]))
                            file_key.write('\n')
                            key_list[0] = random.randint(0, mod)
                            file_key.write(str(key_list[0]))
                            for i in range(1, len_key):
                                key_list[i] = random.randint(0, mod)
                                file_key.write(' - ' + str(key_list[i]))
                            file_key.write('\n')
                            file_key.writelines('Гаммирование')
                            print("Ключ сгенирирован.\n"
                                  "Возврат в главное меню.")
                            file_key.close()
                            break
                        else:
                            print("Значение должнно быть > 2.\n"
                                  "Попробуйте сново.")
                            continue
            break

    def key_error(self, key_name):
        while True:
            with open(key_name, 'r', encoding='utf-8')as file_key:
                key_size = len(file_key.readlines()) - 1
                file_key.seek(0)
                for i in range(key_size):
                    file_key.readline()
                f = file_key.readline()
                if f == 'Гаммирование':
                    print('')
                elif f != 'Гаммирование':
                    print("Недопустимы тип ключа.\n"
                          "Пожалуйста сгенерируйте ключ.\n")
                    return False
                else:
                    print("Неизвестная ошибка!\n"
                          "Экстренный выход из программы!")
                    exit()
                file_key.seek(0)
                alph_list = file_key.readline()
                key_list = file_key.readline()
                alph_list = alph_list.split(' - ')
                alph_list[len(alph_list) - 1] = alph_list[len(alph_list) - 1].split('\n')
                alph_list[len(alph_list) - 1] = alph_list[len(alph_list) - 1][0]
                key_list = key_list.split(' - ')
                key_list[len(key_list) - 1] = key_list[len(key_list) - 1].split('\n')
                key_list[len(key_list) - 1] = key_list[len(key_list) - 1][0]
            try:
                for i in range(len(key_list)):
                    int(key_list[i])
            except ValueError:
                print("В ключе обнаруженно значение отличающиеся от челочисленного.\n"
                      "Пожалуйста сгенерируйте ключ.")
                return False
            for i in range(len(alph_list)):
                if alph_list.count(alph_list[i]) > 1:
                    print("В алфовитной части ключа всречаеться повторение.\n"
                          "Сгенирируйте ключ.")
                    return False
                elif len(alph_list[i]) != 1:
                    print("Алфавитная часть ключа содержит элемент отличный от символа\n"
                          "генирируйте ключ.")
                    return False
                else:
                    continue
            return alph_list, key_list

    def encrypt(self):
        while True:
            file_text_name = self._way_test('txt')
            file_name_encrypt = file_text_name + '.encrypt'  # название файла шифртекста
            file_en = open(file_name_encrypt, 'w')  # Открываем файл и очищаем его, или создаём файл
            file_en.close()  # Закрываем файл
            file_alph_key = self.key_error(self._way_test('key'))  # 0 - алфавит, 1 - ключ/гамма
            if file_alph_key == False:
                break
            size_key = len(file_alph_key[1])

            with open(file_text_name, 'r', encoding='utf-8')as file_text:
                with open(file_name_encrypt, 'a', encoding='utf-8')as file_crypt:
                    file_crypt.write('Гаммирование\n')
                    size_txt = len(file_text.read())
                    # num_key = int((size_txt) / (size_key)) + 1
                    file_text.seek(0)
                    count = 0
                    for ch in range(size_txt):
                        char = file_text.read(1)
                        for i in range(len(file_alph_key[0])):
                            if char == file_alph_key[0][i]:
                                char = i
                                flag = True
                                break
                            elif char != file_alph_key[0][i] and i == len(file_alph_key) - 1:
                                flag = False
                        if flag == True:
                            char = char + int(file_alph_key[1][count])
                            char = char % len(file_alph_key[0])
                            char = file_alph_key[0][char]
                            file_crypt.write(char)
                            count += 1
                            if count == size_key:
                                count = 0
                            continue
                        elif flag == False:
                            file_crypt.write(char)
                            continue
            print("Текст засшифрован\n"
                  "Возврат в главное меню.")
            break

    def decrypt(self):
        file_decrytp_text_name = self._decrypt_file(self._way_test('encrypt'))  # 0 - шифртекст, 1 - текст
        while True:
            with open(file_decrytp_text_name[0], 'r', encoding='utf-8')as file_de:
                file_de.seek(0)
                if file_de.readline() == 'Гаммирование\n':
                    pass
                elif file_de.readline() != 'Гаммирование\n':
                    print("Файл шифртекста не совпадает с методом расшифровки.\n"
                          "Возврат в главное меню.")
                    break
                else:
                    print("Неизвестная ошибка!")
                    exit()
            file_alph_key = self.key_error(self._way_test('key'))  # 0 - алфавит, 1 - ключ/гамма
            size_key = len(file_alph_key[1])
            if file_alph_key == False:
                break
            with open(file_decrytp_text_name[0], 'r', encoding='utf-8')as file_crypt:
                size_crypt_text = len(file_crypt.read())
                file_crypt.seek(0)
                file_crypt.readline()
                with open(file_decrytp_text_name[1], 'a')as file_text:
                    count = 0
                    for ch in range(size_crypt_text):
                        char = file_crypt.read(1)
                        for i in range(len(file_alph_key[0])):
                            if char == file_alph_key[0][i]:
                                char = i
                                flag = True
                                break
                            elif char != file_alph_key[0][i] and i == len(file_alph_key) - 1:
                                flag = False
                        if flag == True:
                            char = char + len(file_alph_key[0])
                            char = char - int(file_alph_key[1][count])
                            char = char % len(file_alph_key[0])
                            char = file_alph_key[0][char]
                            file_text.write(char)
                            count += 1
                            if count == size_key:
                                count = 0
                                continue
                        elif flag == False:
                            file_text.write(char)
                            continue
            print("Текст расшифрован\n"
                  "Возврат в главное меню.")
            break


obj_1 = Method_1()
obj_2 = Method_2()
obj_3 = Method_3()

flag = True
while True:
    select = input("Главное меню:\n"
                   "\t1) Зашифровать текст.\n"
                   "\t2) Расшифровать текст.\n"
                   "\t3) Сгенирировать ключь.\n"
                   "\t4) Выход.\n"
                   "\t>> ")
    if select == '1':
        while True:
            encript_select = input("Шифрование.\n"
                                   "Выберите метод шифрования:\n"
                                   "\t1) Замена.\n"
                                   "\t2) Перестановка.\n"
                                   "\t3) Гаммирование.\n"
                                   "\t4) Главное меню.\n"
                                   "\t>> ")
            if encript_select == '1':
                obj_1.encrypt()
                break
            elif encript_select == '2':
                obj_2.encrypt()
                break
            elif encript_select == '3':
                obj_3.encrypt()
                break
            elif encript_select == '4':
                break
            elif encript_select != '1' and encript_select != '2' and encript_select != '3' and encript_select != '4':
                print("Невверный ввод\n"
                      "Попробуйте сново:")
            else:
                print("Неизвестная ошибка!\n"
                      "Экстренный выход из программы!")
                exit()

    elif select == '2':
        while True:
            decript_select = input("Расшифровка.\n"
                                   "Выберите метод расифрования:\n"
                                   "\t1) Замена.\n"
                                   "\t2) Перестановка.\n"
                                   "\t3) Гаммирование.\n"
                                   "\t4) Главное меню.\n"
                                   "\t>> ")
            if decript_select == '1':
                obj_1.decrypt()
                break
            elif decript_select == '2':
                obj_2.decrypt()
                break
            elif decript_select == '3':
                obj_3.decrypt()
                break
            elif decript_select == '4':
                break
            elif decript_select != '1' and decript_select != '2' and decript_select != '3' and decript_select != '4':
                print("Невверный ввод\n"
                      "Попробуйте сново:")
            else:
                print("Неизвестная ошибка!\n"
                      "Экстренный выход из программы!")
                exit()
    elif select == '3':
        while True:
            genkey_select = input("Генрация ключа.\n"
                                  "Выберите для какого метода сгенирировать ключ:\n"
                                  "\t1) Замена.\n"
                                  "\t2) Перестановка.\n"
                                  "\t3) Гаммирование.\n"
                                  "\t4) Главное меню.\n"
                                  "\t>> ")
            if genkey_select == '1':
                obj_1.genkey()
                break
            elif genkey_select == '2':
                obj_2.genkey()
                break
            elif genkey_select == '3':
                obj_3.genkey()
                break
            elif genkey_select == '4':
                break
            elif genkey_select != '1' and genkey_select != '2' and genkey_select != '3':
                print("Невверный ввод\n"
                      "Попробуйте сново:")
            else:
                print("Неизвестная ошибка!\n"
                      "Экстренный выход из программы!")
                exit()
    elif select == '4':
        break
    elif select != '1' and select != '2' and select != '3' and select != '4':
        print("Невверный ввод\n"
              "Попробуйте сново:")
    else:
        print("Неизвестная ошибка!\n"
              "Экстренный выход из программы!")
        exit()
