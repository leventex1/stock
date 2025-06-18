from ..query.manager import QueryManager
from ..query.time_series import TimeSeriesConverter, TimeSeriesParams
from ..models import StockPrice
from ..db import main_db_session

class StockService:

    def __init__(self, 
                 query_manager: QueryManager,
                 time_series_converter: TimeSeriesConverter
                ):
        self.query_manager = query_manager
        self.time_series_converter = time_series_converter

    def query_and_save_stock_prices(self, time_series_params: TimeSeriesParams) -> list[StockPrice]:
        response = self.query_manager.get_time_series(time_series_params=time_series_params)
        stock_prices = self.time_series_converter.convert(response)
        print(f"Queried {len(stock_prices)} stock prices")
        for stock_price in stock_prices:
            main_db_session.merge(stock_price)
        main_db_session.commit()

        return stock_prices
    
    def get_time_series(self, symbol: str) -> list[StockPrice]:
        stock_prices = (main_db_session
                        .query(StockPrice)
                        .filter(StockPrice.symbol == symbol)
                        .all())
        
        return stock_prices