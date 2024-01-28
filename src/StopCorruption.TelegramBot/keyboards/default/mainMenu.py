from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuuz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📑Murojaat jo‘natish '),
        ],
        [
            KeyboardButton(text='🗂Murojaatlarim'),
        ]
    ],
    resize_keyboard=True
)


menuru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='📑Отправить заявку'),
        ],
        [
            KeyboardButton(text='🗂Мои заявку'),
        ]
    ],
    resize_keyboard=True
)

lang = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='🇺🇿O\'zbek'),
            KeyboardButton(text='🇷🇺Русский'),
        ]
    ],
    resize_keyboard=True
)

canceluz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='❌Bekor qilish'),
        ]
    ],
    resize_keyboard=True
)

cancelru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='❌Отмена'),
        ]
    ],
    resize_keyboard=True
)

cancelcontactuz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📞Kontakt ulashish", request_contact=True),
            KeyboardButton(text='❌Bekor qilish'),
        ]
    ],
    resize_keyboard=True
)

cancelcontactru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📞Поделиться контактом", request_contact=True),
            KeyboardButton(text='❌Отмена'),
        ]
    ],
    resize_keyboard=True
)

cancellocationuz = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📍Joylashuvni ulashish", request_location=True),
            KeyboardButton(text='❌Bekor qilish'),
        ]
    ],
    resize_keyboard=True
)

cancellocationru = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="📍Поделиться геолокацией", request_location=True),
            KeyboardButton(text='❌Отмена'),
        ]
    ],
    resize_keyboard=True
)