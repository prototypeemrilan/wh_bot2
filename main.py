from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from dotenv import load_dotenv
from os import getenv
import logging
from my_addons.admin import start_command
from my_addons.help_command import help
from my_addons.myinfo_command import myinfo
from my_addons.pictures_command import picture
from my_addons.shop import shop_start
from my_addons.shop_souvenier import shop_souvenier
from my_addons.shop_adress import shop_adress
from my_addons.shop_magnets import shop_magnets
from my_addons.shop_switshots import shop_switshots
from my_addons.buy_item import buy_item
from my_addons.echo_command import chsv_uper


load_dotenv()

bot= Bot(getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(help, commands=['help'])
dp.register_message_handler(myinfo, commands=['myinfo'])
dp.register_message_handler(picture, commands=['picture'])
dp.register_callback_query_handler(shop_start, text='shop_start')
dp.register_callback_query_handler(shop_adress, text='shop_adress')
dp.register_callback_query_handler(shop_souvenier, Text(equals='Сувениры с Душами'))
dp.register_callback_query_handler(shop_switshots, Text(equals='Свитшоты с Душами'))
dp.register_callback_query_handler(shop_magnets, Text(equals='Магниты с Душами'))
dp.register_callback_query_handler(buy_item, text='buy_item')

dp.register_message_handler(chsv_uper)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)




