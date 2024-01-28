from aiogram import types, F

from loader import dp, db, bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

@dp.callback_query(F.data.startswith("getLocation"))
async def updatePending(call: types.CallbackQuery):
    await call.answer("Botga yuborildi.")
    post_id = int(str(call.data).replace("getLocation:", ""))
    arizaData = db.select_complaint(post_id = post_id)
    await bot.send_location(chat_id=call.from_user.id, latitude=arizaData[6], longitude=arizaData[7])