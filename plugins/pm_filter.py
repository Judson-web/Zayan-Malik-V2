#Kanged From @TroJanZheX
from info import AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, API_KEY, AUTH_GROUPS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
import re
import random
from pyrogram.errors import UserNotParticipant
from utils import get_filter_results, get_file_details, is_subscribed, get_poster
BUTTONS = {}
BOT = {}


RATING = ["5.1 | IMDB", "6.2 | IMDB", "7.3 | IMDB", "8.4 | IMDB", "9.5 | IMDB", ]
GENRES = ["fun, fact",
          "Thriller, Comedy",
          "Drama, Comedy",
          "Family, Drama",
          "Action, Adventure",
          "Film Noir",
          "Documentary"]

@Client.on_message(filters.text & filters.private & filters.incoming & filters.user(AUTH_USERS) if AUTH_USERS else filters.text & filters.private & filters.incoming)
async def filter(client, message):
    if message.text.startswith("/"):
        return
    if AUTH_CHANNEL:
        invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        try:
            user = await client.get_chat_member(int(AUTH_CHANNEL), message.from_user.id)
            if user.status == "kicked":
                await client.send_message(
                    chat_id=message.from_user.id,
                    text="Sorry Sir, You are Banned to use me.",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await client.send_message(
                chat_id=message.from_user.id,
                text="**🖤𝐉𝐨𝐢𝐧 𝐌𝐲 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐭𝐨 𝐮𝐬𝐞 𝐌𝐞!💜**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("💙𝙅𝙊𝙄𝙉 𝙈𝙔 𝙐𝙋𝘿𝘼𝙏𝙀 𝘾𝙃𝘼𝙉𝙉𝙀𝙇🧡", url=invite_link.invite_link)
                        ]
                    ]
                ),
                parse_mode="markdown"
            )
            return
        except Exception:
            await client.send_message(
                chat_id=message.from_user.id,
                text="Something went Wrong.",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 100:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"[{get_size(file.file_size)}] {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}",callback_data=f"subinps#{file_id}")]
                    )
        else:
            await client.send_sticker(chat_id=message.from_user.id, sticker='CAACAgIAAxkBAAEDELBhZcJbRyS-7uFM7eH3Aif0LmdI8wACwgIAAjZ2IA4AAQlbyvf7wx4hBA')
            return

        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="Gᴏ Tᴏ Nᴇxᴛ Pᴀɢᴇ 🚀",callback_data="pages")]
            )
            poster=None
            if API_KEY:
                poster=await get_poster(search)
            if poster:
                await message.reply_photo(photo=poster, caption=f"<b>Film/Series : {search}\n🌟 IMDB Rating : {random.choice(RATING)}\n🎭 Genres : {random.choice(GENRES)}\n©{message.chat.title}🍿</b>", reply_markup=InlineKeyboardMarkup(buttons))

            else:
                await message.reply_text(f"<b>Film/Series : {search}\n🌟 IMDB Rating : {random.choice(RATING)}\n🎭 Genres : {random.choice(GENRES)}\n©{message.chat.title}🍿</b>", reply_markup=InlineKeyboardMarkup(buttons))
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Gᴏ Tᴏ Nᴇxᴛ Pᴀɢᴇ 🚀",callback_data=f"next_0_{keyword}")]
        )
        buttons.append(    
            [InlineKeyboardButton(text=f"⭕ Pages 1/{data['total']}",callback_data="pages")]
        )
        poster=None
        if API_KEY:
            poster=await get_poster(search)
        if poster:
            await message.reply_photo(photo=poster, caption=f"<b>🎬 Film/Series : {search}\n🌟 Rating : {random.choice(RATING)}\n🎭 Genres : {random.choice(GENRES)}\n©{message.chat.title}🍿</b>", reply_markup=InlineKeyboardMarkup(buttons))
        else:
            await message.reply_text(f"<b><b>🎬 Film/Series : {search}\n🌟 Rating : {random.choice(RATING)}\n🎭 Genres : {random.choice(GENRES)}\n©{message.chat.title}🍿</b>", reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_message(filters.text & filters.group & filters.incoming & filters.chat(AUTH_GROUPS) if AUTH_GROUPS else filters.text & filters.group & filters.incoming)
async def group(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []

        search = message.text
        result_txt = f"<b>🎬 Film/Series : {search}\n🌟 Rating : {random.choice(RATING)}\n🎭 Genres : {random.choice(GENRES)}\n©{message.chat.title}🍿</b>"
        nyva=BOT.get("username")
        if not nyva:
            botusername=await client.get_me()
            nyva=botusername.username
            BOT["username"]=nyva
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                file_name = file.file_name
                file_size = get_size(file.file_size)
                file_link = f"https://telegram.dog/{nyva}?start=mickey_-_-_-_{file_id}"
                btn.append(
                    [
                      InlineKeyboardButton(text=f"{file_name}", url=f"{file_link}"),
                      InlineKeyboardButton(text=f"{file_size}", url=f"{file_link}")
                    ]
                )
        else:
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="Gᴏ Tᴏ Nᴇxᴛ Pᴀɢᴇ 🚀",callback_data="pages")]
            )
            poster=None
            if API_KEY:
                poster=await get_poster(search)
            if poster:
                await message.reply_photo(photo=poster, caption=result_txt, reply_markup=InlineKeyboardMarkup(buttons))
            else:
                await message.reply_text(result_txt, reply_markup=InlineKeyboardMarkup(buttons))
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Gᴏ Tᴏ Nᴇxᴛ Pᴀɢᴇ 🚀",callback_data=f"next_0_{keyword}")]
        )
        buttons.append(    
            [InlineKeyboardButton(text=f"⭕ Pages 1/{data['total']}",callback_data="pages")]
        )
        poster=None
        if API_KEY:
            poster=await get_poster(search)
        if poster:
            await message.reply_photo(photo=poster, caption=result_txt, reply_markup=InlineKeyboardMarkup(buttons))
        else:
            await message.reply_text(result_txt, reply_markup=InlineKeyboardMarkup(buttons))

    
def get_size(size):
    """Get size in readable format"""

    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units):
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]          



@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):

        if query.data.startswith("next"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("You are using this for one of my old message, please send the request again.",show_alert=True)
                return

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"⭕ Pages {int(index)+2}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"⭕ Pages {int(index)+2}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data.startswith("back"):
            ident, index, keyword = query.data.split("_")
            try:
                data = BUTTONS[keyword]
            except KeyError:
                await query.answer("Yᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴛʜɪs ғᴏʀ ᴏɴᴇ ᴏғ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇ 🥺, ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴛʜᴇ ʀᴇǫᴜᴇsᴛ ᴀɢᴀɪɴ😢.",show_alert=True)
                return

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"⭕ Pages {int(index)}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)-1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"⭕ Pages {int(index)}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data == "about":
            buttons = [
                [
                    InlineKeyboardButton('🔰 Oᗯᑎᗴᖇ 🔰', url='https://t.me/xxxtentacionn12'),
                    InlineKeyboardButton('🆂🅾️🆄🆁🅲🅴 🅲🅾️🅳🅴', callback_data="source")
                ]
                ]
            await query.message.edit(text="<b>ᴄʀᴇᴀᴛᴏʀ: <a href='https://t.me/xxxtentacionn12'>𝗚𝗛𝗢𝗦𝗧 𝗠𝗜𝗖𝗞𝗘𝗬</a>\nʟᴀɴɢᴜᴀɢᴇ : <code>ᴘʏᴛʜᴏɴ 3</code>\nʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>ᴘʏʀᴏɢʀᴀᴍ</a>\nsᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://github.com/Judson-web/Zayan-Malik-V2'>ᴄʟɪᴄᴋ ᴍᴇ 👈</a>\nᴅᴀᴛᴀ ʙᴀsᴇ : <a href='https://www.mongodb.com/cloud'>ᴍᴏɴɢᴏ ᴅʙ</a> </b>", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)


        elif query.data.startswith("subinps"):
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{files.file_name}"
                buttons = [
                    [
                        InlineKeyboardButton('🆂🅴🅰️🆁🅲🅷 🅰️🅶🅰️🅸🅽', switch_inline_query_current_chat=''),
                    ]
                    ]
                
                await query.answer()
                await client.send_cached_media(
                    chat_id=query.from_user.id,
                    file_id=file_id,
                    caption=f_caption,
                    reply_markup=InlineKeyboardMarkup(buttons)
                    )
        elif query.data.startswith("checksub"):
            if AUTH_CHANNEL and not await is_subscribed(client, query):
                await query.answer("Bruda I Like Your Smartness, But Don't Be Oversmart, Join Now 😎",show_alert=True)
                return
            ident, file_id = query.data.split("#")
            filedetails = await get_file_details(file_id)
            for files in filedetails:
                title = files.file_name
                size=files.file_size
                f_caption=files.caption
                if CUSTOM_FILE_CAPTION:
                    try:
                        f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
                    except Exception as e:
                        print(e)
                        f_caption=f_caption
                if f_caption is None:
                    f_caption = f"{title}"
                buttons = [
                    [
                        InlineKeyboardButton('🆂🅴🅰️🆁🅲🅷 🅰️🅶🅰️🅸🅽', switch_inline_query_current_chat=''),
                    ]
                    ]
                

        elif query.data == "pages":
            await query.answer("ഇത് നിനക്കുവേണ്ടി ഉള്ളതല്ല മോനെ, വിട്ടോളി😏",show_alert=True)

        elif query.data == "Next":
            await query.answer("ഇത് നിനക്കുവേണ്ടി ഉള്ളതല്ല മോനെ, വിട്ടോളി😏",show_alert=True)
        
        elif query.data == "source":
            await query.answer("സോഴ്സ് കോഡ് തർനെ എനിക്ക് മനസില്ല ഓണ് പോട അവൻ്റെ ഒരു സോഴ്സ് കോടെ phha",show_alert=True)
