# Minimum Distance

The question was asked in Codevita Examination 2015

## Problem Statement

Two riders A and B are travelling on a highway towards each other on two roads that intersect at right angle at speeds VA meters/second and VB meters/second. A is at a distance of 'x' meters and B is at a distance of 'y' meters from the intersection. Calculate the minimum distance between these two riders that is possible.

**For diagrammatic explanation please view the pdf file.**

## Explanation

First, all the inputs provided by the user must be positive as distances and velocities can't be negative (logically).

Now, We need to find the distance between two riders by using the distance formula `(i.e. sqrt(x*x + y*y))` and subtract velocity of each rider from respective distance.

And perform above step until distance of both the rider become's negative. As soon as, both the distances are negative just break the loop and the answer is the minimum distance which we calculated using distance formula before failing in the condition of positivity.


**Calculating and printing of output should be done up to 11 digits precision after decimal point.**

<br/>

```\minimumDistance> python minimumDistance.py```

```10056```

```12034```

```500```

```321```

Output :

```4695.233434026471```
