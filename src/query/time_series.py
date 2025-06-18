from datetime import datetime
from typing import Optional
from .api import APIParams
from ..models import StockPrice
from abc import ABC, abstractmethod

class Interval:
    MIN_1="1min"
    MIN_5="5min"
    MIN_15="15min"
    MIN_30="30min"
    MIN_45="45min"
    HOUR_1="1h"
    HOUR_2="2h"
    HOUR_4="4h"
    HOUR_5="5h"
    DAY="1day"
    WEEK="1week"
    MONTH="1month"

class TimeSeriesParams(APIParams):
    symbol: str
    interval: str
    outputsize: int
    date: datetime
    start_date: datetime
    end_date: datetime

    def __init__(self, 
                 symbol: str, 
                 interval: str,
                 outputsize: int = 30,
                 date: Optional[datetime] = None,
                 start_date: Optional[datetime] = None,
                 end_date: Optional[datetime] = None
                 ):
        self.symbol = symbol
        self.interval = interval
        self.outputsize = outputsize
        self.date = date
        self.start_date = start_date
        self.end_date = end_date

class TimeSeriesConverter(ABC):

    @abstractmethod
    def convert(self, data: dict) -> list[StockPrice]:
        pass

class TwelvedataTimeSeriesConverter(TimeSeriesConverter):

    def convert(self, data) -> list[StockPrice]:
        result: list[StockPrice] = []
        symbol = data.get("meta").get("symbol")
        datetime.strptime
        for value in data.get("values"):
            result.append(
                StockPrice(
                    symbol=symbol,
                    datetime=datetime.strptime(value.get("datetime"), "%Y-%m-%d %H:%M:%S"),
                    open=float(value.get("open")),
                    high=float(value.get("high")),
                    low=float(value.get("low")),
                    close=float(value.get("close")),
                    volume=int(value.get("volume"))
                )
            )
        return result