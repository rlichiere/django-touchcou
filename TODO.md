# Todo

* Protect views with LoginRequiredMixin
* User
  * Profile page
  * integrate Game prepare modal
  * integrate Game board page
  * Autolog anonymous players when creating/joining a game
* GameLogic API (methods should be added to Game model)
  * `createGame`
    * Description
      * Called when a player create a game
      * Create a Game according to game creation form data
    * Parameters
      * `game_name`: name of the game to create
      * `game_genre`: genre of the game to create
      * `game_creator`: user who creates the game
    * Returns
      * the created game object
  * `playerRegister`
    * Description
      * Called when a player enters a game
      * Registers player to the game according with choosen side
    * Parameters
      * `player`: user.id of player
      * `side`: side choosen by the player (actually first or secont letter of Game.genre)
    * Returns
      * ...
  * `playerPrepare`
    * Description
      * Called when a player sends his preparation data
      * Validates and stores player preparation data
    * Parameters
      * `player`: user.id of player
      * `preparation_data`: list of Media/Zone couples
    * Returns
      * ...
  * `playerTouches`
    * Description
      * Called when a player touches the other one
      * Validates and process player's touch
    * Parameters
      * `player`: user.id of player
      * `media`: player's media choosen to perform the touch
      * `zone`: other person's zone choosen by player to perform the touch
    * Returns
      * ...
