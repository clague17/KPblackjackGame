# KPblackjackGame
Instructions for running my code:
Run the file playGame.py in your terminal. The imports to that file should be handled without a problem. Then follow the onscreen text prompts precisely as they are written in order to have an enjoyable experience! Have fun and try not to lose too much money playing BlackJack.

Choice of tooling and rationale:
I created my project in Python, and used the time and random libraries to implement delays and generate pseudo random draws from the deck of cards. My reasoning behind using python is that it is a fast-development scripting language that I could use to easily make a file that can be run from the terminal. I also chose it because I am most comfortable with that language, and I did not want to waste time creating a .tar file for perhaps a Java solution. While python isn’t the best language for Object Oriented programming, I made it work and it is usable for this solution.

High level Structure:

Game object:
Uses Player object (List of players attribute)
Uses Card Object (card attribute)
Has a score attribute
Has a money attribute
Has a name attribute
Uses Deck object (A standard 52 card deck)
Has a dealer attribute (a player object)

theBet:
Create a hashMap wagers that maps each player to their bet
theDeal
Take cards from the Deck object at random and

I created the Game object in a way such that each turn is effectively modular. That is, the Game is broken down into three “steps”: theBet, theDeal, and thePlay. In theBet, each player in the game.players attribute goes around betting on this round, then in theDeal, the dealing occurs, and finally in thePlay, the interesting part of the game actually happens. My implementation allows for many turns to be played as well as multiplayer addition and removal as the rounds progress. I did address the edge case where a player runs out of money and necessarily has to leave the table (theGame).

Note: I did not effectively handle all possible edge cases, and in the case where the user deviates even slightly from the requested input prompts, the rest of the program can and probably will inevitably fail. I prioritized making the foundation of the game scalable and well organized rather than specifically addressing each possible edge case in the 3 hours suggested time.
