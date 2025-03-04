from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardButton,InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='123',callback_data='Nan')],
    [InlineKeyboardButton(text='penis',callback_data='Na1')]
    ])


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Фильм под настроение',callback_data='test')],
    ])

# def inline_moods():
#     moods = InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text='Весёлое',callback_data='NaN')],[InlineKeyboardButton(text='Бодрое',callback_data='NaN')],
#         [InlineKeyboardButton(text='Грустное',callback_data='NaN')],[InlineKeyboardButton(text='Страшное',callback_data='NaN')],
#         [InlineKeyboardButton(text='Не могу определиться',callback_data='NaN')]
#         ])

moods = ['Веселое','Бодрое','Грустное','Страшное','Не знаю']

async def inline_moods():
    keyboard = InlineKeyboardBuilder()
    for mood in moods:
        keyboard.add(InlineKeyboardButton(text = mood, callback_data=f'Moods_{mood}'))
    return keyboard.adjust(2).as_markup()


# moods = ['Веселое','Бодрое','Грустное','Страшное','Не знаю']


# async def inline_mood():
#     keyboard = InlineKeyboardBuilder()
#     for mood in moods:
#         keyboard.add(InlineKeyboardButton(text = mood, callback_data = f'Moods_{mood}'))
#     return keyboard.adjust(2).as_markup()