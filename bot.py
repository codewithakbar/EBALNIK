import handlers
import asyncio
from aiogram import executor
from dispatcher import dp


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)  # Don't skip updates, if your bot will process payments or other important stuff
