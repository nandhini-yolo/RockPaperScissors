
# Rock Paper Scissor Game:

It is a hand game played between two players. Each players simultanously show a
hand signal rock, scissors or paper.  

Rules followed:
- Rock crushes Scissors => Rock wins
- Scissors cuts Paper => Scissors wins
- Paper wraps Rock => Paper wins

Based on the above rules, winner get 1 point. Both player pick the same hand signal,
then it is tie. Whoever scores maximum points at the end of n rounds is the winner.

## Design Process

Initially, I started of with monolithic structure and functional programming to implement the game
to understand the different functionality of game. Once, I got the overall picture, I changed to 
Object oriented design. so, if we want to changes/extend any feature, it can be easily done.

- At first, we implemented the 



## How to play

Clone the repository
git clone https://github.com/nandhini-yolo/RockPaperScissors.git

Add the repo to PYTHONPATH
setenv PYTHONPATH TOP_DIR/src/lib/python:$PYTHONPATH

Start the game 
TOP_DIR/src/appl/rock_paper_scissor_game.py 


## Possible extensions

Some of the possible extensions I thought of and considered while designing the system

1. Instead of just three hand signals, we can easily extend this game to include more hand signals.
We can support this by extending the RPSRules and HandSignals class and overriding the compare function

2. Playing the game between two human user. This requires only minor change in 
rock_paper_scissor_game. The required changes were cleared described in the inline comments

3. Two player over the network, This also we can easily set up by launching the game in the server
and player can connect to the game server, share his chose & communicate with the server over a 
reliable TCP connection.

4. Right now, Computer picks the hand signals randomly. Instead, We can persist the choices made by the opponent 
and its choices as well over history. Then, Computer can analysis the frequency of player choices to maximize the possible wins.



