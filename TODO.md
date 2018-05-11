# Todo

* Protect views with LoginRequiredMixin
* User
  * Profile page
  * integrate Game prepare modal
  * integrate Game board page
  * Autolog anonymous players when creating/joining a game
* GameLogic API
  * playerRegister
    * Description
      * Called when a player enters a game.
      * Registers player to the game according with choosen side.
    * Params
      * player : user.id of player
      * side : side choosen by the player (actually first or secont letter of Game.genre)
    * Returns
      * a
  * playerPrepare (player, preparation_data) : called when a player sends his preparation data
  * playerTouches (player, media, zone)      : called when a player touches the other one

## Define

