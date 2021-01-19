# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1888337
API_HASH = "e0778ef35e3efdbcf39369cd53a99ad0"

# Get this from @Botfather
TOKEN = "1531286557:AAETgtNPP9VNu66d5YNR4UXCe2MGE0sqVbA"

# Your mongodb uri
MONGO_DB_URI = "mongo "mongodb+srv://cluster0.sqeyo.mongodb.net/vcpb" --username Hero"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1154075796,
    800024545,
    1021509576
]

# The ID of the group where your bot streams
GROUP = -1001491774644

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Send "now playing" messages to the group
LOG = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
