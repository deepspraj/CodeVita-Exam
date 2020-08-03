# Stone Game - One Four

The question was asked in Codevita Examination 2014

## Problem Statement

Alice and Bob are playing a game called "Stone Game". Stone game is a two-player game. Let N be the total number
of stones. In each turn, a player can remove either one stone or four stones. The player who picks the last stone,
wins. They follow the "Ladies First" norm. Hence Alice is always the one to make the first move. Your task is to find
out whether Alice can win, if both play the game optimally.

## Explanation

The problem is an easy to be solved. 

The logic is explained as follows:

1. The total number of stones is divided by 4. As, we want to know who was the last one between **Alice** and **Bob** to pick 4 stone at an instance.

    - If the quotient netted is even that means **Bob** is the last player to pick the 4 stones at an instance.

    - If the quotient netted is odd that means **Alice** is the last player to pick the 4 stones at an instance.

2. The remainder after subtracting all the 4 stone's taken by both the player from the total number of stones.

    - If the remainder is odd and the quotient is even then **Alice** wins the game.

    - If the remainder is odd and the quotient is odd then **Bob** wins the game.

    - If the remainder is even and the quotient is even then **Bob** wins the game.

    - If the remainder is even and the quotient is odd then **Alice** wins the game.


**Alice is preferenced to pick first due to "Ladies first rule."**
<br/>

```\stoneGame>python stoneGame.py```

```4```

```63```

```45```

```21```

```98```

Output :

```No```

```No```

```No```

```No```
