from sqlalchemy import Column, String, Float, Integer, DateTime, Text, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()
CacheBase = declarative_base()

class BaseModel:

    def __str__(self):
        params = {
            k: v for k, v in vars(self).items()
            if (v is not None and k != "_sa_instance_state")
        }
        res = ""
        for i, (key, value) in enumerate(params.items()):
            res += ("" if i == 0 else ", ") + f"{key}={value}"
        return res

class StockPrice(Base, BaseModel):
    __tablename__ = "stock_prices"
    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String, nullable=False)
    datetime = Column(DateTime, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("symbol", "datetime", name="uix_symbol_date"),
    )

class ApiCache(CacheBase):
    __tablename__ = "api_cache"
    query_key = Column(String, primary_key=True)
    response_json = Column(Text)
    timestamp = Column(DateTime, default=datetime.now)