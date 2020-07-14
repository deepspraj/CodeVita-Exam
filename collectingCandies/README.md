# Collecting Candies

The question was asked in Codevita Examination 2016

## Problem Statement

Krishna loves candies a lot, so whenever he gets them, he stores them so that he can eat them later whenever he wants to.

He has recently received N boxes of candies each containing Ci candies where Ci represents the total number of candies in the ith box. Krishna wants to store them in a single box. The only constraint is that he can choose any two boxes and store their joint contents in an empty box only. Assume that there are infinite number of empty boxes available.

At a time he can pick up any two boxes for transferring and if both the boxes say contain X and Y number of candies respectively, then it takes him exactly X+Y seconds of time. As he is too eager to collect all of them he has approached you to tell him the minimum time in which all the candies can be collected.

## Explanation

The problem is really an easy one. But, there is a twist that we need to recognize before solving.

For that I have divided the solution in two equal parts.

1. The Count of boxes is of even multiple.

        For example,
        There are 4 Boxes ans user provide data of candies count in each box (1 2 3 4).
        So, we need to add each and every number by sequence to the previous sum. 
        4 boxes, each containing 1, 2, 3 and 4 candies respectively. 
        Adding 1 + 2 in a new box take's 3 seconds. 
        Adding 3 + 3 in a new box takes 6 seconds. 
        Adding 4 + 6 in a new box takes 10 seconds.
        Hence, total time taken is 19 seconds.

2. The Count of boxes is of odd multiple.

        For example,
        There are 5 Boxes ans user provide data of candies count in each box (1 2 3 4 5).
        5 boxes, each containing 1, 2, 3, 4 and 5 candies respectively.
        Adding 1 + 2 in a new box takes 3 seconds.
        Adding 3 + 3 in a new box takes 6 seconds.
        Adding 4 + 5 in a new box takes 9 seconds.
        Adding 6 + 9 in a new box takes 15 seconds.
        Hence, total time taken is 33 seconds.

<br/>

```\collectingCandies> python collectingCandies.py```

```3```

```6```

```12 35 69 18 32 89```

```13```

```1 2 3 4 5 6 7 8 9 13 95 63 65```

```3```

```86 52 34```

Output :

```718 seconds```

```977 seconds```

```276 seconds```
