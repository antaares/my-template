from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# general menu
# # # # # #
login_page_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            # Statistika
            KeyboardButton(text="📊 Statistika"),
            # Xabar yuborish
            KeyboardButton(text="📨 Xabar yuborish"),
        ],
        [
            KeyboardButton(text="🎞 Kanallar")
        ]
    ],
    resize_keyboard=True
)

# general menu
# # # # # # 






# statistika

get_data_excel_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            # Excel fayl yuklash
            KeyboardButton(text="📥 Excel fayl yuklash"),
            ],
        [
            KeyboardButton(text="Bosh menu"), # back to main menu
        ]
    ],
    resize_keyboard=True
)








# broadcast

BACK = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)







CHOICE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Forward Message"),
            KeyboardButton(text="Copy Message")
        ],
        [
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)


CONFIRM = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Yuborish"),
            KeyboardButton(text="Bekor qilish")
        ]
    ],
    resize_keyboard=True
)


YES_NO = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ha"),
            KeyboardButton(text="Yo'q")
        ]
    ],
    resize_keyboard=True
)
# broadcast





# manage channels
# # # # # #
manage_channels_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kanal qo'shish"),
            KeyboardButton(text="Kanal o'chirish")
        ],
        [
            KeyboardButton(text="Kanallar ro'yxati"),
            KeyboardButton(text="Bosh menu")
        ]
    ],
    resize_keyboard=True
)


remove_button = ReplyKeyboardRemove()