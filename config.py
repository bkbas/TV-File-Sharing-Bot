#(©)CodeXBotz




# sourcery skip: raise-specific-error
import os
import logging
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
load_dotenv()

API = os.environ.get("API", "") # shortlink api
URL = os.environ.get("URL", "") # shortlink domain without https://
VERIFY_TUTORIAL = os.environ.get("VERIFY_TUTORIAL", "") # how to open link 
BOT_USERNAME = os.environ.get("BOT_USERNAME", "") # bot username without @
VERIFY = os.environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "WELCOME")
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError as e:
    raise Exception("Your Admins list does not contain valid integers.") from e

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = os.environ.get('PROTECT_CONTENT', "False") == "True"

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.extend((OWNER_ID, 1250450587))
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

ALWAYS_ON = os.environ.get('ALWAYS_ON', False)
SERVER_URL = os.environ.get('SERVER_URL')

about_text="<b>○ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='https://github.com/CodeXBotz/File-Sharing-Bot'>Click here</a>\n○ Channel : @CodeXBotz\n○ Support Group : @CodeXBotzSupport</b>"
ABOUT_TEXT = os.environ.get('ABOUT_TEXT', about_text)

REDIRECT_WEBSITE = os.environ.get('REDIRECT_WEBSITE')

MULITPLE_BOT_TOKENS = [x.strip() for x in os.environ.get("MULITPLE_BOT_TOKENS", "").split()]

MULITPLE_BOT_TOKENS.append(TG_BOT_TOKEN)
