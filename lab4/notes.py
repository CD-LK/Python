import os
import sesurity
import main
from typing import Tuple

note_format_1 = '.txt.aes'
note_format_2 = '.txt'


def create_note(path_dir: str, way_key: str, password: str) -> int:
    flag = 0
    while True:
        note_way, test = main.create_path_note_2(path_dir)
        if test == False:
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
            return 0


def edit_note(path_dir: str, way_key: str, password: str, acc_name: str) -> int:
    dir, test_1 = all_notes(path_dir, acc_name)
    if test_1 == False:
        return 1
    while True:
        note_way, test = main.create_path_note_1(path_dir)
        if test == False:
            return 2
        check = os.path.exists(note_way)
        if test == True:
            ses_dec = sesurity.decrypt(way_key, sesurity.master_key(password))
            note = sesurity.decrypt(note_way, ses_dec)

            os.system(note)
            sesurity.encrypt(note, ses_dec)
            os.remove(ses_dec)
            return 0
        elif check == False:
            back = main.back_note()
            if back == True:
                continue
            elif back == False:
                return 3


def delet_note(path_dir: str, acc_name: str) -> int:
    dir, test = all_notes(path_dir, acc_name)
    if test == False:
        return 1
    while True:
        delete_way, test = main.create_path_note_1(path_dir)
        if test == False:
            return 2
        check = os.path.exists(delete_way)
        if check == True:
            os.remove(delete_way)
            return 0
        elif check == False:
            back = main.back_note()
            if back == True:
                continue
            elif back == False:
                return 3


def all_notes(path_dir: str, acc_name: str) -> Tuple[str, bool]:
    dir = os.listdir(path_dir)
    dir.remove('system.conf.aes')
    dir.remove('g.conf.aes')
    final_dir = str('str')
    for i in range(len(dir)):
        note = dir[i]
        note = note.rstrip('.txt.aes')
        dir[i] = note
    if len(dir) == 0:
        return final_dir, False
    final_dir = str(dir)
    main.list_dir(acc_name, final_dir)
    return final_dir, True


def delet_all_notes(path_dir: str, acc_name: str) -> int:
    dir = os.listdir(path_dir)
    dir.remove('system.conf.aes')
    dir.remove('g.conf.aes')
    for i in range(len(dir)):
        note = dir[i]
        note = note.rstrip('.txt.aes')
        dir[i] = note
    if len(dir) == 0:
        return False
    for i in range(len(dir)):
        dir[i] = dir[i] + '.txt.aes'
        delet_file = os.path.join(path_dir, dir[i])
        os.remove(delet_file)
    return 0


if __name__ == '__main__':
    print('Это модуль')
