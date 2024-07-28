
# Rock Paper Scissor Game:

It is a hand game played between two players. Each player simultaneously shows a
hand signal: one of rock, scissors, or paper.  

Typical ruleset: Rock crushes Scissors, Scissors cuts Paper, Paper wraps Rock

- Based on these rules, winner gets 1 point every round. 
- In case of tie, no one gets a point.
- Whoever scores the maximum points at the end of N rounds is the winner.

## Design Process

Initially, to get an idea of the control flow and various functionalities, 
I started with a non-OOPS monolithic structure to implement the game.
Soon enough, I identified below entities:

- Game object: Started here where the main control loop would be present. 
  This object would give control to each player every turn and determine winner
  and keep count until N rounds are done.
  - It has the logic to decide winner given the two inputs.

- Classified the possible players into Computer and Human, and added them both 
  as subclasses to Player class. If we want to later change the logic of 
  choosing the signal by the computer based on the opponent history, we can 
  modify the computerPlayer class without affecting other behaviours.
    - The base class has a static, factory method to return objects of relevant
      sub-class for given player_type.

- During above implementation, I noticed that if we want to change the rules or
  extend the rules, maintaining it as a separate class would be better, 
  and so did the same. Now we could pass a Rules object to the game to play any 
  variant of the game.

- All other, minor decisions are either self-explanatory or explained with 
  in-line comments.

## How to play
```shell
# Clone the repository or download the files
git clone https://github.com/nandhini-yolo/RockPaperScissors.git

# Add the repo to PYTHONPATH
export PYTHONPATH=<TOP_DIR>/src/lib/python:$PYTHONPATH

# Start the game 
<TOP_DIR>/src/appl/rock_paper_scissor_game.py 
```

## Possible extensions

Some of the possible extensions I thought of and considered:

1. Instead of just three hand signals, the game could have more hand signals
   with their own relations (like RPS-Spock-Lizard). Creating a new Rules by 
   inheriting RPSRules and overriding the compare function would enable this.

2. Playing the game between two human users: this can be done by instantiating 
   the two objects in different threads with their own input collection interface.

    a. Two player over the network: This also can be set up by launching the 
       Game object in the server and Player objects can communicate their choice
       over a TCP connection.

3. Right now, ComputerPlayer picks the hand signals randomly. Instead, we can 
   persist the choices made by the opponent and self over time. Then, 
   Computer can analyse the frequency of player choices to maximize the wins.


## Testing notes:

Negative scenarios:
- Raises an error for invalid input for a hand signals
- Raises an error for invalid input for user name and number of rounds
- Game exits for num of rounds is given as zero
- Doesn't persist the user details or score when the game is killed abruptly

Positive scenarios:
- Accepts the valid inputs from the user
- Repeats the round for given N times
- Decides the winner correctly based on the defined set of rules
- Correctly the tally the score at the end of each round
- Correctly track the score of each player and calculates the winner.
