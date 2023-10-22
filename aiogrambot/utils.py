from contextlib import nullcontext


def with_context(func, ctx, ctx_args, ctx_name):
    if ctx is None:
        ctx = nullcontext
    async def wrapper(*args, **kwargs):
        with ctx(*ctx_args) as ctx_:
            kwargs[ctx_name] = ctx_
            result = await func(*args, **kwargs)
            return result
    return wrapper

def context(ctx=None, ctx_args=(), ctx_name="ctx"):
    def wrapper(func):
        wrapped = with_context(func, ctx, ctx_args, ctx_name)
        return wrapped
    return wrapper