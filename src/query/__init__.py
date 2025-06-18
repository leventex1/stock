from ..config import Config
from .api import APIParams

class QueryBuilder:

    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.__query_params: list[tuple[str, str]] = [("apikey", Config.API_KEY)]

    def add_query_param(self, key: str, value: str) -> "QueryBuilder":
        self.__query_params.append((key, value))
        return self
    
    def build(self) -> str:
        query = self.endpoint
        for (i, (key, value)) in enumerate(self.__query_params):
            query += ("?" if i == 0 else "&")
            query += key + "=" + value
        return query
    
    def build_from(self, api_builder: APIParams) -> str:
        for (key, value) in api_builder.to_dict().items():
            self.add_query_param(key, str(value))
        return self.build()
