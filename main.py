from random import randint





def check_user_and_pin(user):

    pin = str(randint(1000, 9999))
    t = 1
    print(pin)
    while t < 4:
        pin_answer = str(input('Введите пин для входа >>> '))
        if len(pin_answer) !=4 or pin_answer:
            print("Введите 4 цифры")
        if pin_answer != pin:
            t += 1
            print(f"Неверный пин.Осталось {4 - t} попыток")


        elif pin_answer == pin:
            print("Выполнен вход в систему")
            break
        if t == 4:
            print("Вы ввели 3 неверных пина. Вход заблокирован на 5 минут")

check_user_and_pin("Mihail")