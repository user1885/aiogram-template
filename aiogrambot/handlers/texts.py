from shortcuts import *


@dp.message(F.text)
@context(ctx=None, ctx_name="ctx")
async def unbound(message: Message, ctx, **kwargs):
    await message.answer("unbound")