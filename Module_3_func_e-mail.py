def send_email (message, recipient, *, sender='university.help@gmai.com'):
    if '@' not in recipient or '@' not in sender:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient} | Отсутствует символ "@"')
    elif (sender.endswith('.com') or sender.endswith('.net') or sender.endswith('.ru')) == False:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient}')
    elif (recipient.endswith('.com') or recipient.endswith('.net') or recipient.endswith('.ru')) == False:
        print(f'Невозможно отправить письмо с адреса: {sender} на адрес: {recipient} | ошибка окончания ".com.ru.net"')
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmai.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

send_email('Проверка связи', 'ivanov@gmail.ru')  # успешно отправлено
send_email('Проверка связи', 'smirnov@gmail.ru', sender='petrov@gmail.ru')  # нестандартный отправитель
send_email('Проверка связи', 'pupkin.gmail.net')  # невозможно -  нет @
send_email('Проверка связи', 'pupkin@gmail.co')   # невозможно - .co
send_email('Проверка связи', 'pupkin@gmail.r')    # невозможно - .r
send_email('Проверка связи', 'university.help@gmai.com')  # нельзя самому себе

