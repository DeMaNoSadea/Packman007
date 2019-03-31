import random
from aiohttp import web

async def lst(x):
    return web.Response(text=str([random.randint(0, 99) for i in range(10)]))

async def dic(z):
    k = [str(i) for i in range(1, random.randrange(1, 20))]
    v1 = [hash(i) for i in k]
    v = [hex(i) for i in v1]
    d = dict(zip(k, v))
    return web.Response(text=str(d))

app = web.Application()
app.add_routes([web.get('/second', dic), web.get('/first', lst)])
web.run_app(app)
