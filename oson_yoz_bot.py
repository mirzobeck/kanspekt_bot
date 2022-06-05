import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from PIL import ImageDraw, Image, ImageFont
import os



logging.basicConfig(level=logging.INFO)

button = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton('Bot_haqida')]
    ], resize_keyboard=True
)


bot = Bot("5175989981:AAEo5utYZ7tL_U57-rzKgNkseIzaTfLcM54")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(massage: types.Message):
    try:
        user = massage.from_user.first_name
        user_name = massage.from_user.username
        idd = massage.from_user.id
        with open('E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/data.txt', 'r') as file:
            members = file.read()
        if str(idd) not in members:
            with open('E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/data.txt', 'a') as file:
                file.write(str(f'Firstname: {user}    Username:{user_name}    Id: {idd}\n'))
        await massage.answer(f"Assalomu aleykum <b>{user}</b>, Bot'ga xush kelebsiz!\nBot haqida ma'lumot 👇🏻", reply_markup=button, parse_mode='html')
    except:
        await massage.answer("Telegramdagi firstnameingizni lotin harflarida yozib qayta urining!")


@dp.message_handler(text='Bot_haqida')
async def help(massage: types.Message):
    await massage.answer("Bu botda siz har qanday so'zni oson hamda tez yoza olasiz.\nBotni ishlatish uchun matiningizni yozib yuboring va Bot sizga uni rasm korinishida yuboradi.\n<b>Eslatma:</b> Bot faqat lotin alifosi uchun!\nMurojat uchun: <a href='https://t.me/Mirzobek_Sobirov'>Mirzobek</a>", parse_mode='html', disable_web_page_preview=True)

@dp.message_handler(content_types=['photo', 'audio', 'video', 'sticker', 'emoj'])
async def get_audio(message: types.Message):
    await message.answer("Bizga faqat matn yuboring!")


@dp.message_handler()
async def yoz(massage: types.Message):
    s = ""
    cnt = 0
    for i in massage.text:
        s += i
        if i == "\n":
            cnt = 0
        cnt += 1
        if cnt>=55:
            if i == 'a' or i == 'i' or i == 'o' or i == 'u' or i == "o'" or i == 'u' or i == ' ':
                s += '-\n'
                cnt = 0
    img = Image.open('E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/bett.jpg')
    draw = ImageDraw.Draw(img)
    f = ImageFont.truetype("E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/Reality Shift Regular/Reality Shift Regular.ttf",47)
    draw.text((10, 62),s, (10,10,100),f,None,11.15)
    img.save('E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/new.png')
    await massage.answer_photo(photo=open('E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/new.png', 'rb'),caption="Bizni tanlaganingiz uchun rahmat.\n\n😎Botning egasi: <a href='https://t.me/Mirzobek_Sobirov'><b>Sobirov Mirzobek</b></a>", parse_mode='html')
    os.remove(os.path.join('E:/NG/Mirzobek_py/Botlar/oson_yoz_bot/new.png'))


    



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)