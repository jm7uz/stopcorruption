from aiogram import types, F

from loader import dp, db


@dp.message(F.text == "🗂Murojaatlarim")
@dp.message(F.text == "🗂Мои заявку")
async def all_murojatlar(msg: types.Message):
    user = db.select_user(telegram_id = msg.from_user.id)
    murojatlar = db.select_all_complaints()
    if user[3] == "uz":
        txt = "🗃Barcha arizalaringiz:\n\n"
    else:
        txt = "🗃Все ваши приложения:\n\n"
    for n in murojatlar:
        if n[2] == msg.from_user.id:

            if user[3] == "uz":
                txt += f"📄Arzia qabul qilndi: {n[1]}\n🌏Ijrochi: {n[3]} {n[4]}\n📞Tel {n[8]}\n\n"
            else:
                txt += f"📄ваша заявка принята: {n[1]}\n🌏Инспектор: {n[3]} {n[4]}\n📞Тел.{n[8]}\n\n"
    
    await msg.answer(txt)
