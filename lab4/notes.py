import os
import sesurity
import main

note_format_1 = '.txt.aes'
note_format_2 = '.txt'


def create_note(path_dir, way_key, password):
    flag = 0
    while True:
        note_way = main.create_path_note_2(path_dir)
        if note_way == False:
            return 1
        try:
            note_file = open(note_way, 'w')
        except Exception:
            if flag == 3:
                return 2
            main.error()
            flag += 1
        else:

            note_file.close()
            ses_dec = sesurity.decrypt(way_key, sesurity.master_key(password))
            sesurity.encrypt(note_way, ses_dec)
            os.remove(ses_dec)
            return True


def edit_note(path_dir, way_key, password, acc_name):
    dir = all_notes(path_dir, acc_name)
    if dir == False:
        return 1
    while True:
        note_way = main.create_path_note_1(path_dir)
        if note_way == False:
            return 2
        check = os.path.exists(note_way)
        if check == True:
            ses_dec = sesurity.decrypt(way_key, sesurity.master_key(password))
            note = sesurity.decrypt(note_way, ses_dec)
            os.system(note)
            sesurity.encrypt(note, ses_dec)
            os.remove(ses_dec)

            return True
        elif check == False:
            back = main.back_note()
            if back == True:
                continue
            elif back == False:
                return 3


def delet_note(path_dir, acc_name):
    dir = all_notes(path_dir, acc_name)
    if dir == False:
        return 1
    while True:
        delete_way = main.create_path_note_1(path_dir)
        if delete_way == False:
            return 2
        check = os.path.exists(delete_way)
        if check == True:
            os.remove(delete_way)
            return True
        elif check == False:
            back = main.back_note()
            if back == True:
                continue
            elif back == False:
                return 3


def all_notes(path_dir, acc_name):
    dir = os.listdir(path_dir)
    dir.remove('system.conf.aes')
    dir.remove('g.conf.aes')
    for i in range(len(dir)):
        note = dir[i]
        note = note.rstrip('.txt.aes')
        dir[i] = note
    if len(dir) == 0:
        return 1
    main.list(acc_name, dir)
    return dir


def delet_all_notes(path_dir, acc_name):
    dir = all_notes(path_dir, acc_name)
    if dir == 1:
        return 2
    for i in range(len(dir)):
        dir[i] = dir[i] + '.txt.aes'
        delet_file = os.path.join(path_dir, dir[i])
        os.remove(delet_file)
    return True


if __name__ == '__main__':
    print('Это модуль')
