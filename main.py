from aiogram import Bot, Dispatcher, executor
import asyncio

from config import TG_TOKEN

bot = Bot(token=TG_TOKEN, parse_mode="HTML")
loop = asyncio.get_event_loop()
dp = Dispatcher(bot=bot, loop=loop)


if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dispatcher=dp, skip_updates=True)
