from ..models import StockPrice

class AnalysisService:

    """
    Finds the price points where the relative prices of
    n'th closing and (n+1)'th closing price points is between the given range.

    @param price_points: list of StockPrice, should be filtered to a given inverval
                         else it can create false calculations.

    @param percentage_range: tuple of float, the min and max relative percentages of the drop.

    @return list of tuple of StockPrices, where the drop occured between the first and
            second price point.
    """
    def find_drops(self, price_points: list[StockPrice], percentage_range: tuple[float, float], days_after: int) -> list[tuple[StockPrice]]:
        result: list[tuple[StockPrice]] = []

        for i in range(len(price_points) - 1): 
            first: StockPrice = price_points[i]
            second: StockPrice = price_points[i+1]
            relative_percentage = second.close / first.close
            if (relative_percentage >= percentage_range[0] and 
                relative_percentage <= percentage_range[1]):
                days_after_index = i+1+days_after
                days_after_price = second if days_after_index > len(price_points) else price_points[days_after_index]
                result.append((first, second, days_after_price))

        return result