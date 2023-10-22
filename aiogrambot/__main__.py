from app import dp, bot
import handlers
import asyncio


if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))