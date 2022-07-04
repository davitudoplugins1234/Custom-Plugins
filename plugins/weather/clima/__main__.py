from pyrogram.errors import YouBlockedUser

from userge import Message, userge

@userge.on_cmd(
    "clima",
    about={
        "header": "Weather of the city",
        "description": "Busque o clima para uma determinada cidade.",
        "usage": "{tr}clima [text]",
    },
)
async def weather(message: Message):
    city_ = m.input_str
    bot_ = "@WhiterKangBOT"
    async with userge.conversation(bot_, timeout=1000) as conv:
        try:
            await conv.send_message(f"!clima {city_}")
        except YouBlockedUser:
            await message.reply("Por Favor desbloqueie a @WhiterKangBOT")
            return
        response = await conv.get_response(mark_read=False)
        await message.edit(response.text)
               
