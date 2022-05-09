from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(row_width=2,
                              inline_keyboard=[
                                  [
                                      InlineKeyboardButton(
                                          text='Купить грушу',
                                          callback_data=buy_callback.new(item_name='pear',
                                                                         quantity=1)
                                      ),
                                      InlineKeyboardButton(
                                          text='Купить яблоки',
                                          callback_data='buy:apple:5'
                                      )
                                  ],
                                  [
                                      InlineKeyboardButton(
                                          text='Отмена',
                                          callback_data='cansel'
                                      )
                                  ]
                              ])

pear_keyboard = InlineKeyboardMarkup()
PEAR_LINK = 'https://ru.stackoverflow.com/questions/1032284/%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-pycharm-github'
pear_link = InlineKeyboardButton(text='Купи тут',
                                 url=PEAR_LINK)
pear_keyboard.insert(pear_link)