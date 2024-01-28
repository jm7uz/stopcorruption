from aiogram.filters.state import State,StatesGroup

class LoginPage(StatesGroup):
    lang = State()
    login = State()
    password = State()