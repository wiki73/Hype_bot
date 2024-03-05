from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='1'), KeyboardButton(text='2')],
    [KeyboardButton(text='3'), KeyboardButton(text='4')]],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню...'
)
inline = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='кнопка', url='')]
])
# команда 2 советы
#советы делятся на м ж общ
#дальше на советы по теме
#+ добавить кномпу назад
# команда 4 именна хайпологов
