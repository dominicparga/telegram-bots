from os import environ as env

from flask import request, Blueprint
import telegram

blueprint = Blueprint('endgameingbot', __name__)
bot = telegram.Bot(env['ENDGAMEINGBOT_TOKEN'])

@blueprint.route(f'/{bot.token}', methods=['POST'])
def receive_msg():
    resp = request.get_json()
    if 'message' in resp:
        to = resp['message']['from']['id']
        msg = resp['message']['text']
        bot.send_msg(msg, to)

    return 'ok!', 200
