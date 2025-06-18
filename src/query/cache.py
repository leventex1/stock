import json
from ..db import cache_db_session
from ..models import ApiCache


def get_cacheck_response(query_key: str) -> object | None:
    cached = cache_db_session.query(ApiCache).filter_by(query_key=query_key).first()
    if cached:
        print(f"Cache hit: ${query_key}")
        return json.loads(cached.response_json)
    
    return None


def save_response_to_cache(query_key: str, response_data: object) -> None:
    json_data = json.dumps(response_data)
    cached = ApiCache(query_key=query_key, response_json=json_data)
    cache_db_session.merge(cached)
    cache_db_session.commit()
    print(f"Cache saved: ${query_key}")