from datetime import datetime
from src.query.manager import QueryManager
from src.query.time_series import TimeSeriesParams, Interval, TwelvedataTimeSeriesConverter
from src.services.stock_service import StockService

def main():
    query_manager = QueryManager()
    time_series_converter = TwelvedataTimeSeriesConverter()
    
    stock_service = StockService(
        query_manager=query_manager,
        time_series_converter=time_series_converter
    )
    time_series_params = TimeSeriesParams(
        symbol="AAPL", 
        interval=Interval.MIN_1,
    )
    stock_service.query_and_save_stock_prices(time_series_params=time_series_params)
    stock_prices = stock_service.get_time_series(symbol="AAPL")
    for stock_price in stock_prices:
        print(stock_price)
    

if __name__ == "__main__":
    main()