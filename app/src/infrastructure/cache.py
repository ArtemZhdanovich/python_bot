import redis
from redis import Redis
from app.src.configs import RedisConfig

def new_redis_client(redis_config: RedisConfig) -> Redis:
    pool = redis.ConnectionPool(
        host = redis_config.host,
        port = redis_config.port,
        db = redis_config.redis_db)
    return Redis(connection_pool=pool)