# Zombie World

The question was asked in Codevita Examination 2014

## Problem Statement

Zoya has developed a new game called Zombie World. The objective of the game is to kill all zombies in given amount of time. More formally,

- **N** represents the total number of zombies in the current level

- **T** represents the maximum time allowed for the current level

- **P** represents the initial energy level a player starts with

- **Ei** defines the energy of the i-th zombie

- **D** defines the minimum energy the player needs, to advance to the next level

When a player energy is greater than or equal to the i-th zombie's energy, the player wins. Upon winning, the player will be awarded with an additional energy equal to the difference between current zombie energy and the player energy.

One unit of time will be taken to complete the fight with a single zombie.

Rules of the game: -

- At any given time, a player can fight with only one zombie

- Player is allowed to choose any one zombie to fight with.

Your task is to determine whether the player will advance to the next level or not, if he plays optimally.

## Explanation

The problem is an easy.

The logic is explained as follows:

1. It is necessary that initial energy of the player should always be greater than or equal to the first zombie in the sequence to completely kill the one.

2. The player kills the first zombie and gain health equal to difference of the energy of the zombie and the player.

3. Repeat the above two steps to kill all zombies and gain the energy.

4. After killing all the zombies, the health of the player should be equal to or greater than the energy required to advance the player to next level.

5. If above condition satisfy then print Yes else No.


**Note: The player fights all the zombies according to sequence which user has provided.**

<br/>

```\zombieWorld> python zombieWorld.py```

```1```

```5 6```

```56 86 23 14 89```

```63 200```

Output :

```Yes```
