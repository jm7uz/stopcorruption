from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


regionsuz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Andijon viloyati",callback_data="andijonuz"),
            InlineKeyboardButton(text="Farg‘ona viloyati",callback_data="fargonauz"),
        ],
        [
            InlineKeyboardButton(text="Namangan viloyati",callback_data="namanganuz"),
            InlineKeyboardButton(text="Toshkent viloyati",callback_data="toshkentviluz"),
        ],
        [
            InlineKeyboardButton(text="Toshkent shahri",callback_data="toshkentshuz"),
            InlineKeyboardButton(text="Surxondaryo viloyati",callback_data="surxondaryouz"),
        ],
        [
            InlineKeyboardButton(text="Samarqand viloyati",callback_data="samarqanduz"),
            InlineKeyboardButton(text="Buxoro viloyati",callback_data="buxorouz"),
        ],
        [
            InlineKeyboardButton(text="Sirdaryo viloyati",callback_data="sirdaryouz"),
            InlineKeyboardButton(text="Xorazm viloyati",callback_data="xorazmuz"),
        ],
        [
            InlineKeyboardButton(text="Qashqadaryo viloyati",callback_data="qashqadaryouz"),
            InlineKeyboardButton(text="Navoiy viloyati",callback_data="navoiyuz"),
        ],
        [
            InlineKeyboardButton(text="Qoraqalpog‘iston Respublikasi",callback_data="qoraqalpogistonuz"),
            InlineKeyboardButton(text="Jizzax viloyati",callback_data="jizzaxuz"),
        ],
        [
            InlineKeyboardButton(text="❌Bekor qilish",callback_data="canceluz"),
        ],
    ]
)


regionsru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Андижанская область",callback_data="andijonru"),
            InlineKeyboardButton(text="Ферганская область",callback_data="fargonaru"),
        ],
        [
            InlineKeyboardButton(text="Наманганская область",callback_data="namanganru"),
            InlineKeyboardButton(text="Ташкентская область",callback_data="toshkentvilru"),
        ],
        [
            InlineKeyboardButton(text="город Ташкент",callback_data="toshkentshru"),
            InlineKeyboardButton(text="Сурхандарьинская область",callback_data="surxondaryoru"),
        ],
        [
            InlineKeyboardButton(text="Самаркандская область",callback_data="samarqandru"),
            InlineKeyboardButton(text="Бухарская область",callback_data="buxororu"),
        ],
        [
            InlineKeyboardButton(text="Сырдарьинская область",callback_data="sirdaryoru"),
            InlineKeyboardButton(text="Хорезмская область",callback_data="xorazmru"),
        ],
        [
            InlineKeyboardButton(text="Кашкадарьинская область",callback_data="qashqadaryoru"),
            InlineKeyboardButton(text="Навоийская область",callback_data="navoiyru"),
        ],
        [
            InlineKeyboardButton(text="Республика Каракалпакстан",callback_data="qoraqalpogistonru"),
            InlineKeyboardButton(text="Джизакская область",callback_data="jizzaxru"),
        ],
        [
            InlineKeyboardButton(text="❌Отмена",callback_data="cancelru"),
        ],
    ]
)