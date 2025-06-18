from .config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

main_db_engine = create_engine(Config.DB_MAIN_URI)
MainDBSession = sessionmaker(bind=main_db_engine)
main_db_session = MainDBSession()

cache_db_engine = create_engine(Config.DB_CACHE_URI)
CacheDBSession = sessionmaker(bind=cache_db_engine)
cache_db_session = CacheDBSession()

from .models import Base, CacheBase
Base.metadata.create_all(main_db_engine)
CacheBase.metadata.create_all(cache_db_engine)