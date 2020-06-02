import os
import sesurity

note_format_1 = '.txt.aes'
note_format_2 = '.txt'


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


def create_note(path_dir, way_key, password):
    print("=====Создание заметки=====")
    flag = 0
    while True:
        note_way = create_path_note_2(path_dir)
        try:
            note_file = open(note_way, 'w')
        except Exception:
            if flag == 3:
                print("=====Первышен лимит неверного ввода=====")
                return False
            print("=====Недопустимые символы в название заметки=====")
            flag += 1
        else:
            print("=====Заметка созданна=====")
            note_file.close()
            ses_dec = sesurity.decrypt(way_key, sesurity.master_key(password))
            sesurity.encrypt(note_way, ses_dec)
            os.remove(ses_dec)
            return True


def edit_note(path_dir, way_key, password, acc_name):
    print("=====Редактирование заметки=====")
    dir = all_notes(path_dir, acc_name)
    if dir == False:
        return False
    while True:
        note_way = create_path_note_1(path_dir)
        if note_way == False:
            return False
        check = os.path.exists(note_way)
        if check == True:
            ses_dec = sesurity.decrypt(way_key, sesurity.master_key(password))
            note = sesurity.decrypt(note_way, ses_dec)
            os.system(note)
            sesurity.encrypt(note, ses_dec)
            os.remove(ses_dec)
            print("=====Заметка изменена=====")
            return True
        elif check == False:
            back = back_note()
            if back == True:
                continue
            elif back == False:
                return False


def back_note():
    print("=====Заметки не существует=====")
    while True:
        command = input("\t1) Продолжить.\n"
                        "\t2) Выйте в меню заметок.\n"
                        "\t>> ")
        if command == '1':
            return True
        elif command == '2':
            print("=====Возврат в меню заметок=====")
            return False
        elif command != '1' and command != '2':
            print("=====Неверный ввод. Попробуйте сново=====")
            continue
        else:
            print("=====Error=====")
            exit()


def delet_note(path_dir, acc_name):
    print("=====Удаление ззаметки=====")
    dir = all_notes(path_dir, acc_name)
    if dir == False:
        return False
    while True:
        delete_way = create_path_note_1(path_dir)
        check = os.path.exists(delete_way)
        if check == True:
            os.remove(delete_way)
            print("=====Записка удалена=====")
            return True
        elif check == False:
            back = back_note()
            if back == True:
                continue
            elif back == False:
                return False


def all_notes(path_dir, acc_name):
    dir = os.listdir(path_dir)
    dir.remove('system.conf.aes')
    dir.remove('g.conf.aes')
    for i in range(len(dir)):
        note = dir[i]
        note = note.rstrip('.txt.aes')
        dir[i] = note
    if len(dir) == 0:
        print("=====Заметок на аккаунте нету=====")
        return False
    print("=====Все заметки на аккаунте " + acc_name + "'а=====")
    print('\t' + str(dir))
    return dir


def delet_all_notes(path_dir, acc_name):
    print("=====Удаление всех заметок=====")
    dir = all_notes(path_dir, acc_name)
    while True:
        last_chance = input("Вы уверен что хотите удалить все эти записки?\n"
                            "\t1) Да\n"
                            "\t2) Нет\n"
                            "\t>> ")
        if last_chance == '1':
            for i in range(len(dir)):
                dir[i] = dir[i] + '.txt.aes'
                delet_file = os.path.join(path_dir, dir[i])
                os.remove(delet_file)
            print("=====Все заметки удаленны=====\n"
                  "=====Возврат в меню хаметок=====")
            return True
        elif last_chance == '2':
            print("=====Отмена удаление всех заметок=====\n"
                  "=====Возврат в меню заметок=====")
            return False
        elif last_chance != '1' and last_chance != '2':
            print("=====Неверный ввод. Попробуйте сново=====")
            continue
        else:
            print("=====Error=====")
            exit()


if __name__ == '__main__':
    print('Это модуль')
