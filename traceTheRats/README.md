# Trace The Rats

The question was asked in Codevita Examination 2014

## Problem Statement

Given a square maze (A) of dimension N, every entry (A[i][j]) in the maze is either an open cell 'O' or a wall 'X'. A rat can travel to its adjacent locations (left, right, top and bottom), but to reach a cell, it must be open. Given the locations of R rats, can you find out whether all the rats can reach others or not?

## Explanation

The logic is explained as follow:

1. At given location of rats, we need to check whether it is open cell or not.

2. If there is an open cell at any of the 4 surrounding then rat can move else the rat can't.

<br/>

```\traceTheRats> python traceTheRats.py```

```4```

```x o o x```

```o x x o```

```x o x o```

```o x o x```

```3```

```1 2```

```2 4```

```3 2```

Output :

```Yes```

```Yes```

```No```
