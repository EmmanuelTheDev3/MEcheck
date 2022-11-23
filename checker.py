import logging
import json
import asyncio
from datetime import datetime
import requests

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token='$$$$$$')
dp = Dispatcher(bot)



@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.answer(f'Привет! Этот бот отслеживает цену 5 самых дешёвых "Genesis Genopets Habitats" на Magic Eden.\n\nЧтобы получать цены каждый час - напиши /onehour\nЧтобы получит уведомление, когда цена упадёт ниже 15 Sol - /15sol\nЧтобы узнать цену на данный момент - /checkprice', parse_mode=types.ParseMode.HTML)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)



@dp.message_handler(commands='checkprice')
async def cmd_checkprice(message: types.Message):
    with open('response.json', 'r') as j:
        response = json.load(j)
    price = []
    i = 0
    while i <= 5:
        price.append(response['results'][i]['price'])
        i += 1
    price.sort()
    await message.answer(f'5 самых дешёвых Habitats сейчас:\n1: {price[0]} sol\n2: {price[1]} sol\n3: {price[2]} sol\n4: {price[3]} sol\n5: {price[4]} sol', parse_mode=types.ParseMode.HTML)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)


@dp.message_handler(commands='onehour')
async def cmd_onehour(message: types.Message):
    await message.answer(f'Если вы хотите подписаться на рассылку - /onehour_on\nЕсли вы хотите отписаться от рассылки - /onehour_off', parse_mode=types.ParseMode.HTML)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)


@dp.message_handler(commands='onehour_on')
async def cmd_onehour_on(message: types.Message):
    with open('tg_id.json', 'r') as j:
        tg_id = json.load(j)
    if message.chat.id in tg_id:
        await message.answer(f'Вы уже подписаны', parse_mode=types.ParseMode.HTML)
    else:
        tg_id.append(message.chat.id)
        await message.answer(f'Поздравляю! Вы подписались на рассылку, чтобы отменить - /onehour_off', parse_mode=types.ParseMode.HTML)
        with open('tg_id.json', 'w') as js:
            json.dump(tg_id, js, indent=2)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)

@dp.message_handler(commands='onehour_off')
async def cmd_onehour_off(message: types.Message):
    with open('tg_id.json', 'r') as j:
        tg_id = json.load(j)
    if message.chat.id in tg_id:
        tg_id.remove(message.chat.id)
        with open('tg_id.json', 'w') as j:
            json.dump(tg_id, j, indent=2)
        await message.answer(f'Ты что уже уходишь?( Знай: я всегда буду ждать тебя. Просто напиши - /onehour_on', parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f'Не нашёл тебя в списке рассылки, чтобы подписаться - /onehour_on', parse_mode=types.ParseMode.HTML)
        with open('tg_id.json', 'w') as j:
            json.dump(tg_id, j, indent=2)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)


@dp.message_handler(commands='15sol')
async def cmd_15sol(message: types.Message):
    await message.answer(f'Если вы хотите подписаться на рассылку - /15sol_on\nЕсли вы хотите отписаться от рассылки - /15sol_off', parse_mode=types.ParseMode.HTML)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)



@dp.message_handler(commands='15sol_on')
async def cmd_15sol_on(message: types.Message):
    with open('tg_id_15sol.json', 'r') as j:
        tg_id_15sol = json.load(j)
    if message.chat.id in tg_id_15sol:
        await message.answer(f'Вы уже подписаны', parse_mode=types.ParseMode.HTML)
    else:
        tg_id_15sol.append(message.chat.id)
        await message.answer(f'Поздравляю! Вы подписались на рассылку, чтобы отменить - /15sol_off', parse_mode=types.ParseMode.HTML)
        with open('tg_id_15sol.json', 'w') as js:
            json.dump(tg_id_15sol, js, indent=2)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)



@dp.message_handler(commands='15sol_off')
async def cmd_15sol_off(message: types.Message):
    with open('tg_id_15sol.json', 'r') as j:
        tg_id_15sol = json.load(j)
    if message.chat.id in tg_id_15sol:
        tg_id_15sol.remove(message.chat.id)
        with open('tg_id_15sol.json', 'w') as j:
            json.dump(tg_id_15sol, j, indent=2)
        await message.answer(f'Ты что уже уходишь?( Знай: я всегда буду ждать тебя. Просто напиши - /15sol_on', parse_mode=types.ParseMode.HTML)
    else:
        await message.answer(f'Не нашёл тебя в списке рассылки, чтобы подписаться - /15sol_on', parse_mode=types.ParseMode.HTML)
        with open('tg_id_15sol.json', 'w') as j:
            json.dump(tg_id_15sol, j, indent=2)
    with open('tg_usrnme.json', 'r') as js:
        tg_usrnme = json.load(js)
    if message.chat.username in tg_usrnme:
        pass
    else:
        tg_usrnme.append(message.chat.username)
        await bot.send_message($$$$$$, f'Поздравляю! Новый человечек @{message.chat.username}', parse_mode=types.ParseMode.HTML)
        with open('tg_usrnme.json', 'w') as j:
            json.dump(tg_usrnme, j, indent=2)

async def mailing(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        with open('tg_id.json', 'r') as j:
            tg_id = json.load(j)
        with open('response.json', 'r') as j:
            response = json.load(j)
        price = []
        i = 0
        while i <= 5:
            price.append(response['results'][i]['price'])
            i += 1
        price.sort()
        i = 0
        while i < len(tg_id):
            try:
                await bot.send_message(tg_id[i], f'5 самых дешёвых Habitats сейчас:\n1: {price[0]} sol\n2: {price[1]} sol\n3: {price[2]} sol\n4: {price[3]} sol\n5: {price[4]} sol\n\nЧтобы отписаться от рассылки - /onehour_off', parse_mode=types.ParseMode.HTML)
            except Exception as ex:
                await bot.send_message($$$$$$, f'{tg_id[i]} кинул в чс', parse_mode=types.ParseMode.HTML)
                with open('tg_id.json', 'r') as j:
                    tg_id = json.load(j)
                tg_id.remove(tg_id[i])
                with open('tg_id.json', 'w') as j:
                    json.dump(tg_id, j, indent=2)
            i += 1




async def mailing_15(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        with open('tg_id_15sol.json', 'r') as j:
            tg_id_15sol = json.load(j)
        with open('response.json', 'r') as j:
            response = json.load(j)
            price = []
        n = 0
        while n <= 2:
            price.append(response['results'][n]['price'])
            n += 1
        price.sort()
        i = 0
        if price[0] <= 15:
            while i < len(tg_id_15sol):
                try:
                    await bot.send_message(tg_id_15sol[i], f'САМЫЙ ДЕШЁВЫЙ ХАБИТАТ СЕЙЧАС СТОИТ {price[0]} sol\n\nЧтобы отписаться от рассылки - /15sol_off', parse_mode=types.ParseMode.HTML)
                except Exception as ex:
                    await bot.send_message($$$$$$, f'{tg_id_15sol[i]} кинул в чс', parse_mode=types.ParseMode.HTML)
                    with open('tg_id_15sol.json', 'r') as j:
                        tg_id_15sol = json.load(j)
                    tg_id_15sol.remove(tg_id_15sol[i])
                    with open('tg_id_15sol.json', 'w') as j:
                        json.dump(tg_id_15sol, j, indent=2)
                i += 1
            await asyncio.sleep(600)
        else:
            pass


async def parser(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        try:
            response = requests.get(
                'https://api-mainnet.magiceden.dev/rpc/getListedNFTsByQuery?q={%22$match%22:{%22collectionSymbol%22:%22genesis_genopets_habitats%22},%22$sort%22:{%22takerAmount%22:1},%22$skip%22:0,%22$limit%22:20,%22status%22:[]}')
            with open('response.json', "w") as f:
                f.write(response.text)
        except Exception as ex:
            with open("Error.txt", "w") as f:
                f.write(str(ex))

if name == 'main':
    loop = asyncio.get_event_loop()
    loop.create_task(mailing(3596))
    loop.create_task(parser(5))
    loop.create_task(mailing_15(5))
    executor.start_polling(dp, skip_updates=True)
