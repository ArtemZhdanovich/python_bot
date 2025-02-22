from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine
from app.src.configs import PostgresConfig


def new_session_maker(psql_config: PostgresConfig) -> sessionmaker[Session]:
    database_uri = "postgresql+psycopg://{login}:{password}@{host}:{port}/{database}".format(
        login=psql_config.login,
        password=psql_config.password,
        host=psql_config.host,
        port=psql_config.port,
        database=psql_config.database,
    )

    engine = create_engine(
        database_uri,
        pool_size=15,
        max_overflow=15,
        connect_args={
            "connect_timeout": 5,
        },
    )
    return sessionmaker(engine, class_=Session, autoflush=False, expire_on_commit=False)