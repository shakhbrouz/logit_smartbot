from aiogram import Router, types
from db import add_user

router = Router()

@router.message(commands=["start"])
async def start_handler(message: types.Message):
    await add_user(message.from_user.id, message.from_user.full_name)
    await message.answer(f"Привет, {message.from_user.full_name}! Вы зарегистрированы.")

def register_start(dp):
    dp.include_router(router)