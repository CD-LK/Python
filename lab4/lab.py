import main
import notes

while True:
    select = input("Главное меню:\n"
                   "\t1) Аутентификация аккаунта.\n"
                   "\t2) Создание аккаунта.\n"
                   "\t3) Удаление аккаунта.\n"
                   "\t4) Выход из программы.\n"
                   "\t>> ")
    if select == '1':

        try:
            aut = main.autacc()
        except Exception:
            print("=====Неверны ввод пароля=====")
            continue

        if aut == False:
            continue
        else:
            path_dir, password, acc_name, way_key = aut
            while True:
                select_note = input("Меню заметок:\n"
                                    "\t1) Создать пустую заметку.\n"
                                    "\t2) Редактировать заметку.\n"
                                    "\t3) Удалить заметку.\n"
                                    "\t4) Удалить все заметки.\n"
                                    "\t5) Список существующих заметок.\n"
                                    "\t6) Возврат в главное меню.\n"
                                    "\t>> ")
                if select_note == '1':
                    notes.create_note(path_dir, way_key, password)
                    continue
                elif select_note == '2':
                    notes.edit_note(path_dir, way_key, password, acc_name)
                    continue
                elif select_note == '3':
                    notes.delet_note(path_dir, acc_name)
                elif select_note == '4':
                    notes.delet_all_notes(path_dir, acc_name)
                    continue
                elif select_note == '5':
                    notes.all_notes(path_dir, acc_name)
                    continue
                elif select_note == '6':
                    print("=====Возврат в главное меню=====")
                    break
                elif select_note != '1' and select_note != '2' and select_note != '3' and select_note != '4' and select_note != "5" and select_note != '6':
                    print("=====Неверный ввод. Попробуйте сново=====")
                    continue
                else:
                    print("=====Error=====\n")
                    exit()
    elif select == '2':
        main.creatacc()
        continue
    elif select == '3':
        main.deletacc()
        continue
    elif select == '4':
        print("=====Завершение работы программы=====")
        break
    elif select != '1' and select != '2' and select != '3' and select != '4':
        print("=====Неверный ввод. Попробуйте сново=====")
        continue
    else:
        print("=====Error=====\n")
        exit()
