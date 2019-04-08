'''
This Telegram bot serves by doing all kind of random stuff.
'''

from flask import Flask

# blueprints / bots
from telegram_bots import pargabot, endgameingbot

app = Flask(__name__)

app.register_blueprint(pargabot.blueprint)
app.register_blueprint(endgameingbot.blueprint)
# app.register_blueprint(
    # endgameingbot.blueprint,
    # url_prefix=f'/{endgameingbot.bot.token}'
# )
