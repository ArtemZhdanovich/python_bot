 
import contextlib

from telebot import TeleBot
from telebot.types import Message


class DeleteMessage:
    def __init__(self, bot: TeleBot,
        cache_storage:  
    ) -> None:
        self.bot = bot

    def update_msg_to_del(self, chat_id:int, user_id:int, msg:Union[Message, List[Message]], flag:bool=False) -> None:
        # sourcery skip: avoid-builtin-shadow
        obj_type = isinstance(msg)
        key = 'msg_del_thread' if flag else 'msg_del'
        if obj_type == list:
            id = [message.message_id for message in msg]
        else:   
            id = msg.message_id
        value = {'chat_id':msg.chat.id, 'message_id': id}
        cache_storage.set_value(chat_id, user_id, key, value)


    def del_msg(self, chat_id:int, user_id:int, flag:bool=False, return_state_data:bool=False) -> Optional[dict]:
        key = 'msg_del_thread' if flag else 'msg_del'
        msg = cache_storage.get_value(chat_id, user_id).get(key)
        with contextlib.suppress():
            if isinstance(msg['message_id']) == list:
                for message in msg['message_id']:
                    self.bot.delete_message(int(msg['chat_id']), message)
            self.bot.delete_message(int(msg['chat_id']), msg['message_id'])
        if return_state_data:
            return msg