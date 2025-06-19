import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf
import pandas as pd
from ..models import StockPrice

class PlotService:

    def plot_stock_prices(self, prices: list[StockPrice]) -> None:
        prices = sorted(prices, key=lambda p: p.datetime)

        dates = [p.datetime for p in prices]
        opens = [p.open for p in prices]
        highs = [p.high for p in prices]
        lows = [p.low for p in prices]
        closes = [p.close for p in prices]

        plt.figure(figsize=(12, 6))

        plt.plot(dates, opens, label="Open", marker="o")
        plt.plot(dates, highs, label="High", marker="^")
        plt.plot(dates, lows, label="Low", marker="v")
        plt.plot(dates, closes, label="Close", marker="s")

        plt.xlabel("Date")
        plt.ylabel("Strock Price")
        plt.title(f"({prices[0].symbol}) Stock Prices Over Time")
        plt.legend()
        
        # Format the x-axis to show date labels
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))
        plt.gcf().autofmt_xdate()  # Rotate date labels automatically

        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plot_candlestick(self, stock_prices: list):
        # Convert list of StockPrice to DataFrame
        df = pd.DataFrame([{
            "Date": p.datetime,
            "Open": p.open,
            "High": p.high,
            "Low": p.low,
            "Close": p.close,
            "Volume": p.volume
        } for p in stock_prices])

        df.set_index("Date", inplace=True)
        df.sort_index(inplace=True)

        mpf.plot(
            df,
            type='candle',
            style='yahoo',
            title=f"Candlestick Chart: {stock_prices[0].symbol if stock_prices else ''}",
            ylabel="Price",
            ylabel_lower="Volume",
            volume=True,
            tight_layout=True
        )