import logging
import os
import random
from typing import Iterable

import telebot
from telebot.types import Message

from dishka import Provider, Scope, provide, make_container
from dishka.integrations.telebot import (
    FromDishka, inject, setup_dishka, TelebotProvider,
)

from app.src.configs import BotConfig, Config

# app dependency logic
class MyProvider(Provider):
    @provide(scope=Scope.APP)
    def get_int(self) -> Iterable[int]:
        print("solve int")
        yield random.randint(0, 10000)



configs = Config()
bot = telebot.TeleBot(configs.bot.noken, use_class_middlewares=True)




logging.basicConfig(level=logging.INFO)

container = make_container(MyProvider(), TelebotProvider())
setup_dishka(container=container, bot=bot)
try:
    bot.infinity_polling()
finally:
    container.close()