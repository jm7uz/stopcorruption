import sqlite3
import aiohttp 
from aiogram.filters import CommandStart
from aiogram import types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext

from loader import dp, db

from keyboards.default.mainMenu import lang, menuuz, menuru

from states.login import LoginPage
from oneIdService.oneid import loginOnePage, UserData


lang_change = """🇺🇿Assalomu alaykum, iltimos tilni tanlang
🇷🇺Здравствуйте, выберите пожалуйста язык"""

@dp.message(CommandStart())
async def start_bot(message:types.Message, state: FSMContext):
    try:
        #get_data page
        if True:
            await message.answer(lang_change, reply_markup=lang)
            await state.set_state(LoginPage.lang)
    except sqlite3.IntegrityError as err:
        user = db.select_user(telegram_id = message.from_user.id)
        btn = InlineKeyboardBuilder()
        btn.button(text="stopcorruption.uz", url="https://www.stopcorruption.uz/")
        btn.adjust(3)
        if user[3] == 'uz':
            await message.answer("Rasmiy sahifalar:", reply_markup=btn.as_markup())
            await message.answer("🏛 Bosh Menyu", reply_markup=menuuz)
        else:
            await message.answer("Официальные страницы:", reply_markup=btn.as_markup())
            await message.answer("🏛 Главное меню", reply_markup=menuru)

    
@dp.message(F.text, LoginPage.lang)
async def change_lang(msg: types.Message, state: FSMContext):
    lang = msg.text
    if "🇺🇿" in lang:
        await msg.answer("OneId tizimi orqali ro'yxatdan olingan login kiriting: ")
        await state.set_data(
            {
                "language" : "uz"
            }
        )
    elif "🇷🇺" in lang:
        await msg.answer("Введите логин, зарегистрированный через систему OneId: ")
        await state.set_data(
            {
                "language" : "ru"
            }
        )
    await state.set_state(LoginPage.login)
    

@dp.message(F.text, LoginPage.login)
async def login_oneId(msg: types.Message, state: FSMContext):
    
    data = await state.get_data()
    login = msg.text
    lang = str(data['language'])
    print(lang, "uz" == lang)
    if "uz" == lang:
        print("asd")
        await msg.answer("OneId tizimi orqali ro'yxatdan olingan parolingizni kiriting: ")
        
        await state.set_state(LoginPage.password)
    elif "ru" == lang:
        await msg.answer("Введите пароль, зарегистрированный через систему OneId: ")
        await state.set_state(LoginPage.password)
    
    await state.set_data(
        {
            "login" : login,
            "language" : lang
        }
    )
    
@dp.message(F.text, LoginPage.password)
async def password_oneId(msg: types.Message, state: FSMContext):
    data = await state.get_data()
    login = data['login']
    password = msg.text
    await msg.delete()
    lang = data['language']
    loginStatus = False
    
    token = await loginOnePage(username=login, password=password)
    if 'result' in token:
        if 'access_token' in token['result']:
            barer = token['result']['access_token']
            datas = await UserData(token=barer)
            if "profileData" in datas:
                user_datas = datas['profileData']
                fullName = user_datas['fullName']
                permitAddress = user_datas['permitAddress']
                phone = user_datas['phone']
                passportNumber = user_datas['passportNumber']
                passportIssuedBy = user_datas['passportIssuedBy']
            else:
                loginStatus = True
        else:
            loginStatus = True

    headers = {
        "Content-Type": "application/json"
        }
    url = "https://localhost:7130/api/Users"
    data = {
            "isOneID" : True,
            "telegramId": msg.from_user.id,
            "fullName": fullName,
            "permitAddress": permitAddress,
            "phone" : phone,
            "language" : lang,
            "passportNumber" : passportNumber,
            "passportIssuedBy" : passportIssuedBy
        }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            status =  await response.status()
    if "🇺🇿" in lang:
        if loginStatus:
            await msg.answer("Login yoki parol xato kiritilgan iltimos qaytadan kiring.\n/start")
        else:
            
            if status == 200:
                await msg.answer("Murojaat yuborishingiz mumkin", reply_markup=menuuz)
            else:
                await msg.answer("Iltimos qaytadan ro'yxatdan o'ting")
    else:
        if loginStatus:
            await msg.answer("Логин или пароль введены неверно. Пожалуйста, войдите снова.\n/start")
        else:
            if status == 200:
                await msg.answer("Вы можете отправить запрос.", reply_markup=menuru)
            else:
                await msg.answer("Пожалуйста, зарегистрируйтесь еще раз.")
    

        
    await state.clear()