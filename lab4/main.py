import os
import shutil
import sesurity

inf_acc_en = 'system.conf'
inf_acc_de = inf_acc_en + '.aes'
inf_key_en = 'g.conf'
inf_key_de = inf_key_en + '.aes'
note_format_1 = '.txt.aes'
note_format_2 = '.txt'


def back():
    while True:
        command = input("\t1) Продолжить.\n"
                        "\t2) Завершить создание аккаунта.\n"
                        "\t>> ")
        if command == '1':
            return True
        elif command == '2':
            print("=====Создание аккаунта прерванно====\n"
                  "=====Возврат в главное меню=====")
            return False
        elif command != '1' and command != '2':
            print("=====Неверный ввод. Попробуйте сново=====")
            continue
        else:
            print("=====Error=====")
            exit()


def enter_path():
    path = os.getcwd()
    path = path.replace(' ', '_')
    path = path.replace('(', '[')
    path = path.replace(')', ']')
    check = os.path.exists(path)
    if check == False:
        os.mkdir(path)
    print(path)
    path = os.path.join(path, 'inf')
    print(path)
    check = os.path.exists(path)
    if check == False:
        os.mkdir(path)
    acc_name = input("Введите имя пользователя:\n"
                     "\t>> ")
    try:
        os.mkdir(path)
    except FileExistsError:
        pass
    fullpath = os.path.join(path, acc_name)
    print(fullpath)
    name_chek = os.path.exists(fullpath)
    return acc_name, name_chek, fullpath


def creatacc():
    print("=====Регистрация пользователья=====")
    while True:
        acc_name, name_chek, fullpath = enter_path()
        if name_chek == True:
            print("=====Имя пользователя занято=====")
            chek = back()
            if chek == False:
                return False
            elif chek == True:
                continue
        elif name_chek == False:
            while True:
                try:
                    password_1 = str(input("Придумайте пароль.\n"
                                           "\t>> "))
                    password_2 = str(input("Повторите пароль.\n"
                                           "\t>> "))
                except TypeError:
                    print("=====Неверный ввод. Попробуйте сново=====")
                    continue
                if password_1 != password_2:
                    print("=====Пароли не совпадают=====")
                    chek = back()
                    if chek == False:
                        return False
                    elif chek == True:
                        continue
                elif password_1 == password_2:
                    password = password_1
                    os.mkdir(fullpath)
                    way = os.path.join(fullpath, inf_acc_en)
                    way_key = os.path.join(fullpath, inf_key_en)
                    sesurity.encrypt(sesurity.create_hash_file(password, acc_name, way),
                                     sesurity.create_genkey_enfile(sesurity.genkey(), sesurity.master_key(password),
                                                                   way_key))

                    print("=====Аккаунт создан======")

                    return acc_name, password
            break


def deletacc():
    print("=====Удаление аккаунта=====")
    acc_name, name_chek, fullpath = enter_path()  # 0 - Путь, 1 - имя аккаунта, 2 - директория польователя
    if name_chek == False:
        print("=====Аккаунта не существует=====\n"
              "=====Возврат в главное меню=====")
        return False
    elif name_chek == True:
        flag = 0
        way = os.path.join(fullpath, inf_acc_de)
        way_key = os.path.join(fullpath, inf_key_de)
        while flag < 3:
            password = input("Введите пароль для удаления аккаунта.\n"
                             "\t>>> ")
            check = sesurity.check_pass(
                sesurity.decrypt(way, sesurity.create_genkey_defile(way_key, sesurity.master_key(password))), acc_name,
                password)
            if check == True:
                while True:
                    last_chance = input("Вы точно хотите удалить аккаунт?\n"
                                        "\t1) Да\n"
                                        "\t2) Нет\n"
                                        "\t>> ")
                    if last_chance == '1':
                        print("=====Аккаунт удалён=====\n"
                              "=====Возврат в главное меню=====")
                        shutil.rmtree(fullpath)
                        return False
                    elif last_chance == '2':
                        print("=====Возврат в главное меню=====")
                        return False
                    elif last_chance != '1' and last_chance != '2':
                        print("=====Неверный ввод. Попробуйте сново=====")
                        continue
                    else:
                        print("=====Error=====")
                        exit()
            else:
                if flag == 2:
                    print("=====Превышен лимит неверного ввода=====\n"
                          "=====Возврат в главное меню=====")
                    return False
                print("=====Неверный ввод. Попробуйте сново=====")
                flag += 1


def autacc():  # false - если аккаунта не существует, или если превышен лимит ввода пароля. В противном случаи возвращает имя, пароль и путь
    print("=====Аутентификация аккаунта=====")
    acc_name, name_chek, fullpath = enter_path()
    if name_chek == False:
        print("Аккаунта не существует, создайте аккаунт.\n"
              "=====Возврат в главное меню=====")
        return False
    elif name_chek == True:
        flag = 0
        way = os.path.join(fullpath, inf_acc_de)
        way_key = os.path.join(fullpath, inf_key_de)
        while True:
            password = input("Введите пароль для авторизацие.\n"
                             "\t>> ")

            check = sesurity.check_pass(
                sesurity.decrypt(way, sesurity.create_genkey_defile(way_key, sesurity.master_key(password))), acc_name,
                password)
            if check == True:
                print("=====Вход произведён=====\n"
                      "Здравствуйте " + acc_name + "!")
                return fullpath, password, acc_name, way_key
            elif check == False:
                if flag == 2:
                    print("=====Превышен лимит неверного ввода=====\n"
                          "=====Возврат в главное меню=====")
                    return False
                print("=====Неверный ввод. Попробуйте сново=====")
                flag += 1


def create_path_note_1(path_dir):
    flag = True
    count = 0
    while True:
        note_name = str(input("Введите название заметки.\n"
                              "\t>> "))
        note_name = note_name.replace(' ', '_')
        note_name = note_name.replace('(', '[')
        note_name = note_name.replace(')', ']')
        char_error = ['\\', '/', ';', ':', '*', '?', '|', '>', '<']
        for char in note_name:
            if char_error.count(char) != 0:
                print("=====Недопустимое название заметки. Попробуйте сново=====")
                count += 1
                flag = False
                break
        if flag == False:
            if count == 3:
                print("=====Превышен лимит неверного ввода=====")
                return False
            continue
        note_name = note_name + note_format_1
        note_way = os.path.join(path_dir, note_name)
        return note_way


def create_path_note_2(path_dir):
    count = 0
    flag = True
    while True:
        note_name = str(input("Введите название заметки.\n"
                              "\t>> "))
        note_name = note_name.replace(' ', '_')
        note_name = note_name.replace('(', '[')
        note_name = note_name.replace(')', ']')
        char_error = ['\\', '/', ';', ':', '*', '?', '|', '>', '<']
        for char in note_name:
            if char_error.count(char) != 0:
                print("=====Недопустимое название заметки. Попробуйте сново=====")
                count += 1
                flag = False
                break
        if flag == False:
            if count == 3:
                print("=====Превышен лимит неверного ввода=====")
                return False
            continue
        note_name = note_name + note_format_2
        note_way = os.path.join(path_dir, note_name)
        return note_way


if __name__ == '__main__':
    print('Это модуль, запускать lab.py')
