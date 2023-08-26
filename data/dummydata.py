import asyncio
from helpers.db import add_user, add_market

users = [
  {
    "username": "user1",
    "description": "user1",
    "balance": 1000.0,
    "password_hash": "user1",
  },
  {
    "username": "user2",
    "description": "user2",
    "balance": 1000.0,
    "password_hash": "user2",
  }
]

markets = [
  {
    "title": "Will we have AGI by 2025?",
    "description": "AGI can do everything better than humans",
    "creator": "user1",
  },
  {
    "title": "Will we have self driving cars by 2025?",
    "description": "Deployed in all cities",
    "creator": "user1",
  },
  {
    "title": "Will we Foom by 2030?",
    "description": "Also, Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.",
    "creator": "user2",
  }
]


async def main():
  for user in users:
    await add_user(**user)

  for market in markets:
    await add_market(**market)


if __name__ == "__main__":
  asyncio.run(main())
