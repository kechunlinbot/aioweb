#@author kechunlin
import logging
logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',status='200',reason='OK',headers={'Content-Type':'text/html'})

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = await loop.create_server(app.make_handler(),'','8000')
    logging.info('server started at ...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()