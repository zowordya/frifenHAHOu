from aiogram.types import FSInputFile
from aiogram import Router, F
from aiogram.types import ChatMemberUpdated, Message

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! 👋\n"
        "Добро пожаловать в наш чат-бот. Чем могу помочь?"
    )
@router.chat_member()
async def on_user_leave(event: ChatMemberUpdated):
    if event.old_chat_member.status in ['member', 'administrator'] and event.new_chat_member.status == 'left':
        user = event.from_user
        photo_path = "fr.jpg"  # Замените на путь к вашему фото
        photo = FSInputFile(photo_path)
        await event.bot.send_photo(
            chat_id=event.chat.id,
            photo=photo,
            caption=f"Тупой мудак {user.full_name} покинул чат. НЕ ждём тебя снова! 🤍"
        )
#гит работает или как?
