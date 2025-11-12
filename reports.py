# report.py
import json, string

# Данные мероприятия
data = {
    'name_head': 'Александр Викторович',
    'city_event': 'Москва',
    'date_event': '15.03.2021',
    'name_event': '«Развитие бизнеса с помощью информационных технологий»',
    'address_event': 'Рождественский бульвар, 28',
    'firms': ['ООО «Innovation»', 'ООО «Science»', 'ООО «InternationalData»']
    }

# Преобразуем список компаний участников в строку
data['firms'] = ', '.join(data['firms'])

# Загружаем шаблон
with open('mail-invitation.tpl') as tpl:
    temp = tpl.read()

template = string.Template(temp)

# Загружаем данные участников 
with open('data.json') as fp:
    members = json.load(fp)

# Проходим по участникам и генерируем 
# письма, которые выведем в терминал
for member in members:
    # Добавим к данным мероприятия 
    # имя участника из .json файла
    data['name_member'] = member['name']
    # получаем готовое письмо
    output = template.substitute(data)
    print('-'*30)
    # Почта, на которую отправляем письмо
    print('Почта:', member['email'])
    # готовое письмо к отправке
    print(output)