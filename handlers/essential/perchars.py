import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, pear_keyboard
from loader import dp, bot


@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer('Edit @Sberleadbot info.\n'
                        'Name: Бот для Заданий на Курсе Udemy\n'
                        'Description: ?\n'
                        'About: ?\n'
                        'Botpic: ?nobotpic\n'
                        'Commands: nocommandsyet\n',
                         reply_markup=choice
                        )

@dp.message_handler(buy_callback.filter(item_name='pear'))
async def buying_pear(call:CallbackQuery, callback_data: dict):
    # await bot.answer_callback_query(callback_query_id=call.id)
    await call.answer(cache_time=60)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    quantity = callback_data.get('quantity')
    await call.message.answer(f'Вы выбрали груши, в количестве: {quantity} шт. Спасибо!',
                              reply_markup=pear_keyboard)
