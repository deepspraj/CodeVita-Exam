# Reverse Gear

The question was asked in Codevita Examination 2015

## Problem Statement

A futuristic company is building an autonomous car. The scientists at the company are training the car to perform Reverse parking. To park, the car needs to be able to move in backward as well as forward direction. The car is programmed to move backwards **B** meters and forwards again, say **F** meters, in a straight line. The car does this repeatedly until it is able to park or collides with other objects. The car covers **1** meter in **T** units of time. There is a wall after distance **D** from car's initial position in the backward direction.

The car is currently not without defects and hence often hits the wall. The scientists are devising a strategy to prevent this from happening. Your task is to help the scientists by providing them with exact information on amount of time available before the car hits the wall.

## Explanation

In reality, we park the car at a particular position by driving some distance forward, backward after ensuring the position we turn off the engine.

So, we need to apply the same strategy in this problem.

Let **C** be the difference between the forward distance and backward distance.

Multiply the **C** with **T** (time) and add to the Total time required **(TT)**.

Subtract **C** from **D** (distance).

Perform the above two steps, repeatedly until the **D** becomes smaller than **C**.

As soon as the **C** becomes greater than **D** multiply the remaining distance **D** and add the product to the Total time.

And print the Total Time **(TT)**.

**Note - If ans display as "0" that means the provided inputs are not according to the specific conditions.**

**Please check input twice before entering.**
<br/>
<br/>

```\reverseGear> python reverseGear.py```

```2```

```5 17 9 23```

```3 12 8 20```

Output :

```297```

```208```
