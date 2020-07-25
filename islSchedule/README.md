# Indian Soccer League (ISL) Schedule

The question was asked in Codevita Examination 2015 and 2016

## Problem Statement

The Indian Soccer League (ISL) is an annual football tournament. The group stage of ISL features N teams playing against each other with following set of rules:

1. N teams play against each other twice - once at Home and once Away.

2. A team can play only one match per day.

3. A team cannot play matches on consecutive days.

4. A team cannot play more than two back to back Home or Away matches.

5. Number of matches in a day has following constraints.

    - The match pattern that needs to be followed is -

        - Day 1 has two matches and Day 2 has one match,

        - Day 3 has two matches and Day 4 has one match and so on

    - There can never be 3 or more matches in a day.

6. Gap between two successive matches of a team cannot exceed floor(N/2) days where floor is the mathematical function floor ( ).

7. Derby Matches (any one)

    - At least half of the derby matches should be on weekend.

    - At least half of the weekend matches should be derby matches.

Your task is to generate a schedule abiding to above rules.

## Explanation

Initially, we critically need checking whether the input provided by the user is greater than **eight** and is an **even** or not.

Second, we need divide the first half of the team in one list (array) and other half in second list (array) in reverse order.

Now, matches will be between the first team from first half list and second half list.The count of teams must be even because each and every team should have an opponent.

Next remove last team of first half list and insert it to last of the second half teams list. Now, remove the first team from second half and insert that team at second position in first half team list.

Repeat the above step up to n-1 times to get unique matches every time.
If there is condition of every team play twice with same opponent then just print the same list of matches twice.

**Note: The standard condition of derby matches is yet unsatisfied, but other than this all local condition is reasonably satisfied.**


**Code will be updated soon.**

<br/>

```\islSchedule> python islSchedule.py``` 

```8```

```1 2 3 4 5 6 7 8```
  
Output :

```T1 vs T8``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T2 vs T7```

```T3 vs T6```

```T4 vs T5``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T1 vs T7```

```T8 vs T6```

```T2 vs T5``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T3 vs T4```

```T1 vs T6```

```T7 vs T5``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T8 vs T4```

```T2 vs T3```

```T1 vs T5``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T6 vs T4```

```T7 vs T3```

```T8 vs T2``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T1 vs T4```

```T5 vs T3```

```T6 vs T2``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T7 vs T8```

```T1 vs T3```

```T4 vs T2``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T5 vs T8```

```T6 vs T7```

```T1 vs T2``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T3 vs T8```

```T4 vs T7```

```T5 vs T6``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T1 vs T8```

```T2 vs T7```

```T3 vs T6``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T4 vs T5```

```T1 vs T7```

```T8 vs T6``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T2 vs T5```

```T3 vs T4```

```T1 vs T6``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T7 vs T5```

```T8 vs T4```

```T2 vs T3``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T1 vs T5```

```T6 vs T4```

```T7 vs T3``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T8 vs T2```

```T1 vs T4```

```T5 vs T3``` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ```T6 vs T2```

```T7 vs T8```
