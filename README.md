# telegram-bots

These bots are deployed at `heroku`, where only one so-called `dyno` is for free.
Hence one backend is used for all my bots.

## local testing

1. First of all, __update pipenv__ and __start the local heroku server__.

   ```zsh
   # update pipenv
   source ./utils/prepare_deployment.sh "<telegram-bot-api branch>"

    # start local heroku server
    pipenv run heroku local
   ```

2. Then make the local heroku server available via `ngrok`:

   ```zsh
   ngrok http 5000
   ```

3. Update the telegram bots' webhooks __using environment variables__.
   `pipenv` is used for the right environment variables, which can be set in a local `.env` file.

   ```zsh
   # update webhook in .env

   pipenv run python utils/set_webhook_to_ngrok.py
   ```

## deploying to heroku

1. __Update pipenv__ using the following script.

   ```zsh
   # update pipenv
   source ./utils/prepare_deployment.sh "master"
   ```

2. __Set the webhook to heroku__, not to `ngrok`.

   ```zsh
   pipenv run python utils/set_webhook_to_heroku.py
   ```

3. __Push to master__ since heroku automatically deploys from github.

## TODO

- clean up utils script
