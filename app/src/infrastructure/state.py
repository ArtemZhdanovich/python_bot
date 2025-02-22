from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateRedisStorage

from app.src.configs import RedisConfig


def get_state_redis_storage(configs: RedisConfig) -> StateRedisStorage:
    return StateRedisStorage(
        host=configs.host,
        port=configs.port,
        db=configs.redis_db
    )


class UserStates(StatesGroup):
    waiting_data1 = State()
    waiting_data2 = State()