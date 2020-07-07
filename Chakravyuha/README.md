# Chakravyuha

The question was asked in Codevita Examination 2017

## Problem Statement

During the battle of Mahabharat, when Arjuna was far away in the battlefield, Guru Drona made a Chakravyuha formation of the Kaurava army to capture Yudhishthir Maharaj. Abhimanyu, young son of Arjuna was the only one amongst the remaining Pandava army who knew how to crack the Chakravyuha. He took it upon himself to take the battle to the enemies.

Abhimanyu knew how to get power points when cracking the Chakravyuha. So great was his prowess that rest of the Pandava army could not keep pace with his advances. Worried at the rest of the army falling behind, Yudhishthir Maharaj needs your help to track of Abhimanyu's advances. Write a program that tracks how many power points Abhimanyu has collected and also uncover his trail A Chakravyuha is a wheel-like formation.

A Chakravyuha has a very well-defined co-ordinate system. Each point on the co-ordinate system is manned by a certain unit of the army. The Commander-In-Chief is always located at the centre of the army to better co-ordinate his forces. The only way to crack the Chakravyuha is to defeat the units in sequential order. 

A Sequential order of units differs structurally based on the radius of the Chakra. The radius can be thought of as length or breadth of the matrix depicted above.

## Explaination

This is hectic challenge to solve. But when we divide the problem in several problems, then it is easy.

First, we need to solve the numerical spiral matrix.

Second, we need to give a point for every achievement achieved by Abhimanyu and save the location.

Last, print the points and the locations.

<br />
<br />

```\Chakravyuha> python chakravyuha.py```

```4```

Output :

```1 2 3 4```

```12 13 14 5```

```11 16 15 6```

```10 9 8 7```

```Total Power points : 2```

```(0,0)```

```(2,0)```
