# drunk_bot
Discord Bot for the boys drinking habits

Run bot_core.py locally after connecting the bot to your discord server.
Make user to update client ID and permissions in bot_command_logic.py

Bot command prefix = '!'

Games currently implimented. 
Powerhour:
  Callable via !powerhour start
  Optional Arugment of a positive INT for how long you want the game to run default 60 minutes
  Can end the game via !powerhour end at any point
  Rules:
    Drink a shot's worth of beer every minute when the bot says drink,
    Try not to puke

King's Cup:
  Callable via !kingscup pull
  Default for arg is pull so !kingscup will do the same function as above
  As long as the bot is in the chat the game will remain persistent,
  you can reset the game via !kingscup reset or !kingscup restart.
  This will create and shuffle a new deck, a new deck is automatically made when 
  the game is lost.
  Rules:
    Every person who wants to play will pull a card and the card will have a rule,
    The rule will be displayed in chat and the person that fails to comply with the rule 
    or is addressed in the rule has to take a drink. 
    The card is removed from the deck and there is a chance of breaking the imagary circle 
    which prompts a drink but does not end the game. The card is then insereted into an imagary
    can (like the real life game) and has a random chance to pop the can. Both of these will be 
    more common the more cards removed and chances reset with new decks.
    If the 'beer' is popped then that player must finish their drink and the bot will reset the game
