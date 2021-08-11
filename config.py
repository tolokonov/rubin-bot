import os

TG_TOKEN = os.getenv("TG_TOKEN")

button_text_calendar = "Календарь смены"
button_text_songs = "Песенник"
button_text_employees = "Комиссары смены"

# Cписок сотрудников лагеря по отрядам и службы
# Тут нужно проработать для каждого отряда Фамилия и Имя комиссаров и id_photo для каждого из них (фотки взять из их вк)
employees_list = [
    {
        'group_name': 'Отряд 1',
        'place': 'Беседка около 1 Корпуса',
        'employees' : [
            {
                'name': 'кушнир',
                'image_id': 'AgACAgIAAxkBAANEYRPz8BCLZnOndo3zBuNfnyh8EIYAAvm4MRsv3phI63Qe_oNd4b4BAAMCAANzAAMgBA'
            },
            {
                'name': 'дина',
                'image_id': 'AgACAgIAAxkBAANEYRPz8BCLZnOndo3zBuNfnyh8EIYAAvm4MRsv3phI63Qe_oNd4b4BAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 2',
        'place': 'Беседка около 1 Корпуса',
        'employees' : [
            {
                'name':'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Отряд 3',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Отряд 4',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Отряд 5',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Отряд 6',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Отряд 7',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Отряд 8',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Медиацентр',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
    {
        'group_name': 'Служба \"Рассвет\"',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'кушнир',
                'image_id': 'sss.sss.com'
            },
            {
                'name': 'дина',
                'image_id': ''
            }
        ]
    },
]

# Здесь должен быть id фотки с календарём (прокидываешь через бота фотку и пишешь id сюда
CALENDAR_FILE_ID = 'https://www.typecalendar.com/wp-content/uploads/2020/02/June-2021-Calendar.jpg'


# Здесь у нас словарь с file_id текстовых файлов песен
song_file_ids = {
    '00': 'asdasdasd',
    '01': 'asdasdasd',
}

song_names = [
    [
        "Гимн Российской Федерации",
        "Гимн Рубина",
        "Парфюмер",
        "За Рубин горой",
        "Юбилейная песня",
        "У всех Рубиновцев память особая"
    ],
    [
        "Надежда",
        "Алые паруса",
        "Вахтеры",
        "Рыжая",
        "Серебро",
        "Мой рок-н-ролл"
    ]
]