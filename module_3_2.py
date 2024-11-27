
def send_email(message,*, recipient ='urban.teacher@mail.com', sender = 'university.help@gmail.com' ):

    if(sender==recipient):
        print('Нельзя отправить письмо самому себе!')

    elif(sender=='university.help@gmail.com'):
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')

    elif(sender=='an.nabogdanova@yandex.ru'):
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')

    elif('@','.com' not in recipient or '@', '.com' not in sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')


send_email('Нельзя отправить письмо самому себе!', recipient='university.help@gmail.com')
send_email('Письмо успешно отправлено с адреса {sender>} на адрес {recipient}.')
send_email('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.', sender='an.nabogdanova@yandex.ru')
send_email('Невозможно отправить письмо с адреса {sender} на адрес {recipient}', sender='vasyok1337@gmail.com')

