from datetime import datetime
from src.query.manager import QueryManager
from src.query.time_series import TimeSeriesParams, Interval, TwelvedataTimeSeriesConverter
from src.services.stock_service import StockService
from src.services.plot_service import PlotService
from src.services.analysis_service import AnalysisService

def main():
    query_manager = QueryManager()
    time_series_converter = TwelvedataTimeSeriesConverter()
    
    stock_service = StockService(
        query_manager=query_manager,
        time_series_converter=time_series_converter
    )
    plot_service = PlotService()
    analysis_service = AnalysisService()

    time_series_params = TimeSeriesParams(
        symbol="TSLA", 
        interval=Interval.DAY,
        start_date="2019-10-01",
        end_date="2025-06-19",
    )
    stock_service.query_and_save_stock_prices(time_series_params=time_series_params)
    stock_prices = stock_service.get_time_series(symbol="TSLA")
    for stock_price in stock_prices:
        print(stock_price)

    plot_service.plot_stock_prices(stock_prices)
    drop_points = analysis_service.find_drops(stock_prices, (0.8, 0.9))
    flatten_drop_points = [item for tup in drop_points for item in tup]
    print(flatten_drop_points)
    plot_service.plot_stock_prices(flatten_drop_points)



if __name__ == "__main__":
    main()