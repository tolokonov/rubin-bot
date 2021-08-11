from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
     CallbackQuery
from aiogram.types.input_media import InputMediaPhoto
from aiogram.dispatcher.filters import Text


from main import dp, bot
import config


MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=config.button_text_calendar),
            KeyboardButton(text=config.button_text_songs),
            KeyboardButton(text=config.button_text_employees)
        ],
    ]
)

#Чтобы получить клавиатурку, нужен /start
@dp.message_handler(commands=['start'])
async def start_menu(msg: Message):
    await bot.send_message(
        chat_id=msg.from_user.id,
        text="Привет! Это телеграм-бот лагеря \"Рубин-55\", в котором ты сможешь найти некоторую информацию о лагере.\n"
             "Выбери раздел меню на интерактивной клавиатуре, чтобы пойти дальше.",
        reply_markup=MAIN_MENU
    )


@dp.message_handler(Text(equals=config.button_text_calendar))
async def show_calendar(msg: Message):
    await bot.send_photo(
        chat_id=msg.from_user.id,
        photo=config.CALENDAR_FILE_ID,
        caption="<b>Календарь нашей смены</b> \n"
                "Здесь отображены ключевые мероприятия нашей смены. \n"
                "Будь всегда в курсе событий :)",
    )


@dp.message_handler(Text(equals=config.button_text_employees))
async def employees(msg: Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Отряд 1", callback_data="empl@1"),
        InlineKeyboardButton("Отряд 2", callback_data="empl@2"),
        InlineKeyboardButton("Отряд 3", callback_data="empl@3"),
        InlineKeyboardButton("Отряд 4", callback_data="empl@4"),
        InlineKeyboardButton("Отряд 5", callback_data="empl@5"),
        InlineKeyboardButton("Отряд 6", callback_data="empl@6"),
        InlineKeyboardButton("Отряд 7", callback_data="empl@7"),
        InlineKeyboardButton("Отряд 8", callback_data="empl@8"),
        InlineKeyboardButton("Медиацентр", callback_data="empl@9"),
        InlineKeyboardButton("Служба \"Рассвет\"", callback_data="empl@10")
    )
    await bot.send_message(
        chat_id=msg.from_user.id,
        text="Выберите раздел: ",
        reply_markup=markup
    )


@dp.message_handler(Text(equals=config.button_text_songs))
async def songs_menu(msg: Message):
    markup = InlineKeyboardMarkup()
    songs_page = config.song_names[0]
    for index, song_name in enumerate(songs_page):
        markup.add(InlineKeyboardButton(song_name, callback_data=f"song@0@{index}"))

    markup.row(
        InlineKeyboardButton('◀️', callback_data="page@-1"),
        InlineKeyboardButton('▶️', callback_data="page@1")
    )
    await bot.send_message(
        chat_id=msg.from_user.id,
        text="Здесь вы можете ознакомиться с важными песнями для нашего лагеря."
             " Некоторые из них были написаны нашими рубиновцами. \n<b>Страница 1</b>",
        reply_markup=markup
    )


@dp.callback_query_handler(lambda call: call.data.split('@')[0] == 'page')
async def show_page(call: CallbackQuery):
    page_number = int(call.data.split('@')[1])
    if 0 <= page_number < len(config.song_names):
        songs_page = config.song_names[page_number]
        markup = InlineKeyboardMarkup()

        # Песни разделены по страницам, по 6 штук на страницу
        for index, song_name in enumerate(songs_page):
            markup.add(InlineKeyboardButton(song_name, callback_data=f"song@{page_number}@{index}"))

        markup.row(
            InlineKeyboardButton('◀️', callback_data=f"page@{page_number-1}"),
            InlineKeyboardButton('▶️', callback_data=f"page@{page_number+1}")
        )

        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=f"Здесь вы можете ознакомиться с важными песнями для нашего лагеря. "
                 f"Некоторые из них были написаны нашими рубиновцами. "
                 f"\n<b>Страница {page_number + 1}</b>",
            reply_markup=markup
        )


@dp.callback_query_handler(lambda call: call.data.split('@')[0] == 'song')
async def show_song(call: CallbackQuery):
    page_number, song_number = map(int, call.data.split('@')[1:])
    song_name = config.song_names[page_number][song_number]

    file = await bot.download_file_by_id(config.song_file_ids[f'{page_number}{song_number}'])
    text = file.getvalue().decode('UTF-8')
    file.close()

    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=f"Текст песни <b>\"{song_name}\"</b> : \n\n" + text,
        reply_markup=None
    )


@dp.callback_query_handler(lambda call: call.data.split('@')[0] == 'empl')
async def show_employee(call: CallbackQuery):
    empl_id = int(call.data.split("@")[1])
    empl_data = config.employees_list[empl_id - 1]
    formated_text = f"<b>{empl_data['group_name']}</b>\n" \
                    f"Место положение: <b>{empl_data['place']}</b>\n" \
                    f"Коммиссары: \n"

    media = []
    for empl in empl_data['employees']:
        formated_text += f"- {empl['name']} \n"
        media.append(InputMediaPhoto(empl["image_id"], caption=empl['name']))

    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=formated_text
    )

    await bot.send_media_group(
        chat_id=call.from_user.id,
        media=media
    )


# Вспомогательная штука для необходимых в боте файлов (загружать фотки именно фотками, не документом)
@dp.message_handler(content_types=['document', 'video', 'photo'])
async def print_file_id(message: Message):
    document_id = message.document.file_id if message.document else None
    photo_id = message.photo[0].file_id if message.photo else None
    video_id = message.video[0].file_id if message.video else None

    await bot.send_message(
        chat_id=message.from_user.id,
        text=repr([document_id, photo_id, video_id])
    )

