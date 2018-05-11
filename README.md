# django-touchcou
**touché-coulé** game based on **Django** framework.


# Deployment instructions

## First build

1. Install project requirements
   pip install -r requirements




# Game status sequence

1. waiting_registrations_opening
1. waiting_players
1. waiting_game_launch
1. waiting_player_input
1. processing_player_input
   1. if player_wins -> player_wins
   1. else -> waiting_player_input (next_player)
1. player_wins
1. closed
