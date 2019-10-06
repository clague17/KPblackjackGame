# KPblackjackGame

### How to run:

Clone github repo:

```sh
$ git clone https://github.com/clague17/KPblackjackGame.git
```

```sh
$ cd <path/to/repo>/KPblackjackGame
$ python playGame.py
```

Run the file playGame.py in your terminal. The imports to that file should be handled without a problem. Then follow the onscreen text prompts precisely as they are written in order to have an enjoyable experience! Have fun and try not to lose too much money playing BlackJack.

### Tooling and Rationale

I created my project in Python2, and used the time and random libraries to implement delays and generate pseudo random draws from the deck of cards. My reasoning behind using python is that it is a fast-development scripting language that I could use to easily make a file that can be run from the terminal.

### High level structure

Game Object

- Uses Player object (List of players attribute)
- Uses Card Object (card attribute)
- Has a score attribute
- Has a money attribute
- Has a name attribute
- Uses Deck object (A standard 52 card deck)
- Has a dealer attribute (a player object)

I created the Game object in a way such that each turn is effectively modular. That is, the Game is broken down into three “steps”: theBet, theDeal, and thePlay.

##### TheBet

In theBet, each player in the game.players attribute goes around betting on this round and locks in initial bets.

##### TheDeal

In theDeal, the initial deck shuffle and first round dealing occurs.

##### thePlay

In thePlay, the actual blackjack logic such as hitMe, raise, check, bust, dealerPlays are all implemented.

My implementation allows for many turns to be played as well as multiplayer addition and removal as the rounds progress. I did address the edge case where a player runs out of money and necessarily has to leave the table (theGame).

#### Note

I did not effectively handle all possible edge cases, and in the case where the user deviates even slightly from the requested input prompts, the rest of the program can and probably will fail. I prioritized making the foundation of the game well organized and modular rather than specifically addressing each possible edge case in the 3 hours suggested time. With more time, I would increase the robustness of this small app, as well as add intensive testing.
