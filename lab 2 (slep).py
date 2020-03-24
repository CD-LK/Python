print("Программа по проверки конфигурационного файла приложения.")
name_config = input("Введите название конфигурационного файла, или путь к оному: ")
flag = True
while flag:
    key = input("Введите имя параметра: ")
    with open(name_config, "r") as file:
        for line in file:
            if key in line and line[0] != "#" and line[0] != ";" and line[0] != '\n':
                data = line.split()
                if key == data[0]:
                    print("Количество значений параметра " + str(key) + " - " + str(len(data) - 1))
                    if len(data) == 2:
                        for i in range(1, len(data)):
                            print(data[i])
                        break
                    elif len(data) > 2:
                        num = int(input("Сколько значений параметра вы хотите посмотреть? - "))
                        if num < len(data):
                            for i in range(1, num + 1):
                                print(data[i])
                        elif num >= len(data):
                            print("***ERORE***\nК-во значений на вывод больше чем самих значений.")
                            break
                    elif len(data) < 2:
                        print("Значений не обнаруженно.")
                        break
                    else:
                        print("Alarm!\nНеизвесная ошибка!\nЭкстренный выход из программы.")
                        exit()
                    break
                elif key != data[0]:
                    print("Параметра не обнаружено.\nЗаканчиваю цикл программы.")
                    break
                else:
                    print("Alarm!\nНеизвесная ошибка!\nЭкстренный выход из программы.")
                    exit()
            else:
                print("Параметра не обнаружено.\nЗаканчиваю цикл программы.")
                break

    for i in range(5):
        command = (input("Хотите повторить программу?(Y/N)"))
        if command == "Y":
            break
        elif command == "N":
            print("Осуществляю выход из програмы")
            flag = False
            break
        else:
            print("Неверный ввод")
        if i == 4:
            print("Слишком много ошибок!\nGet out!")
            flag = False
            break
