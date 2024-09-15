from IYIusic.core.bot import AMBOT
from IYIusic.core.dir import dirr
from IYIusic.core.git import git
from IYIusic.core.userbot import Userbot
from IYIusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = AMBOT()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
