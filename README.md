# django-touchcou
A naughty **touché-coulé** game based on **Django** framework

## Technology stack
* Python 3
* Django 2.0
* MySQL

# Deployment instructions

## First build

1. Install Python 3
1. Install Git bash
1. Create virtual environment in project folder
   1. **TODO**
1. Pull django repository in project folder
   1. `git clone https://github.com/rlichiere/django-touchcou.git`
1. Launch virtual environment
   * Linux:
      1. **TODO**
   * Windows:
      1. `myvenv\Scripts\activate`
1. Install project requirements
   1. `pip install -r requirements.txt`
1. Set application configuration:
   1. In `touchcou/config` copy `config_model.yml` to `config_private.yml`
   1. Adapt `config_private.yml` parameters to your convenience
1. Create superuser
   1. Move to django app
      1. `cd touchcou`
   1. Create superuser account
      1. python manage.py createsuperuser --username {ADMIN_USER} --email {ADMIN_EMAIL}
         * Reply to prompt with a passowrd longer than 8 letters

## Execution

1. Open a terminal
1. Move to project folder:
   * Linux:
      1. `cd /{PROJECT_PATH}`
   * Windows:
      1. `{PROJECT_VOLUME_LETTER}:`
      1. `cd {PROJECT_PATH}`
1. Launch virtual environment (see above)
   * Linux:
      1. **TODO**
   * Windows:
      1. `myvenv\Scripts\activate`
1. Start Django application
   * PyCharm:
      1. `Run > Run 'touchcou'`

## Maintenance

**TODO**

# Game status sequence

Every Game will follow the sequence below:
1. `WAITING_REGISTRATIONS_OPENING`
   1. waits until the planned date for the opening of registrations
   1. if not date is planned, takes the next step
1. `WAITING_PLAYERS`
   1. waits until every participation slot is filled by a player
1. `WAITING_GAME_LAUNCH`
1. `WAITING_PLAYER_INPUT`
1. `PROCESSING_PLAYER_INPUT`
   1. if player_wins -> player_wins
   1. else -> waiting_player_input (next_player)
1. `PLAYER_WINS`
1. `FINISHED`

# Documentation

## Main features

* Game creation
  * `name`: name of the game
  * `genre`: genre of game
    * `HF`: man and woman
    * `FH`: woman and man
    * `HH`: man and man
    * `FF`: woman and woman
  * `creator`
    * Anonymous users must enter a player name
