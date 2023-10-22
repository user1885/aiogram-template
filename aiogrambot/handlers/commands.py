from shortcuts import *


@dp.message(Command("start"))
@context(ctx=None, ctx_name="example")
async def start(message: Message, example, **kwargs):
    await message.answer("start")