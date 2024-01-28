from aiogram.filters.state import State,StatesGroup

class RegisterPage(StatesGroup):
    region = State()
    province = State()
    typeViolation = State()
    location = State()
    mediaViolation = State()

class CheckApplication(StatesGroup):
    appid = State()
    