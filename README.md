<a href="https://en.wikipedia.org/wiki/Pikachu">
  <img src="https://telegra.ph/file/2b3571b5103e31b329469.jpg" alt="view">    
   


# [𝙋𝙄𝙆𝘼𝘾𝙃𝙐](http://t.me/CB_movieRobot)
  
  ![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Adv+Auto+Filter+bot+V2;Click+Deploy+to+Heroku+Button;By+Pikachu)

## Added Features
* Index channel or group files for inline search.
* Index command to index all the files in a given channel (No USER_SESSION Required).
* When you post file on telegram channel or group this bot will save that file in database, so you can search easily in inline mode.
* Supports document, video and audio file formats with caption support.
* Imdb posters for autofilter.
* Custom captions for your files.
* Support Auto-Filter (Both in PM and in Groups)
* Once files saved in Database , exists until you manually deletes. (No Worry if post gets deleted from source channel.)
* Added Force subscribe (Only channel subscribes can use the bot)
* Ability to restrict groups(AUTH_GROUPS)
  
## Installation

 ### Easy Way
-------------------
<html>
<body>

<details close>
  <summary>Heroku</summary>
  <p><p><a href="https://heroku.com/deploy?template=https://github.com/PeacefighterTG/PIKACHU-bot"><img src="https://img.shields.io/badge/Deploy%20Pikachu%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="300""/></a></p></p>
</details>

</body>
</html>

--------------------
  
### Hard Way
```bash
# Create virtual environment
python3 -m venv env

# Activate virtual environment
env\Scripts\activate.bat # For Windows
source env/bin/activate # For Linux or MacOS

# Install Packages
pip3 install -r requirements.txt

# Edit info.py with variables as given below then run bot
python3 bot.py
```
Check [`sample_info.py`](sample_info.py) before editing [`info.py`](info.py) file

### Docker
```
docker run -d \
    -e BOT_TOKEN="123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11" \
    -e API_ID='12345' \
    -e API_HASH='0123456789abcdef0123456789abcdef' \
    -e CHANNELS='-10012345678' \
    -e ADMINS='123456789' \
    -e DATABASE_URI="mongodb+srv://...mongodb.net/Database?retryWrites=true&w=majority" \
    -e DATABASE_NAME=databasename \
    --restart on-failure \
    --name mediasearchbot botxtg/media-search-bot
```
You can also run with `env` file like below,
```
docker run -d \ 
     --env-file .env \
     --restart on-failure \
     --name mediasearchbot botxtg/media-search-bot
```

## Variables
### Required Variables
* `BOT_TOKEN`: Create a bot using [@BotFather](https://telegram.dog/BotFather), and get the Telegram API token.
* `API_ID`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `API_HASH`: Get this value from [telegram.org](https://my.telegram.org/apps)
* `CHANNELS`: Username or ID of channel or group. Separate multiple IDs by space
* `ADMINS`: Username or ID of Admin. Separate multiple Admins by space
* `DATABASE_URI`: [mongoDB](https://www.mongodb.com) URI. Get this value from [mongoDB](https://www.mongodb.com).
* `DATABASE_NAME`: Name of the database in [mongoDB](https://www.mongodb.com). 

### Optional Variables
* `COLLECTION_NAME`: Name of the collections. Defaults to Telegram_files. If you going to use same database, then use different collection name for each bot
* `CACHE_TIME`: The maximum amount of time in seconds that the result of the inline query may be cached on the server
* `USE_CAPTION_FILTER`: Whether bot should use captions to improve search results. (True/False)
* `AUTH_USERS`: Username or ID of users to give access of inline search. Separate multiple users by space. Leave it empty if you don't want to restrict bot usage.
* `AUTH_CHANNEL`: Username or ID of channel. Without subscribing this channel users cannot use bot.
* `START_MSG`: Welcome message for start command.
* `INVITE_MSG`: Auth channel invitation message.
* `USERBOT_STRING_SESSION`: User bot string session From : https://replit.com/@JUD-FORFOR/DARK-LORD
    
## Note
* Currently [API used](http://www.omdbapi.com) here is allowing 1000 requests per day.You may not get posters if its crossed. 
Once a poster is fetched from OMDB , poster is saved to DB to reduce duplicate requests.
    
## Admin commands
```
channel - Get basic infomation about channels
total - Show total of saved files
delete - Delete file from database
index - Index all files from channel or group
logger - Get log file
```

## Tips
* Use `index` command or run [one_time_indexer.py](one_time_indexer.py) file to save old files in the database that are not indexed yet.
* You can use `|` to separate query and file type while searching for specific type of file. For example: `Avengers | video`
* If you don't want to create a channel or group, use your chat ID / username as the channel ID. When you send a file to a bot, it will be saved in the database.
    
## If Any Doubts Ask In [Support Group](telegram.me/STMbOTsUPPORTgROUP)

## Contributions
Contributions are welcome.

## Thanks to [Pyrogram](https://github.com/pyrogram/pyrogram)

## Contact Owner & Editor
[Editor](https://t.me/VAMPIRE_KING_NO_1) - [Owner](https://t.me/Peace_fighter_No1)

## License
Code released under [The GNU General Public License](LICENSE).
    
### Note
    
 Anyone Can Fork & Edite This Repo But Add Us In Credit 😊
