# Card Flipping Game

## TL;DR Latest Results

<u>1x10</u><sup>6</sup> <u>Iterations</u>

| Player    |Wins   |Win Percentage (1 d.p)| 
| :--------:|:-----:|:------------:|
| Player 1  |143158 | 14.3%        |
| Player 2  |143289 | 14.3%        |
| Player 3  |142682 | 14.3%        |
| Player 4  |142281 | 14.2%        |
| Player 5  |143665 | 14.4%        |
| Player 6  |142636 | 14.3%        |
| Player 7  |142289 | 14.2%        |

## Background

This repo is to simulate a simplified version of a game I play IRL. As an MMath student I thought I could figure out the probabilities of winning this game by hand (my original analysis below). However I'm not convinced by my own workings out so thought it a good idea to run a simulation and see if my calculations are reasonable. IRL we have 7 players but this could be adapted to any number.

## Rules of the game

The aim of the game is to win the prize (surprise surprise). To setup the game shuffle the order of players and lay down an equal number of cards. Each person takes a turn to flip a card over. Either the card has the prize and the game ends or play moves on to the next player.

## 2 Player Example 

There are two cards (A and B)

@ToDo Add Images

Player 1 chooses card A. Not the winner.

Player 2 only has card B to choose. Wins.

### Probabilities

- We know that "The sum of the probabilities of all outcomes must equal 1."
- We also know that Player 2's chances are dependant on the outcome of Player 1's choice
- This means the probability of Player 2 winning is the probability of Player 1 losing AND the probability that Player 2 chooses correctly.

| Player    |Win |Lose | 
| :--------:|:--:|:---:|
| Player 1  |1/2 |1/2 |
| Player 2  |1/2 * 1/1| (1-P(win)) |

Which equates to

| Player    |Win |Lose | 
| :--------:|:--:|:---:|
| Player 1  |50% |50% |
| Player 2  |50%| 50% |

## My initial exploration of a 7 player game
I used the same method and assumptions as above and this was my process.

<u>Player 1</u>
- W: 1/7
- L: 1-P(win) = 1 - 1/7 = 6/7

<u>Player 2</u>
- W: P(Player 1 losing AND picking the correct card) = 6/7 * 1/6 = 1/7
- L: 1-P(win) = 1 - 1/7 = 6/7

<u>Player 3</u>
- W: P(Player 2 losing AND picking the correct card) = 6/7 * 1/5 = 6/35
- L: 1-P(win) = 1 - 6/35 = 29/35

<u>Player 4</u>
- W:  29/35 * 1/4 = 29/140
- L:  1 - 29/140 = 111/140

<u>Player 5</u>
- W:  111/140 * 1/3 = 37/140
- L:  1 - 37/140 = 103/140

<u>Player 6</u>
- W:  103/140 * 1/2 = 103/280
- L:  1 - 103/280 = 177/280

<u>Player 7</u>
- W:  177/280 * 1/1 = 177/280
- L:  1 - 177/280 = 103/280

### Summary Table (1 d.p)

| Player    |Win  |Lose   | 
| :--------:|:---:|:-----:|
| Player 1  |14.3%| 85.7% |
| Player 2  |14.3%| 85.7% |
| Player 3  |17.1%| 82.9% |
| Player 4  |20.7%| 79.3% |
| Player 5  |26.4%| 73.6% |
| Player 6  |36.8%| 63.2% |
| Player 7  |63.2%| 36.8% |

### Results Analysis

@ToDo Add graph of placement vs chance of winning

Intuitively I thought it would be a place in the middle with the highest chance of winning so I decided to create this simulation to test my theory.

## Simulation Results

<u>1x10</u><sup>6</sup> <u>Iterations</u>

| Player    |Wins   |Win Percentage (1 d.p)| 
| :--------:|:-----:|:------------:|
| Player 1  |143158 | 14.3%        |
| Player 2  |143289 | 14.3%        |
| Player 3  |142682 | 14.3%        |
| Player 4  |142281 | 14.2%        |
| Player 5  |143665 | 14.4%        |
| Player 6  |142636 | 14.3%        |
| Player 7  |142289 | 14.2%        |

## Conclusion

Clearly my analysis doesn't match the simulation so if anyone can point out my mistake I will be very grateful.