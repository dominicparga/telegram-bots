_branch=${1:-develop}

# update pipenv
pipenv clean
pipenv install -e "git+https://github.com/dominicparga/telegram-bot-api.git@${_branch}#egg=telegram"
pipenv lock
pipenv sync

# update requirements.txt for heroku
pipenv lock -r > requirements.txt
pipenv lock -r -d > dev-requirements.txt
