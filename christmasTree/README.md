# Christmas Tree

The question was asked in Codevita Examination 2016

## Problem Statement

Chirag is a pure Desi boy. And his one and only dream is to meet Santa Claus. He decided to decorate a Christmas tree for Santa on coming Christmas. Chirag made an interesting Christmas tree that grows day by day.

The Christmas tree is comprised of the following Parts:

1. Stand
2. Each Part is further comprised of Branches.
3. Branches are comprised of Leaves.

How the tree appears as a function of days should be understood. Basis that print the tree as it appears on the given day. Below are the rules that govern how the tree appears on a given day. Write a program to generate such a Christmas tree whose input is number of days.

## Explanation

1. Create a symmetrical triangle (i.e. first part) of stars with rows (user input + 1).
2. Create a symmetrical traiangle (i.e. second part) starting from 3 stars with rows (user input - 1) upto **x (i.e. user input - 4)** times.
3. Create a symmetrical traiangle (i.e. third part) starting from 3 stars with rows **(x - 1)**.
4. Create a simple stand.

Hence, Program is done.

```\christmasTree> python christmasTree.py```

```4```

Output :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```*```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```* * *```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```* * * * *```

&nbsp;&nbsp;&nbsp;&nbsp;```* * * * * * *```

```* * * * * * * * *```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```* * *```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```* * * * *```

&nbsp;&nbsp;&nbsp;&nbsp;```* * * * * * *```
      
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```* * *```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```* * * * *```
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```*```
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```*```