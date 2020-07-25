# Sheldon Cooper and his beverage paradigm 

The question was asked in Codevita Examination 2015

## Problem Statement

Sheldon Cooper, Leonard Hofstadter and Penny decide to go for drinks at Cheese cake factory. Sheldon proposes to make a game out of this. Sheldon proposes as follows,

- To decide the amount of beverage they plan to consume, say X.

- Then order for a random number of different drinks, say { A, B, C, D, E, F } of quantities { a, b, c, d, e, f } respectively.

- If quantity of any three drinks add up to X then we'll have it else we'll return the order. E.g. If a + d + f = X then True else False

You are given

1. Number of bottles N corresponding to different beverages and hence their sizes

2. Next N lines, contain a positive integer corresponding to the size of the beverage

3. Last line consists of an integer value, denoted by X above

Your task is to help find out if there can be any combination of three beverage sizes that can sum up to the quantity they intend to consume. If such a combination is possible print True else False

## Explanation

Within the given capacity of the bottle, We just need to find which three bottles will contribute to be summation equal to the total amount of beverage which Sheldon and his friends are interested to drink.

**Please make sure that Sheldon and his other two friend's get different capacity of bottle every time.**

```\sheldonCooper> python sheldonCooper.py```

```8```

```10```

```25```

```1```

```18```

```34```

```14```

```3```

```8```

Output :

```True```
