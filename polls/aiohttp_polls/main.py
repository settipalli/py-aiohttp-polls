from aiohttp import web
from routes import setup_routes
from db import init_pg, close_pg
from utils import load_config
import pathlib

app = web.Application()
setup_routes(app)

conf = load_config(str(pathlib.Path('..') / 'config' / 'polls.yaml'))
app['config'] = conf

app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app, host='127.0.0.1', port=8080)
