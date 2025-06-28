import requests
from src.config import Config
from src.query.manager import QueryManager
from src.query.time_series import TimeSeriesParams, Interval, TwelvedataTimeSeriesConverter
from src.services.stock_service import StockService
from src.services.plot_service import PlotService
from src.services.analysis_service import AnalysisService

def main():
    query_manager = QueryManager()
    """ response = query_manager.get_stocks()
    stocks = response.get("data")

    county_map: dict = dict()
    for stock in stocks:
        try:
            county_map[stock.get("country")].append(stock)
        except:
            county_map[stock.get("country")] = []

    for (country, stocks) in county_map.items():
        print(country, len(stock))
        if country == "Hungary":
            for stock in stocks:
                print(stock.get("name")) """
    time_series_converter = TwelvedataTimeSeriesConverter()
    
    stock_service = StockService(
        query_manager=query_manager,
        time_series_converter=time_series_converter
    )
    plot_service = PlotService()
    analysis_service = AnalysisService()

    time_series_params = TimeSeriesParams(
        symbol="AAPL",
        interval=Interval.DAY,
        start_date="2020-10-01",
        end_date="2025-06-28",
    )
    stock_service.query_and_save_stock_prices(time_series_params=time_series_params)
    stock_prices = stock_service.get_time_series(symbol=time_series_params.symbol)
    for stock_price in stock_prices:
        print(stock_price)
    
    plot_service.plot_stock_prices(stock_prices)
    drop_points = analysis_service.find_drops(stock_prices, (0.1, 0.9), 7)
    flatten_drop_points = [item for tup in drop_points for item in tup]
    plot_service.plot_stock_prices(flatten_drop_points, scatter_plot=True)

    total_diff = 0
    for (start_point, drop_point, after_point) in drop_points:
        diff = after_point.close - drop_point.close
        print(f"{start_point.close}, {drop_point.close}, {after_point.close}, diff={diff}")
        total_diff += diff

    print(f"total diff={total_diff}")



if __name__ == "__main__":
    main()