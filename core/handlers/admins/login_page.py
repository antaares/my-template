from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from aiogram.dispatcher.storage import FSMContext
from filters.is_admin import IsAdmin
from filters.is_private import IsPrivate

from loader import dp

from handlers.admins.keyboards import login_page_keyboard, remove_button




@dp.message_handler(IsPrivate(), IsAdmin(), Command('login'), state="*")
async def login(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await message.answer("Assalomu alaykum, siz admin paneldasiz...")
    await message.answer(text="Qanday amal bajaramiz?", reply_markup=login_page_keyboard)


@dp.message_handler(IsPrivate(), IsAdmin(), Command('logout'), state="*")
async def logout(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await message.answer("Admin panledan chiqdingiz.", reply_markup=remove_button)
    await message.answer(f"Hello, {message.from_user.full_name}!")



