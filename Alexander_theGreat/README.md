# Alexander The Great

The question was asked in Codevita Examination 2019

## Problem Statement

Alexander The great, while roaming the stretch of Turkey, came across a wise man. He asked the wise man, "Who is the greatest conqueror of all?". The wise man replied, "A person with great strength and intelligence. Whosoever can solve my puzzle will go on to become the greatest!". 

The puzzle is as follows; 

Given two integers **'n1'** and **'n2'**, select two integers **'a'** and **'b'**, such as to solve the equation **(n1 * a + n2 * b = x)**. But there is a catch, **'x'** is the smallest positive integer which satisfies the equation. Can you help Alexander become the greatest?

## Explaination

The question is linear Diophantine equation. Diophantine equation is the equation in which only the equation is provided and two or more unknowns are needed to find. But, Diophantine equation is solvable only when the **x** is multiple of **gcd** of **a** ( intercept of n1 ) and **b** ( intercept of n2 ). Either **smallest multiple** is the required solution of the given question or **gcd** is the solution ( whichever is the smallest ).

```\Alaxander_theGreat> python alexanderTheGreat.py```

```784525```

```09645```

Output :

```5```


### [For More details](https://en.wikipedia.org/wiki/Diophantine_equation)