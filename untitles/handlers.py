from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State

import untitles.keyboards as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f'Привет {message.from_user.full_name}!\nЯ бот, который поможет подобрать фильм под твоё настроение!',
                        reply_markup=kb.settings)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('This is command /help')

@router.message(F.text == 'How are you?')
async def how_are_you(message:Message):
    await message.answer("I'm fine!")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID photo:\n{message.photo[-1].file_id}')

@router.message(Command('get_photo'))
async def get_photo(message:Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAOWZ8M6bwyin-h_NRJOJBMv6JcGTngAAhbvMRsOECFKdnDJj90aon0BAAMCAAN4AAM2BA',
                               caption='This is Toyota Crown!❤️')

@router.callback_query(F.data == 'test')
async def POMENYAT(callback:CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('Выбери своё настроение, а я подберу под тебя фильм!', reply_markup =await kb.inline_moods())

