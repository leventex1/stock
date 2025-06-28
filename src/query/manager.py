import requests
from .cache import get_cacheck_response, save_response_to_cache
from src.query import QueryBuilder
from .time_series import TimeSeriesParams
from ..config import Config

class QueryManager:

    def get_stocks(self) -> dict | None:
        endpoint = Config.BASE_API + "/stocks"
        query_builder = QueryBuilder(endpoint)
        query = query_builder.build()

        cached = get_cacheck_response(query_key=query)
        if cached:
            return cached
        
        resopnse = requests.get(query)
        if resopnse.status_code != 200:
            print(f"API request to {query} failed with status code {resopnse.status_code} | {resopnse.text}")
            return None

        data: dict = resopnse.json()

        if data.get("status") == "error":
            print(f"API request to {query} has error with code {data.get("code")} | {data.get("message")}")
            return None
        
        save_response_to_cache(query_key=query, response_data=data)
        return data

    def get_time_series(self, time_series_params: TimeSeriesParams) -> dict | None:
        endpoint = Config.BASE_API + "/time_series"
        query_builder = QueryBuilder(endpoint)
        query = query_builder.build_from(time_series_params)

        cached = get_cacheck_response(query_key=query)
        if cached:
            return cached
        
        resopnse = requests.get(query)
        if resopnse.status_code != 200:
            print(f"API request to {query} failed with status code {resopnse.status_code} | {resopnse.text}")
            return None

        data: dict = resopnse.json()

        if data.get("status") == "error":
            print(f"API request to {query} has error with code {data.get("code")} | {data.get("message")}")
            return None

        save_response_to_cache(query_key=query, response_data=data)
        return data