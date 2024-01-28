from aiogram import types, F

from loader import dp, db, bot

@dp.callback_query(F.data.startswith("statusUpdate"))
async def updatePending(call: types.CallbackQuery):
    await call.answer("✅Status o'zgartirildi.")
    post_id = int(str(call.data).replace("statusUpdate:", ""))

    post_full = db.select_complaint(post_id = post_id)

    db.update_complaint_status(status="pending", post_id=post_id)

    try:
        await bot.send_message(chat_id=post_full[2], text="Arizangiz holati yangilandi, ko'rib chiqilmoqda ohirgi yakun sizga ma'lum qilinadi.\n\nСтатус вашей заявки был обновлен, и вы будете уведомлены об окончательном результате.")
    except Exception as e:
        pass