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
                'name': 'Сергей Бухер',
                'image_id': 'AgACAgIAAxkBAANMYRQ2PiPYO7XbDpWiBCNXG7UdyWkAApq2MRtCkKFIvCdv6iG6WDwBAAMCAANzAAMgBA'
            },
            {
                'name': 'Ирина Бондарева',
                'image_id': 'AgACAgIAAxkBAANOYRQ4d0TyXTLfuE7-1mwb2EYKVzwAApy2MRtCkKFItutOgufAXgkBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 2',
        'place': 'Беседка около 1 Корпуса',
        'employees' : [
            {
                'name':'Цыцаров Денис',
                'image_id': 'AgACAgIAAxkBAANQYRQ52ff23jAHSIaIeo2bGLdTIf4AAp-2MRtCkKFIVDnjoiXvwXUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Козырькова Дина',
                'image_id': 'AgACAgIAAxkBAANSYRQ5-xolXIWxTk-nnH8EdYqxiykAAqC2MRtCkKFII7dtIiHpwTcBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 3',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Назимов Дмитрий',
                'image_id': 'AgACAgIAAxkBAANUYRQ-8AMXblJ8WbG7uQXyDbRe244AAqG2MRtCkKFIWRbq612oNYABAAMCAANzAAMgBA'
            },
            {
                'name': 'Давыдова Мария',
                'image_id': 'AgACAgIAAxkBAANWYRQ_bTppuQpF_GfAwwoHDWP_v1kAAqK2MRtCkKFIfMUscvZ9RvoBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 4',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Кушнир Артём',
                'image_id': 'AgACAgIAAxkBAANaYRRARgogQ5zaMzd01fd59i4nT0sAAqW2MRtCkKFIntSLbZERFUUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Харлина Анастасия',
                'image_id': 'AgACAgIAAxkBAANYYRQ_6qr9MEBSOXBcsCRu74CFr1kAAqO2MRtCkKFIRQHuGz2hfJsBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 5',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Старченков Кирилл',
                'image_id': 'AgACAgIAAxkBAANeYRRDeQ_PqVLdaU1CXCtVxfzNUXcAAqi2MRtCkKFIIz-a5BsZMmUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Сафонова Дарья',
                'image_id': 'AgACAgIAAxkBAANcYRRDW55yIOiptj3qcFwzU7pZCgYAAqe2MRtCkKFIDJHHd0goMNQBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 6',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Конон Артем',
                'image_id': 'AgACAgIAAxkBAANiYRRFW6jZihb0eZmyBk_AlXPCWYcAAqq2MRtCkKFI8ouuP04W3IQBAAMCAANzAAMgBA'
            },
            {
                'name': 'Филоненко Елизавета',
                'image_id': 'AgACAgIAAxkBAANgYRRFL4mLht868O6lQARMuiXVZZ0AAqm2MRtCkKFIZ3p-bHmnUycBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 7',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Ваньков Дарви',
                'image_id': 'AgACAgIAAxkBAANmYRRHyinARbby9A_qMflNRJkSuk0AAq62MRtCkKFIi0RQIbxClKcBAAMCAANzAAMgBA'
            },
            {
                'name': 'Шацкова Валерия',
                'image_id': 'AgACAgIAAxkBAANkYRRHpOdM20mUmNXv0MI6Dijg1e8AAq22MRtCkKFIEbNRi9a6mzABAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Отряд 8',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Ерохин Валера',
                'image_id': 'AgACAgIAAxkBAANqYRRJopVCod3GI0ZZMelYovqc6LUAArC2MRtCkKFIKEcR1ZYkK-MBAAMCAANzAAMgBA'
            },
            {
                'name': 'Фомина Екатерина',
                'image_id': 'AgACAgIAAxkBAANoYRRJgDA3n9olnv7-f_IS8Xf9_3YAAq-2MRtCkKFIlMjZFPmOVEgBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Медиацентр',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Черняева Екатерина',
                'image_id': 'AgACAgIAAxkBAANsYRRMMQRyh015nIGRuu7JDE9fSvwAArO2MRtCkKFIsrJQsj4ZhJIBAAMCAANzAAMgBA'
            },
            {
                'name': 'фонина Арина',
                'image_id': 'AgACAgIAAxkBAANuYRRNc7ucg6sKzoWbfIk7x461lU0AArS2MRtCkKFI9C2XXt180HgBAAMCAANzAAMgBA'
            },
            {
                'name': 'Косухина Мария',
                'image_id': 'AgACAgIAAxkBAANwYRRNlfKyGYNF8nTNmBEL6UovIX0AArW2MRtCkKFILmlj7FHyiG8BAAMCAANzAAMgBA'
            },
            {
                'name': 'Шмелева Анастасия',
                'image_id': 'AgACAgIAAxkBAANyYRRN_d-tGQfHsP3P4CiSiXHheZkAAre2MRtCkKFIKz118tNlgpoBAAMCAANzAAMgBA'
            },
            {
                'name': 'Романова Елизавета',
                'image_id': 'AgACAgIAAxkBAAN0YRROFY9PCj0qa-xknhYUWLI396IAAri2MRtCkKFIK9GMIYwipSABAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Служба \"Рассвет\"',
        'place': 'Беседка около 1 Корпуса',
        'employees': [
            {
                'name': 'Варсеев Тимофей',
                'image_id': 'AgACAgIAAxkBAAN2YRRTw1avidrA9semx1NL20hFixsAArm2MRtCkKFIOF-LNeNqScwBAAMCAANzAAMgBA'
            },
            {
                'name': 'Чучина Анастасия',
                'image_id': 'AgACAgIAAxkBAAN4YRRT6MbQX3NG-YG8KQtVhl0YNuoAArq2MRtCkKFICIlE7guA7VUBAAMCAANzAAMgBA'
            },
            {
                'name': 'Рогова Марина'
                'image_id': 'AgACAgIAAxkBAAN6YRRUC_IUV28ZPxosKWxahPUd_TIAAru2MRtCkKFIXjsveV06b9cBAAMCAANzAAMgBA'
            }
        ]
    },
    {
        'group_name': 'Тех-служба',
        'place': 'Беседка',
        'employees': [
            {
                'name': 'Толоконов Илья',
                'image_id': 'AgACAgIAAxkBAAN8YRRUzKnUoicLExCR-bnO65tFaPUAAry2MRtCkKFIS2_w7wnNYG8BAAMCAANzAAMgBA'
            },
            {
                'name': 'Конаков Павел',
                'image_id': 'AgACAgIAAxkBAAOAYRRVA959qZZWDoK7c-BSBb5vEB8AAr62MRtCkKFIH5SF6UXnnzkBAAMCAANzAAMgBA'
            },
            {
                'name': 'Близнов Матвей',
                'image_id': 'AgACAgIAAxkBAAOCYRRVHhX0jZL0N2tqFIWtX9-UdxUAAr-2MRtCkKFIn0_BbgFkiu4BAAMCAANzAAMgBA'
            },
            {
                'name': 'Рюмин Кирилл',
                'image_id': 'AgACAgIAAxkBAAN-YRRU6E8GzyzIBbp_UWsfI2myBkoAAr22MRtCkKFINmOYydRtsDMBAAMCAANzAAMgBA'
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
