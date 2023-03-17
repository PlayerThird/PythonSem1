import random

import redis

# redis_server = redis.Redis()#передаём поток
#
# redis_server.close()#закрываем поток

with redis.Redis() as redis_server:#автоматически закрывает поток, когда код внутри with выполнится(закончится)
    redis_server.lpush("que", random.randint(0,10))#пушим слева