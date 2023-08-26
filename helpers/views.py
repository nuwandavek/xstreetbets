from aiohttp import web
from jinja2 import Environment, FileSystemLoader
from helpers.db import User, Market, Prediction, Payout, Session


EMOJIS = ["🐙", "🐘", "🐢", "🐬", "🐯"]
env = Environment(loader=FileSystemLoader('templates'))


async def index(request):
  template = env.get_template('index.html')
  return web.Response(text=template.render(), content_type='text/html')


async def users(request):
  template = env.get_template('users.html')
  all_users = []
  with Session() as session:
    users = session.query(User).all()
    for user in users:
      temp = user.__dict__
      temp['emoji'] = EMOJIS[user.id % 5]
      all_users.append(temp)
  return web.Response(text=template.render(users=users), content_type='text/html')


async def markets(request):
  template = env.get_template('markets.html')
  all_markets = []
  with Session() as session:
    markets = session.query(Market).all()
    for market in markets:
      temp = market.__dict__
      temp['creator'] = market.creator.__dict__
      temp['creator']['emoji'] = EMOJIS[temp['creator']['id'] % 5]
      all_markets.append(temp)
  return web.Response(text=template.render(markets=markets), content_type='text/html')


async def predictions(request):
  template = env.get_template('predictions.html')
  predictions = []
  return web.Response(text=template.render(predictions=predictions), content_type='text/html')


async def payouts(request):
  template = env.get_template('payouts.html')
  payouts = []
  return web.Response(text=template.render(payouts=payouts), content_type='text/html')


async def error_404(request):
  template = env.get_template('404.html')
  return web.Response(text=template.render(), content_type='text/html')
