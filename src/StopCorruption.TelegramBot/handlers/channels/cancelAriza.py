from aiogram import types, F

from loader import dp, db, bot
from aiogram.utils.keyboard import InlineKeyboardBuilder

channel_id = -1002057290166


@dp.callback_query(F.data.startswith("cancelAriza"))
async def updatePending(call: types.CallbackQuery):
    await call.answer("Botga kirib tasdiqlang.")
    post_id = int(str(call.data).replace("cancelAriza:", ""))
    from_user_id = db.select_complaint(post_id = post_id)
    user_id = call.from_user.id
    message_id = call.message.message_id
    btn = InlineKeyboardBuilder()
    btn.button(text="✅Ha", callback_data=f"stageTwoCancelYes:{from_user_id[2]}-{post_id}-{message_id}")
    btn.button(text="❌Yo'q", callback_data=f"stageTwoCancel:{from_user_id[2]}-{post_id}-{message_id}")
    btn.adjust(2)
    await bot.copy_message(chat_id=user_id, from_chat_id=channel_id, message_id=call.message.message_id, reply_markup=btn.as_markup())

@dp.callback_query(F.data.startswith("stageTwoCancel"))
async def updatePending(call: types.CallbackQuery):
    data = str(call.data)
    if data.startswith("stageTwoCancelYes"):
        data = str(call.data).replace("stageTwoCancelYes:", "")
        from_user_id, post_id, message_id = data.split("-")
        try:
            db.update_complaint_status(status="cancel", post_id=int(post_id))
            await bot.delete_message(chat_id=channel_id, message_id=int(message_id))
            await call.message.delete()
            await bot.send_message(chat_id=int(from_user_id), text="Arizangiz Bekor qilindi.\n\nВаша заявка была отменена.")
        except Exception as e:
            pass
    else:
        await call.message.delete()