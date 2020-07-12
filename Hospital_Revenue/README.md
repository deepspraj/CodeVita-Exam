# Hospital Revenue

The question was asked in TCS Codevita Examination

## Problem Statement

Dr. Vishnu is opening a new world-class hospital in a small town designed to be the first preference of the patients in the city. Hospital has N rooms of two types – with TV and without TV, with daily rates of R1 and R2 respectively. However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the year, instead, it follows a pattern.

The number of patients on any given day of the year is given by the following formula – (6-M)2 + | D-15 |, where M is the number of the month (1 for Jan, 2 for Feb …12 for Dec) and D is the date (1,2…31).

All patients prefer without TV rooms as they are cheaper but will opt for with TV rooms only if without TV rooms are not available. Hospital has a revenue target for the first year of operation. Given this target and the values of N, R1, and R2 you need to identify the number of TVs the hospital should buy so that it meets the revenue target. Assume the Hospital opens on 1st Jan and year is a non-leap year.

## Explanation

Firstly, We need to assume the fact that the patient gets discharged on the same day only.

Then, count the number of patients visited every day if the visited patient is more than the number of rooms we can have the only same count of patients.

If patients are less than the number of r0oms then we need to allow the non TV rooms and thereafter TV rooms.

By considering that there are **'x'** TV rooms and **'(n-x)'** are non TV rooms we need to calculate total revenue, if the calculated revenue just exceeds the targeted revenue or is equal to targeted revenue then the count is correct else we need to increase the number of TV rooms and recalculate the revenue.

<br/>
<br/>

```\Hospital_Revenue> python hospitalRevenue.py```

```30```

```2000 1000```

```10000000```

```16```

Output :

```5```
