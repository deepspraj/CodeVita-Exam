# Bride Hunting

The question was asked in Codevita Examination 2019

## Problem Statement

Sam is an eligible bachelor. He decides to settle down in life and start a family.He goes bride hunting. He wants to marry a girl who has at least one of the 8 qualities mentioned below :-

1) The girl should be rich.
2) The girl should be an Engineer/Doctor.
3) The girl should be beautiful.
4) The girl should be of height 5.3".
5) The girl should be working in an MNC.
6) The girl should be an extrovert.
7) The girl should not have spectacles.
8) The girl should be kind and honest.

He is in search of a bride who has some or all of the 8 qualities mentioned above. On bride hunting, he may find more than one contenders to be his wife.

In that case, he wants to choose a girl whose house is closest to his house. Find a bride for Sam who has maximum qualities. If in case, there are more than one contenders who are at equal distance from Sam’'s house

then print **"Polygamy not allowed".**

Given a Matrix N*M, Sam's house is at (1, 1). It is denoted by 1. In the same matrix, the location of a marriageable Girl is also denoted by 1. Hence 1 at location (1, 1) should not be considered as the location of a marriageable Girl’s location.

The qualities of that girl, as per Sam’'s criteria, have to be decoded from the number of non-zero neighbors (max 8-way) she has. Similar to the condition above, 1 at location (1, 1) should not be considered as the quality of a Girl.

Find Sam, a suitable Bride and print the row and column of the bride, and find out the number of qualities that the Bride possesses.

## Explanation

Firstly, we need to confirm that whether at a particular location (say **A**) the bride is present or not. If at a location **(A)** the value is **1** that means there is the bride and we need to consider that location **(A)**. To calculate the qualities of the bride **(A)** we need to calculate the count of surrounding bride. If the bride at location **A** is surrounded by **3** another bride's that means the number of qualities of the bride at the location **(A)** is **3**. In this way, we need to calculate the qualities of every present bride and their qualities. The bride with more number of qualities and close to Sam's house is the right candidate for marriage.

**It is necessary that Sam should be present at location (1,1)**

```\Bride_Hunting> python brideHunting.py```

```6 6```

```1 0 0 0 0 0```

```0 0 1 1 1 0```

```0 0 1 1 1 0```

```0 0 1 1 1 0```

```0 0 1 1 1 0```

```0 0 1 1 1 0```

Output :

```3:4:8```
