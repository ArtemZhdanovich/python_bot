from os import environ as env

from pydantic import BaseModel, Field


class BotConfig(BaseModel):
    token: str = Field(alias="API_TOKEN")
    

class PostgresConfig(BaseModel):   
    host: str = Field(alias='POSTGRES_HOST')
    port: int = Field(alias='POSTGRES_PORT')
    login: str = Field(alias='POSTGRES_USER')
    password: str = Field(alias='POSTGRES_PASSWORD')
    database: str = Field(alias='POSTGRES_DB')


class RedisConfig(BaseModel):
    port:str = Field(alias='REDIS_PORT')
    host:str = Field(alias='REDIS_HOST')
    redis_db:str = Field(alias='REDIS_DB')


class Config(BaseModel):
    bot: BotConfig = Field(default_factory=lambda: BotConfig(**env))
    postgres: PostgresConfig = Field(default_factory=lambda: PostgresConfig(**env))
    redis: RedisConfig = Field(default_factory=lambda: RedisConfig(**env))