from datetime import datetime
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Enum as SQLEnum
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey


class Status(Enum):
  OPEN = 'open'
  RESOLVED = 'resolved'
  CANCELLED = 'cancelled'


class Bet(Enum):
  FOR = 'for'
  AGAINST = 'against'


Base = declarative_base()


class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True, autoincrement=True)
  username = Column(String, unique=True)
  description = Column(String)
  password_hash = Column(String)
  balance = Column(Float)
  create_time = Column(DateTime, default=datetime.utcnow, index=True)
  update_time = Column(DateTime, default=datetime.utcnow, index=True)
  markets = relationship('Market', backref='creator')
  predictions = relationship('Prediction', backref='user')
  payouts = relationship('Payout', backref='user')


class Market(Base):
  __tablename__ = 'market'
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String)
  description = Column(String)
  status = Column(SQLEnum(Status), default=Status.OPEN)
  creator_id = Column(Integer, ForeignKey('user.id'))
  for_stock = Column(Float, default=0)
  against_stock = Column(Float, default=0)
  probability = Column(Float, default=0.5)
  create_time = Column(DateTime, default=datetime.utcnow, index=True)
  update_time = Column(DateTime, default=datetime.utcnow, index=True)
  predictions = relationship('Prediction', backref='market')
  payouts = relationship('Payout', backref='market')


class Prediction(Base):
  __tablename__ = 'prediction'
  id = Column(Integer, primary_key=True, autoincrement=True)
  market_id = Column(Integer, ForeignKey('market.id'))
  user_id = Column(Integer, ForeignKey('user.id'))
  bet = Column(SQLEnum(Bet))
  amount = Column(Float)
  create_time = Column(DateTime, default=datetime.utcnow, index=True)
  payouts = relationship('Payout', backref='prediction')


class Payout(Base):
  __tablename__ = 'payout'
  id = Column(Integer, primary_key=True, autoincrement=True)
  market_id = Column(Integer, ForeignKey('market.id'))
  prediction_id = Column(Integer, ForeignKey('prediction.id'))
  user_id = Column(Integer, ForeignKey('user.id'))
  amount = Column(Float)
  create_time = Column(DateTime, default=datetime.utcnow, index=True)


async def init_tables():
  engine = create_engine('sqlite:////xsb/data/bets.db')
  Base.metadata.create_all(engine)


def Session():
  engine = create_engine('sqlite:////xsb/data/bets.db')
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  return SessionLocal()


async def add_user(username, description, password_hash, balance):
  with Session() as session:
    user = session.query(User).filter(User.username == username).first()
    if user is None:
      user = User(username=username, description=description, password_hash=password_hash, balance=balance)
      session.add(user)
      session.commit()
      print(f'Added User {username}')
    else:
      print(f'User {username} already exists')
    return user


async def add_market(title, description, creator):
  with Session() as session:
    user = session.query(User).filter(User.username == creator).first()
    if user is None:
      print(f'User {creator} does not exist')
      return
    market = Market(title=title, description=description, creator=user)
    session.add(market)
    session.commit()
    print(f'Added Market {title}')
    return market
