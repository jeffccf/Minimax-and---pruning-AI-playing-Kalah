# Minimax-and-alpha-beta-pruning-AI-playing-Kalah

Kalah is a two player game, each player has 6 holes and a kalah, the stones in the kalah are the score for the player.
In the beginning, there are 6 stones in each holes (not kalah).
Two players take turn to pick a hole with stone(s) and take all the stones from the hole and put those stones in the following holes (or kalahs).

There are some special rules, first, if the last stone is placed on the player's kalah, the player gets an extra round.
Second, if the last stone ends in the player's empty hole, the player can take that stone and all the stones from the opponent's direct hole to the player's kalah.
Third, if one player has no stones in all of his/her holes, the other player can put all the stones in the hole to its own kalah.

When both players has no stones in their holes, the game ends and whoever has more stones in his/her kalh wins.
If a player possesses more than 36 stones in his/her kalah, the game ends and the player wins, it is not necessary to play until both players empty their holes.

The goal of this ai is to play kalah. For each round, the ai has to choose a hole with stone(s). The ai implements minimax with alpha beta pruning. The pruning part can reduce the time the ai needs to return a value.

The difference between different AIs using minimax algorithm is the design of heuristic function. 
I take the following thing in account. First, the stones in the kalah, this represents the score of the game so I gave it a high weight. 
Second, if some holes can give a player another round, the heuristic could also get a higher score. 
Lastly, count the stones in the players hole, I gave this a small weight since having more stones doesn't necessary mean advantage.
