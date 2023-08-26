from aiohttp import web
from helpers.db import init_tables
from helpers.views import index, users, markets, predictions, payouts, error_404


async def xsb():
  await init_tables()
  app = web.Application()
  app.router.add_static('/static/', path='static', name='static')
  app.router.add_get('/', index)
  app.router.add_get('/users', users)
  app.router.add_get('/markets', markets)
  app.router.add_get('/predictions', predictions)
  app.router.add_get('/payouts', payouts)
  app.router.add_route('*', '/{path_info:.*}', error_404)
  return app

if __name__ == "__main__":
  app = xsb()
  web.run_app(app, host="0.0.0.0", port=5000)
