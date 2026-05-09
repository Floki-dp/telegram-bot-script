import asyncio
import os

asyncio.set_event_loop(asyncio.new_event_loop())

from pyrogram import Client, filters



from pyrogram import Client, filters
import asyncio

API_ID = введите свой Айди 
API_HASH = "введите свой апи хаш  "

service_endpoints = ["введите сюда юзернейм своего бота без @", "введите сюда юзернейм своего бота без @",  "введите сюда юзернейм своего бота без @"]

app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.command("find", prefixes=".") & filters.me)
async def find_me(client, message):
    if len(message.command) < 2:
        return await message.edit("СТОП МНЕ ПРИЯТНО")


    query = message.command[1]
    await message.edit(f"🔍 Ищу инфу по: {query}")

    for bot in service_endpoints:
        await client.send_message(bot, query)
        await asyncio.sleep(15)

app.run()
