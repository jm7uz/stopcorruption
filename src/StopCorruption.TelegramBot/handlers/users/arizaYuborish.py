from aiogram import types, F
from aiogram.fsm.context import FSMContext

from aiogram.types import FSInputFile

from states.murojat import RegisterPage
from loader import dp, db, bot

from keyboards.default.mainMenu import canceluz, cancelru, \
    menuuz, menuru, cancelcontactuz, cancelcontactru, cancellocationuz, cancellocationru

from keyboards.inline.regions import regionsuz, regionsru
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove

channel_id = -1002057290166

regionsdict = {
    "andijonuz": "Andijon viloyati",
    "fargonauz": "Farg‘ona viloyati",
    "namanganuz": "Namangan viloyati",
    "toshkentviluz": "Toshkent viloyati",
    "toshkentshuz": "Toshkent shahri",
    "surxondaryouz": "Surxondaryo viloyati",
    "samarqanduz": "Samarqand viloyati",
    "buxorouz": "Buxoro viloyati",
    "sirdaryouz": "Sirdaryo viloyati",
    "xorazmuz": "Xorazm viloyati",
    "qashqadaryouz": "Qashqadaryo viloyati",
    "navoiyuz": "Navoiy viloyati",
    "qoraqalpogistonuz": "Qoraqalpog‘iston Respublikasi",
    "jizzaxuz": "Jizzax viloyati",
    "andijonru": "Андижанская область",
    "fargonaru": "Ферганская область",
    "namanganru": "Наманганская область",
    "toshkentvilru": "Ташкентская область",
    "toshkentshru": "город Ташкент",
    "surxondaryoru": "Сурхандарьинская область",
    "samarqandru": "Самаркандская область",
    "buxororu": "Бухарская область",
    "sirdaryoru": "Сырдарьинская область",
    "xorazmru": "Хорезмская область",
    "qashqadaryoru": "Кашкадарьинская область",
    "navoiyru": "Навоийская область",
    "qoraqalpogistonru": "Республика Каракалпакстан",
    "jizzaxru": "Джизакская область",
}

provincedict = {'qoraqalpogistonuz': ['Nukus shahri', 'Amudaryo tumani', 'Beruniy tumani', 'Kegeyli tumani', "Qorao'zak tumani", "Qonliko'l tumani", "Qo'ng'irot tumani", "Mo'ynok tumani", 'Nukus tumani', "Taxtako'pir tumani", "To'rtko'l tumani", "Xo'jayli tumani", 'Chimboy tumani', 'Shumanay tumani', "Ellikqal'a tumani", 'Taxiatosh tumani', "Bo'zatov tumani"], 'andijonuz': ['Andijon shahar', "Oltinko'l tumani", 'Baliqchi tumani', "Bo'z tumani", 'Shahrixon tumani', 'Asaka tumani', 'Marxamat tumani', 'Buloqboshi tumani', "Xo'jaobod tumani", 'Paxtaobod tumani', 'Izboskan tumani', "Qo'rg'ontepa tumani", 'Xonobod shahar', 'Andijon tumani', "Ulug'nor tumani", 'Jalaquduq tumani'], 'buxorouz': ['Kogon shahar', 'Buxoro tuman', 'Vobkent tuman', 'Jondor tuman', 'Kogon tuman', 'Olot tuman', 'Peshku tuman', 'Romitan tuman', 'Shofirkon tuman', "Qorako'l tuman", 'Qorovulbozor tuman', "G'ijduvon tuman"], 'jizzaxuz': ['Jizzax shahar', 'Arnasoy tumani', 'Baxmal tumani', "Do'stlik tumani", 'Sharof Rashidov tumani', 'Zarbdor tumani', 'Zafarobod tumani', 'Zomin tumani', "Mirzacho'l tumani", 'Paxtakor tumani', 'Forish tumani', "G'allaorol tumani", 'Yangiobod tumani'], 'navoiyuz': ['Navoiy shahar', 'Karmana tuman', 'Qiziltepa tuman', 'Konimex tuman', 'Uchquduq tuman', 'Tomdi tuman', 'Zarafshon shahar', 'Xatirchi tuman', 'Navbahor tuman', 'Nurota tuman', "G'ozg'on shahar"], 'namanganuz': ['Namangan shahri', 'Kosonsoy tumani', 'Mingbuloq tumani', 'Namangan tumani', 'Norin tumani', 'Pop tumani', "To'raqo'rg'on tumani", 'Uychi tumani', "Uchqo'rg'on tumani", 'Chortoq tumani', 'Chust tumani', 'Davlatobod tumani', 'Yangi Namangan tumani', "Yangiqo'rg'on tumani"], 'samarqanduz': ['Samarqand shahri', 'Oqdaryo tumani', "Bulung'ur tumani", 'Jomboy tumani', 'Payariq tumani', "Qo'shrabot tumani", 'Ishtixon tumani', "Kattaqo'rg'on tumani", "Kattaqo'rg'on shahri", 'Narpay tumani', 'Paxtachi tumani', 'Nurobod tumani', "Pastdarg'om tumani", 'Samarqand tumani', 'Toyloq tumani', 'Urgut tumani'], 'sirdaryouz': ['Guliston shahar', 'Mirzaobod tumani', 'Oqoltin tumani', 'Sirdaryo tumani', 'Sayxunobod tumani', 'Yangier shahar', 'Sardoba tumani', 'Xovos tumani', 'Shirin shahar', 'Boyovut tumani', 'Guliston tumani'], 'surxondaryouz': ['Boysun tumani', 'Sherobod tumani', 'Angor tumani', 'Muzrabot tumani', 'Termiz tumani', 'Termiz shahri', "Jarqo'rg'on tumani", 'Qiziriq tumani', "Qumqo'rg'on tumani", "Sho'rchi tumani", 'Oltinsoy tumani', 'Denov tumani', 'Sariosiyo tumani', 'Uzun tumani', 'Bandixon tumani'], 'toshkentviluz': ['Angren shahri', 'Bekobod shahri', 'Olmaliq shahri', 'Oxangaron shahar', 'Nurafshon shahar', 'Chirchiq shahri', "Yangiyo'l shahri", 'Bekobod tumani', "Bo'ka tumani", "Bo'stonliq tumani", 'Qibray tumani', 'Quyi Chirchiq tumani', "Oqqo'rg'on tumani", 'Ohangaron tumani', 'Parkent tumani', 'Piskent tumani', 'Toshkent tumani', 'Zangiota tumani', "O'rta Chirchiq tumani", 'Chinoz tumani', 'Yuqori Chirchiq tumani', "Yangiyo'l tumani"], 'fargonauz': ["Farg'ona shahar", "Marg'ilon shahar", 'Quvasoy shahar', "Qo'qon shahar", 'Beshariq tumani', "Bag'dod tumani", 'Buvayda tumani', "Dang'ara tumani", 'Yozyovon tumani', 'Quva tumani', 'Oltiariq tumani', "Qo'shtepa tumani", 'Rishton tumani', "So'x tumani", 'Toshloq tumani', "O'zbekiston tumani", "Uchko'prik tumani", "Farg'ona tumani", 'Furqat tumani'], 'xorazmuz': ['Urganch shahar', "Bog'ot tumani", 'Gurlan tumani', "Qo'shko'pir tumani", 'Urganch tumani', 'Xazorasp tumani', 'Xonqa tumani', 'Xiva tumani', 'Xiva shahar', 'Shovot tumani', 'Yangiariq tumani', 'Yangibozor tumani', 'Tuproqqala tumani'], 'qashqadaryouz': ['Qarshi shahri', 'Shahrisabz shahri', "G'uzor tumani", 'Dehqonobod tumani', 'Qamashi tumani', 'Qarshi tumani', 'Kasbi tumani', 'Kitob tumani', 'Koson tumani', 'Mirishkor tumani', 'Muborak tumani', 'Nishon tumani', 'Chiroqchi tumani', 'Shahrisabz tumani', "Ko'kdala tumani", "Yakkabog' tumani"], 'toshkentshuz': ['Uchtepa tumani', 'Bektemir tumani', "M.Ulug'bek tumani", 'Mirobod tumani', 'Olmazor tumani', 'Sergeli tumani', 'Yashnobod tumani', 'Chilonzor tumani', 'Shayxontohur tumani', 'Yunusobod tumani', 'Yakkasaroy tumani', 'Yangi xayot tumani'],'qoraqalpogistonru': ['Город Нукус', 'Амударьинский район', 'Берунийский район', 'Кегейлинский район', 'Караозакский район', 'Конликольский район', 'Позвонить в район', 'Мойнокский район', 'Нукусский район', 'Тахтакорпирский район', 'Торткольский район', 'Ходжалинский район', 'Чимбойский район', 'Шуманайский район', 'Элликкалинский район', 'Тахиатошский район', 'Бозатовский район'], 'andijonru': ['город Андижан', 'Олтинкольский район', 'Рыбацкий район', 'Бозский район', 'Шахриханский район', 'Асакинский район', 'Мархаматский район', 'Булагбошинский район', 'Ходжаабадский район', 'Пахтаабадский район', 'Избосканский район', 'Коргонтепинский район', 'город Ханабад', 'Андижанский район', 'Улугнорский район', 'Джалакудукский район'], 'buxororu': ['город Когон', 'Бухарский район', 'Вобкентский район', 'Оживленный район', 'Когонский район', 'Олотский район', 'Пешкунский район', 'Ромитанский район', 'Шафирконский район', 'Каракольский район', 'Каровулбазарский район', 'Гиждуванский район'], 'jizzaxru': ['город Джизак', 'Арнасойский район', 'Бархатный район', 'Район Дружбы', 'Шароф Рашидовский район', 'Зарбдарский район', 'Зафарабадский район', 'Зоминский район', 'Мирзачольский район', 'Пахтакорский район', 'Форишский район', 'Галлаорольский район', 'Янгиабадский район'], 'navoiyru': ['город Навои', 'Карманинский район', 'Кизилтепинский район', 'Конимехский район', 'Узгудукский район', 'Томди туман', 'Красивый город', 'Хатырчинский район', 'Навбахорский район', 'Нуратинский район', 'город Газгон'], 'namanganru': ['город Наманган', 'Косонсойский район', 'Мингбулокский район', 'Наманганский район', 'Норинский район', 'Поп-район', 'Торакурганский район', 'Уйчинский район', 'Учкурганский район', 'Чортокский район', 'Чустский район', 'Давлатабадский район', 'Новый Наманганский район', 'Янгикурганский район'], 'samarqandru': ['город Самарканд', 'Акдарьинский район', 'Булунгурский район', 'Джомбойский район', 'Паярикский район', 'Хошработский район', 'Иштиханский район', 'Каттакурганский район', 'город Каттакурган', 'Нарпайский район', 'Пахтачинский район', 'Нурабадский район', 'Пастдаргомский район', 'Самаркандская область', 'Тойлокский район', 'Ургутский район'], 'sirdaryoru': ['город Гулистан', 'Мирзаабадский район', 'Аколтинский район', 'Сырдарьинский район', 'Сайхунабадский район', 'Новый город', 'Сардобинский район', 'Хавосский район', 'Милый город', 'Бойовутский район', 'Гулистанский район'], 'surxondaryoru': ['Байсунский район', 'Шерабадский район', 'Ангорский район', 'Музработский район', 'Термезский район', 'Город Термез', 'Джаркурганский район', 'Кызирикский район', 'Кумкурганский район', 'Шорчинский район', 'Алтинсойский район', 'Деновский район', 'Сариосийский район', 'Узунский район', 'Бандиханский район'], 'toshkentvilru': ['Город Ангрен', 'город Бекобад', 'город Алмалык', 'город Ахангарон', 'Яркий город', 'город Чирчик', 'город Янёль', 'Бекобадский район', 'Бокинский район', 'Бостанлыкский район', 'Кибрайский район', 'Нижне-Чирчикский район', 'Аккурганский район', 'Охангаронский район', 'Паркентский район', 'Пискентский район', 'Ташкентский район', 'Зангиотский район', 'Средний Чирчикский район', 'Чинозский район', 'Верхне-Чирчикский район', 'Янгиёлский район'], 'fargonaru': ['город Фергана', 'город Маргилан', 'город Кувасой', 'город Кокан', 'Бешарикский район', 'Багдадский район', 'Бувайдский район', 'Дангаринский район', 'Ежиовонский район', 'Кувинский район', 'Алтыарикский район', 'Коштепинский район', 'Риштонский район', 'Сохский район', 'Тошлокский район', 'Район Узбекистана', 'Учкоприкский район', 'Ферганский район', 'Фуркатский район'], 'xorazmru': ['город Ургенч', 'Боготский район', 'Гурланский район', 'Кошкопирский район', 'Ургенчский район', 'Хазораспский район', 'Ханкайский район', 'Хивинский район', 'город Хива', 'Шаватский район', 'Янгарикский район', 'Янгибазорский район', 'Тупарккалинский район'], 'qashqadaryoru': ['город Карши', 'город Шахрисабз', 'Гузорский район', 'Дехканабадский район', 'Камашинский район', 'Каршинский район', 'Касбийский район', 'Книжный район', 'Косонский район', 'Миришкорский район', 'Мубаракский район', 'Целевой район', 'Чиракчинский район', 'Шахрисабзский район', 'Кокдалинский район', 'Яккабогский район'], 'toshkentshru': ['Учтепинский район', 'Бектемирский район', 'М.Улугбекский район', 'Мирабадский район', 'Алмазарский район', 'Сергелийский район', 'Яшнабадский район', 'Чиланзорский район', 'Шайхонтохурский район', 'Юнусабадский район', 'Яккасарайский район', 'Район новой жизни']}

def extract_numbers(input_string):
    return ''.join(char for char in input_string if char.isdigit())

qoidabuzarlikPath = FSInputFile("utils/qoidabuzarlik.jpg")

@dp.message(F.text == "📑Murojaat jo‘natish")
@dp.message(F.text == "📑Отправить заявку")
async def arizaOlish(msg: types.Message, state: FSMContext):
    user = db.select_user(telegram_id = msg.from_user.id)

    if user[3] == "uz":
        await msg.answer("Xududni tanlang ", reply_markup=regionsuz)
    else:
        await msg.answer("Выберите область ", reply_markup=regionsru)
      
    await state.set_state(RegisterPage.region)




@dp.callback_query(F.data.endswith("uz"), RegisterPage.region)
@dp.callback_query(F.data.endswith("ru"), RegisterPage.region)
async def get_provinces(query: types.CallbackQuery, state: FSMContext):
    text = query.data
    print(text)
    await query.answer("✅")
    await query.message.delete()
    await state.update_data(
            {
                "region" : text
            }
        )

    if text in ["canceluz", "cancelru"]:
        if text == "canceluz":
            await query.message.answer("Bosh sahifa", reply_markup=menuuz)
        else:
            await query.message.answer("Главное меню", reply_markup=menuru)
        await state.clear()
    else:
        if query.data.endswith("uz"):
            province = {'qoraqalpogistonuz': ['Nukus shahri', 'Amudaryo tumani', 'Beruniy tumani', 'Kegeyli tumani', "Qorao'zak tumani", "Qonliko'l tumani", "Qo'ng'irot tumani", "Mo'ynok tumani", 'Nukus tumani', "Taxtako'pir tumani", "To'rtko'l tumani", "Xo'jayli tumani", 'Chimboy tumani', 'Shumanay tumani', "Ellikqal'a tumani", 'Taxiatosh tumani', "Bo'zatov tumani"], 'andijonuz': ['Andijon shahar', "Oltinko'l tumani", 'Baliqchi tumani', "Bo'z tumani", 'Shahrixon tumani', 'Asaka tumani', 'Marxamat tumani', 'Buloqboshi tumani', "Xo'jaobod tumani", 'Paxtaobod tumani', 'Izboskan tumani', "Qo'rg'ontepa tumani", 'Xonobod shahar', 'Andijon tumani', "Ulug'nor tumani", 'Jalaquduq tumani'], 'buxorouz': ['Kogon shahar', 'Buxoro tuman', 'Vobkent tuman', 'Jondor tuman', 'Kogon tuman', 'Olot tuman', 'Peshku tuman', 'Romitan tuman', 'Shofirkon tuman', "Qorako'l tuman", 'Qorovulbozor tuman', "G'ijduvon tuman"], 'jizzaxuz': ['Jizzax shahar', 'Arnasoy tumani', 'Baxmal tumani', "Do'stlik tumani", 'Sharof Rashidov tumani', 'Zarbdor tumani', 'Zafarobod tumani', 'Zomin tumani', "Mirzacho'l tumani", 'Paxtakor tumani', 'Forish tumani', "G'allaorol tumani", 'Yangiobod tumani'], 'navoiyuz': ['Navoiy shahar', 'Karmana tuman', 'Qiziltepa tuman', 'Konimex tuman', 'Uchquduq tuman', 'Tomdi tuman', 'Zarafshon shahar', 'Xatirchi tuman', 'Navbahor tuman', 'Nurota tuman', "G'ozg'on shahar"], 'namanganuz': ['Namangan shahri', 'Kosonsoy tumani', 'Mingbuloq tumani', 'Namangan tumani', 'Norin tumani', 'Pop tumani', "To'raqo'rg'on tumani", 'Uychi tumani', "Uchqo'rg'on tumani", 'Chortoq tumani', 'Chust tumani', 'Davlatobod tumani', 'Yangi Namangan tumani', "Yangiqo'rg'on tumani"], 'samarqanduz': ['Samarqand shahri', 'Oqdaryo tumani', "Bulung'ur tumani", 'Jomboy tumani', 'Payariq tumani', "Qo'shrabot tumani", 'Ishtixon tumani', "Kattaqo'rg'on tumani", "Kattaqo'rg'on shahri", 'Narpay tumani', 'Paxtachi tumani', 'Nurobod tumani', "Pastdarg'om tumani", 'Samarqand tumani', 'Toyloq tumani', 'Urgut tumani'], 'sirdaryouz': ['Guliston shahar', 'Mirzaobod tumani', 'Oqoltin tumani', 'Sirdaryo tumani', 'Sayxunobod tumani', 'Yangier shahar', 'Sardoba tumani', 'Xovos tumani', 'Shirin shahar', 'Boyovut tumani', 'Guliston tumani'], 'surxondaryouz': ['Boysun tumani', 'Sherobod tumani', 'Angor tumani', 'Muzrabot tumani', 'Termiz tumani', 'Termiz shahri', "Jarqo'rg'on tumani", 'Qiziriq tumani', "Qumqo'rg'on tumani", "Sho'rchi tumani", 'Oltinsoy tumani', 'Denov tumani', 'Sariosiyo tumani', 'Uzun tumani', 'Bandixon tumani'], 'toshkentviluz': ['Angren shahri', 'Bekobod shahri', 'Olmaliq shahri', 'Oxangaron shahar', 'Nurafshon shahar', 'Chirchiq shahri', "Yangiyo'l shahri", 'Bekobod tumani', "Bo'ka tumani", "Bo'stonliq tumani", 'Qibray tumani', 'Quyi Chirchiq tumani', "Oqqo'rg'on tumani", 'Ohangaron tumani', 'Parkent tumani', 'Piskent tumani', 'Toshkent tumani', 'Zangiota tumani', "O'rta Chirchiq tumani", 'Chinoz tumani', 'Yuqori Chirchiq tumani', "Yangiyo'l tumani"], 'fargonauz': ["Farg'ona shahar", "Marg'ilon shahar", 'Quvasoy shahar', "Qo'qon shahar", 'Beshariq tumani', "Bag'dod tumani", 'Buvayda tumani', "Dang'ara tumani", 'Yozyovon tumani', 'Quva tumani', 'Oltiariq tumani', "Qo'shtepa tumani", 'Rishton tumani', "So'x tumani", 'Toshloq tumani', "O'zbekiston tumani", "Uchko'prik tumani", "Farg'ona tumani", 'Furqat tumani'], 'xorazmuz': ['Urganch shahar', "Bog'ot tumani", 'Gurlan tumani', "Qo'shko'pir tumani", 'Urganch tumani', 'Xazorasp tumani', 'Xonqa tumani', 'Xiva tumani', 'Xiva shahar', 'Shovot tumani', 'Yangiariq tumani', 'Yangibozor tumani', 'Tuproqqala tumani'], 'qashqadaryouz': ['Qarshi shahri', 'Shahrisabz shahri', "G'uzor tumani", 'Dehqonobod tumani', 'Qamashi tumani', 'Qarshi tumani', 'Kasbi tumani', 'Kitob tumani', 'Koson tumani', 'Mirishkor tumani', 'Muborak tumani', 'Nishon tumani', 'Chiroqchi tumani', 'Shahrisabz tumani', "Ko'kdala tumani", "Yakkabog' tumani"], 'toshkentshuz': ['Uchtepa tumani', 'Bektemir tumani', "M.Ulug'bek tumani", 'Mirobod tumani', 'Olmazor tumani', 'Sergeli tumani', 'Yashnobod tumani', 'Chilonzor tumani', 'Shayxontohur tumani', 'Yunusobod tumani', 'Yakkasaroy tumani', 'Yangi xayot tumani']}
            provinces = province[query.data]
            index = 0
            btn = InlineKeyboardBuilder()
            for province in provinces:
                btn.button(text=province,callback_data=f"proviceuz:{index}")
                index+=1
            btn.button(text="❌Bekor qilish", callback_data=f"canceluz")
            btn.adjust(2)
            await query.message.answer(text="Tumanni tanlang", reply_markup=btn.as_markup())
        else:
            provinceru = {'qoraqalpogistonru': ['Город Нукус', 'Амударьинский район', 'Берунийский район', 'Кегейлинский район', 'Караозакский район', 'Конликольский район', 'Позвонить в район', 'Мойнокский район', 'Нукусский район', 'Тахтакорпирский район', 'Торткольский район', 'Ходжалинский район', 'Чимбойский район', 'Шуманайский район', 'Элликкалинский район', 'Тахиатошский район', 'Бозатовский район'], 'andijonru': ['город Андижан', 'Олтинкольский район', 'Рыбацкий район', 'Бозский район', 'Шахриханский район', 'Асакинский район', 'Мархаматский район', 'Булагбошинский район', 'Ходжаабадский район', 'Пахтаабадский район', 'Избосканский район', 'Коргонтепинский район', 'город Ханабад', 'Андижанский район', 'Улугнорский район', 'Джалакудукский район'], 'buxororu': ['город Когон', 'Бухарский район', 'Вобкентский район', 'Оживленный район', 'Когонский район', 'Олотский район', 'Пешкунский район', 'Ромитанский район', 'Шафирконский район', 'Каракольский район', 'Каровулбазарский район', 'Гиждуванский район'], 'jizzaxru': ['город Джизак', 'Арнасойский район', 'Бархатный район', 'Район Дружбы', 'Шароф Рашидовский район', 'Зарбдарский район', 'Зафарабадский район', 'Зоминский район', 'Мирзачольский район', 'Пахтакорский район', 'Форишский район', 'Галлаорольский район', 'Янгиабадский район'], 'navoiyru': ['город Навои', 'Карманинский район', 'Кизилтепинский район', 'Конимехский район', 'Узгудукский район', 'Томди туман', 'Красивый город', 'Хатырчинский район', 'Навбахорский район', 'Нуратинский район', 'город Газгон'], 'namanganru': ['город Наманган', 'Косонсойский район', 'Мингбулокский район', 'Наманганский район', 'Норинский район', 'Поп-район', 'Торакурганский район', 'Уйчинский район', 'Учкурганский район', 'Чортокский район', 'Чустский район', 'Давлатабадский район', 'Новый Наманганский район', 'Янгикурганский район'], 'samarqandru': ['город Самарканд', 'Акдарьинский район', 'Булунгурский район', 'Джомбойский район', 'Паярикский район', 'Хошработский район', 'Иштиханский район', 'Каттакурганский район', 'город Каттакурган', 'Нарпайский район', 'Пахтачинский район', 'Нурабадский район', 'Пастдаргомский район', 'Самаркандская область', 'Тойлокский район', 'Ургутский район'], 'sirdaryoru': ['город Гулистан', 'Мирзаабадский район', 'Аколтинский район', 'Сырдарьинский район', 'Сайхунабадский район', 'Новый город', 'Сардобинский район', 'Хавосский район', 'Милый город', 'Бойовутский район', 'Гулистанский район'], 'surxondaryoru': ['Байсунский район', 'Шерабадский район', 'Ангорский район', 'Музработский район', 'Термезский район', 'Город Термез', 'Джаркурганский район', 'Кызирикский район', 'Кумкурганский район', 'Шорчинский район', 'Алтинсойский район', 'Деновский район', 'Сариосийский район', 'Узунский район', 'Бандиханский район'], 'toshkentvilru': ['Город Ангрен', 'город Бекобад', 'город Алмалык', 'город Ахангарон', 'Яркий город', 'город Чирчик', 'город Янёль', 'Бекобадский район', 'Бокинский район', 'Бостанлыкский район', 'Кибрайский район', 'Нижне-Чирчикский район', 'Аккурганский район', 'Охангаронский район', 'Паркентский район', 'Пискентский район', 'Ташкентский район', 'Зангиотский район', 'Средний Чирчикский район', 'Чинозский район', 'Верхне-Чирчикский район', 'Янгиёлский район'], 'fargonaru': ['город Фергана', 'город Маргилан', 'город Кувасой', 'город Кокан', 'Бешарикский район', 'Багдадский район', 'Бувайдский район', 'Дангаринский район', 'Ежиовонский район', 'Кувинский район', 'Алтыарикский район', 'Коштепинский район', 'Риштонский район', 'Сохский район', 'Тошлокский район', 'Район Узбекистана', 'Учкоприкский район', 'Ферганский район', 'Фуркатский район'], 'xorazmru': ['город Ургенч', 'Боготский район', 'Гурланский район', 'Кошкопирский район', 'Ургенчский район', 'Хазораспский район', 'Ханкайский район', 'Хивинский район', 'город Хива', 'Шаватский район', 'Янгарикский район', 'Янгибазорский район', 'Тупарккалинский район'], 'qashqadaryoru': ['город Карши', 'город Шахрисабз', 'Гузорский район', 'Дехканабадский район', 'Камашинский район', 'Каршинский район', 'Касбийский район', 'Книжный район', 'Косонский район', 'Миришкорский район', 'Мубаракский район', 'Целевой район', 'Чиракчинский район', 'Шахрисабзский район', 'Кокдалинский район', 'Яккабогский район'], 'toshkentshru': ['Учтепинский район', 'Бектемирский район', 'М.Улугбекский район', 'Мирабадский район', 'Алмазарский район', 'Сергелийский район', 'Яшнабадский район', 'Чиланзорский район', 'Шайхонтохурский район', 'Юнусабадский район', 'Яккасарайский район', 'Район новой жизни']}
            provinces = provinceru[query.data]
            index = 0
            btn = InlineKeyboardBuilder()
            for province in provinces:
                btn.button(text=province,callback_data=f"proviceru:{index}")
                index+=1
            btn.button(text="❌Отмена", callback_data=f"cancelru")
            btn.adjust(2)
            await query.message.answer(text="Tumanni tanlang", reply_markup=btn.as_markup())
    
    await state.set_state(RegisterPage.province)

@dp.callback_query(F.data.startswith("provice"), RegisterPage.province)
@dp.callback_query(F.data.in_({"canceluz", "cancelru"}), RegisterPage.province)
async def get_provinces(query: types.CallbackQuery, state: FSMContext):
    await query.answer("✅")
    await query.message.delete()
    text = query.data

    await state.update_data(
            {
                "provice" : text
            }
        )

    if text in ["canceluz", "cancelru"]:
        if text == "canceluz":
            await query.message.answer("Bosh sahifa", reply_markup=menuuz)
        else:
            await query.message.answer("Главное меню", reply_markup=menuru)
        await state.clear()
    else:
        if text.startswith("proviceuz"):
            btn = InlineKeyboardBuilder()
            for n in range(1, 5):
                btn.button(text=str(n), callback_data=f"qoidabuzarlikuz:{n}")
            btn.button(text="❌Bekor qilish", callback_data=f"canceluz")
            btn.adjust(2)
            await query.message.answer(text="Qoidabuzarlik turini tanlang:",reply_markup=btn.as_markup())
        else:
            btn = InlineKeyboardBuilder()
            for n in range(1, 5):
                btn.button(text=str(n), callback_data=f"qoidabuzarlikru:{n}")
            btn.button(text="❌Отмена", callback_data=f"cancelru")
            btn.adjust(2)
            await query.message.answer(text="Выберите тип нарушения:", reply_markup=btn.as_markup())
    
    await state.set_state(RegisterPage.typeViolation)

@dp.callback_query(F.data.startswith("qoidabuzarlik"), RegisterPage.typeViolation)
@dp.callback_query(F.data.in_({"canceluz", "cancelru"}), RegisterPage.typeViolation)
async def get_provinces(query: types.CallbackQuery, state: FSMContext):
    await query.answer("✅")
    await query.message.delete()
    text = query.data

    await state.update_data(
            {
                "typeViolation" : text
            }
        )

    if text in ["canceluz", "cancelru"]:
        if text == "canceluz":
            await query.message.answer("Bosh sahifa", reply_markup=menuuz)
        else:
            await query.message.answer("Главное меню", reply_markup=menuru)
        await state.clear()
    else:
        if text.startswith("qoidabuzarlikuz"):
            await query.message.answer("Huquqbuzarlik sodir etilgan manzilni kiriting", reply_markup=cancellocationuz)
        else:
            await query.message.answer("Введите адрес, где произошло правонарушение", reply_markup=cancellocationuz)
    
    await state.set_state(RegisterPage.location)

@dp.message(F.location | F.text, RegisterPage.location)
async def get_location_state(msg: types.Message, state: FSMContext):
    text = msg.text

    if text in ["❌Bekor qilish", "❌Отмена"]:
        if "❌Bekor" in text:
            await msg.answer("Bosh sahifa", reply_markup=menuuz)
        else:
            await msg.answer("Главное меню", reply_markup=menuru)
        await state.clear()
    else:
        location = f"latitude:{msg.location.latitude}-longitude:{msg.location.longitude}"
        await state.update_data(
            {
                "latitude" : msg.location.latitude,
                "longitude" : msg.location.longitude
            }
        )

        user = db.select_user(telegram_id = msg.from_user.id)

        if user[3] == "uz":
            await msg.answer("Huquqbuzarlik tavsifi fotosurat\nEslatma! Agar sizda huquqbuzar haqida ma'lumot bo‘lsa, iltimos, u xaqidagi ma'lumotlarini yuboring (foto, kontakt, video) ", reply_markup=ReplyKeyboardRemove())
        else:
            await msg.answer("Описание правонарушения фотография\nПримечание! Если у Вас есть информация о правонарушителе, просим отправить его данные (фото, контакт, видео)", reply_markup=ReplyKeyboardRemove())
    
    await state.set_state(RegisterPage.mediaViolation)

@dp.message(F.video  | F.photo | F.document, RegisterPage.mediaViolation)
async def get_location_state(msg: types.Message, state: FSMContext):
    
    data = await state.get_data()
    count = int(db.count_complaints()[0])
    pstid= count+1
    province = int(str(data['provice']).replace("proviceuz:", ""))
    btn = InlineKeyboardBuilder()
    btn.button(text="Ko'rib chiqilmoqda", callback_data=f"statusUpdate:{pstid}")
    btn.button(text="❌Bekor qilish", callback_data=f"cancelAriza:{pstid}")
    btn.button(text="Ariza joylashuvi", callback_data=f"getLocation:{pstid}")
    btn.button(text="✅Ariza tasdiqlash", callback_data=f"arizaTasdiqlah:{pstid}")
    btn.adjust(2)

    mediaContent = msg.message_id

    await bot.copy_message(chat_id=channel_id, 
                            from_chat_id=msg.from_user.id, 
                            message_id=mediaContent, 
                            caption=f"🆔Id: {pstid}\n👤Arizachi:{data['fullname']}\n📄Ariza qabul qilindi: {pstid}\n🌏Murojaat: {regionsdict[data['region']]} {provincedict[data['region']][province]}\n📞Tel {data['phone']}\n⛓Qoidabuzarlik turi {extract_numbers(data['typeViolation'])}",
                            reply_markup=btn.as_markup())
    
    user = db.select_user(telegram_id = msg.from_user.id)
    
    db.add_complaint(post_id=pstid, user_id=msg.from_user.id, 
                     region=regionsdict[data['region']], district=provincedict[data['region']][province], 
                     description=mediaContent,
                     latitude=data["latitude"],
                     longitude=data["longitude"],
                     phone=data['phone'],
                     status="wait")
    
    if user[3] == "uz":
        full = f"📄Ariza qabul qilindi: {pstid}\n🌏Murojaat: {regionsdict[data['region']]} {provincedict[data['region']][province]}\n📞Tel {data['phone']}"
        await msg.answer(full, reply_markup=menuuz)
    else:
        full = f"📄ваша заявка принята: {pstid}\n🌏Обращаться: {regionsdict[data['region']]} {provincedict[data['region']][province]}\n📞Тел. {data['phone']}"
        await msg.answer(full, reply_markup=menuru)

    await state.clear()
