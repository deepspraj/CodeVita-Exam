# Catch 22

The question was asked in Codevita Examination 2015

## Problem Statement

A robot is programmed to move forward F meters and backwards again, say B meters, in a straight line. The Robot covers 1 meter in T units of time. On Robot's path there is a ditch at a distance FD from initial position in forward direction as well as a ditch at a distance BD from initial position in backward direction. This forward and backward movement is performed repeatedly by the Robot.

Your task is to calculate amount of time taken, before the Robot falls in either ditch, if at all it falls in a ditch.

## Explanation

First, if forward distance (F) and backward distance (B) are same and forward direction is greater than forward distance then the robot will not be ditched **i.e. NO DITCHED.**

Let distance (dist) be the distance from the initial position (origin) and answer (ans) be the total distance travelled by the robot and answer. 

Add **F** to **dist** and **ans** when robot travels forward. Add **B** to **ans** and subtract from **dist**. 

Perform this untill **dist** is less than or equal to the **FD** or **BD** is greater than or equal to the **dist**. 

If **FD** condition satisfies the let forward (variable) be equal to 1 else **BD** condition satisfies then let backward (variable) be equal to 1.

If forword is equal to one then follow :

- If the dist is equal to **FD** then simply get the product of ans and time **(T)** else subtract difference of dist and **FD** from ans and then get the product of ans and time **(T)**.

If backword is equal to one then follow :

- If the dist is equal to BD then simply get the product of ans and time **(T)** else add difference of dist and **FD** from ans and then get the product of ans and time **(T)**.

Once, the product is obtained just print it and print the direction of the whether it is forward **(F)** or backward **(B)**.

<br/>

```\catch22> python catch22.py```

```5```

```4 5 6 7 8```

```3 2 1 0 5```

```7 5 2 3 6```

```9 6 3 2 48```

```5 2 3 6 8```

Output :

```432 B```

```0 F```

```6 F```

```6 F```

```30 F```

