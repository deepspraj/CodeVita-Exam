# Jurassic Park

The question was asked in Codevita Examination 2018

## Problem Statement

Smilodon is a ferocious animal that used to live during the Pleistocene epoch (2.5 mya–10,000 years ago). Scientists successfully created few smilodons in experimental DNA research. A park is established and those smilodons are kept in a cage for visitors.
This park consists of Grasslands(G), Mountains(M), and Waterbodies(W) and it has three gates (situated in grasslands only). Below is a sample layout.

Before opening the park, the club authority decides to calculate the Safety index of the park. The procedure of the calculation is described below. Please help them to calculate.
Safety Index calculation

Assume a person stands on grassland(x) and a Smilodon escapes from the cage situated on grassland (y). If the person can escape from any of those three gates before the Smilodon able to catch him, then the grassland (x) is called safe else it is unsafe. A person and a Smilodon both take 1 second to move from one area to another adjacent area (top, bottom, left, or right) but a person can move only over grasslands through Smilodon can move over grasslands and mountains.

If any grassland is unreachable for Smilodon (maybe it is unreachable for any person also), to increase the safe index value Club Authority use to mark those grasslands as safe land.

## Explaination

For solving the problem we need to state two things that grassland is safe only in two possible ways.

1. When grassland is surrounded by water.
2. And if any other grassland is present in the neighbor.

As soon as we get the coordinates of the cage. Change the notation of the cage to 'C'. By using the above two ways, we can calculate the number of safe grasslands. Once, we get the count of safe grasslands we can obtain the safety index from the given formula.

<br/>
<br/>

```\Jurassic_Park> python jurassicPark.py```

```5 5```

```3 5 5 2 5 3 4 1```

```w g w m g```

```g g g w m```

```m m g m g```

```g g w m w```

```w g g w m```

Output :

```72.73```
