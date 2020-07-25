# Where's My Car

The question was asked in Codevita Examination 2016

## Problem Statement

The year is 2050. The population surge has taken over our metropolitan cities. High rise buildings are on a rise. And as usual, with the increase in population, the problem of parking in the city has increased manifold.

To reduce the problem of parking, the government has built multi-storey parking lots all over the city. Imagine the city as an X-Y grid. And there are roads connecting all the neighbouring grid points except diagonals. And there is a pre-defined intersection interval **'I'** for parking lots such that at every I th intersection, there is a parking lot, starting from (0,0). For example, for a city of grid size 4×7 and I=3, you’ll have 6 parking lots at (0,0), (0,3), (0,6), (3,0), (3,3) and (3,6).

Now all the cars have been fitted with self-driving mechanism. So whenever you get out of a car at any point in the grid, it will choose the nearest parking lot and automatically drive to it. If two parking lots are at equal distance from where you left, it will choose the parking lot with the lowest X-coordinate first, and if X-coordinates are same, the lowest Y-coordinate.

At the parking lot, the cars will start getting parked from the ground floor and in the first available slot. As each floor gets filled up, newer cars will start parking on floors above them. Assume all the parking lots in the city have unlimited number of floors and a common maximum capacity of each floor **'C'**.

Now whenever the owner wants to know where his car is parked or wants to retrieve it, he’ll open the app ‘Where’s my car!’ and insert his car number and the app will tell him the coordinates of the parking lot, the floor number and the slot number.

## Explanation

The Logic applied precisely is explained as follows:

1. Get the matrix and plot the Parking Lots according to the user input.

2. Once, the parking lots are located, create a dictionary with the key as the lots location.

3. Get the data from the user whether the car is here for parking or retrieval.

4. According to the users input, park the car at the nearest parking lot.

5. For retrieval checks the location of the car in the dictionary.

6. As soon as location obtained then print the key of the dictionary where the car is found i.e. the location of the parking lot.

7. For the count of the floor just use divide the index by the capacity where the car was located and for the count of the car at that floor use modulus operation.
<br/>

**Note: The source code don't support multiple areas (i.e. no more than one city area) else tried the program may crash.**

<br/>

```\whereMyCar> python wheresMyCar.py```

```7 7 2 2```

```10```

```P 3 2 MH12DE1433```

```P 5 3 DL04AF4943```

```P 5 5 KL45DD2002```

```R DL04AF4943```

```P 1 6 MH06EF3259```

```R MH12DE1433```

```P 3 6 UP16CD1996```

```R KL45DD2002```

```R MH06EF3259```

```P 4 6 GJ03MW8855```

Output :

```16```

```4 2 0 1```

```2 2 0 1```

```4 4 0 1```

```0 6 0 1```
