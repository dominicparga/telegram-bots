if __name__ == '__main__':
    from os import environ as env
    import telegram

    pargabot = telegram.Bot(env['PARGABOT_TOKEN'])
    endgameingbot = telegram.Bot(env['ENDGAMEINGBOT_TOKEN'])

    pargabot.set_webhook_root(env['WEBHOOK_NGROK'])
    endgameingbot.set_webhook_root(env['WEBHOOK_NGROK'])

    print(f'pargabot.webhook      = {pargabot.webhook}')
    print(f'endgameingbot.webhook = {endgameingbot.webhook}')
