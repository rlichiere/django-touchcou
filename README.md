# django-touchcou
**touché-coulé** game based on **Django** framework.


# Game status sequence :

1. waiting_registrations_opening
1. waiting_players
1. waiting_game_launch
1. waiting_player_input
1. processing_player_input
   1. if player_wins -> player_wins
   1. else -> waiting_player_input (next_player)
1. player_wins
1. closed
