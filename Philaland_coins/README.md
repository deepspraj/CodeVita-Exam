# Philaland Coins

The question was asked in Codevita Examination 2019

## Problem Statement

The problem solvers have found a new Island for coding and named it as Philaland.

These smart people were given a task to make purchase of items at the Island easier by distributing various coins with different value.

Manish has come up with a solution that if we make coins category starting from $1 till the maximum price of item present on Island, then we can purchase any item easily. He added following example to prove his point.

Let’s suppose the maximum price of an item is 5$ then we can make coins of {$1, $2, $3, $4, $5} to purchase any item ranging from $1 till $5.

Now Manisha, being a keen observer suggested that we could actually minimize the number of coins required and gave following distribution {$1, $2, $3}.

According to him any item can be purchased one time ranging from $1 to $5. Everyone was impressed with both of them.

Your task is to help Manisha come up with minimum number of denominations for any arbitrary max price in Philaland.

## Explaination

The problem wants us to find the minimum numbers of coins required to satisfy all the count from 0 to N (maximum price).
So here the solution, we need to configure that in our daily life we have only **10 rupees coin**, **5 rupees coin**, **2 rupees coin**, and **1 rupee coin**. That means, our solution will be having only **10 rupees coin**, **5 rupees coin**, **2 rupees coin**, and **1 rupee coin**. 

Firstly, we need to find the **count of 10 rupees coin**. This can be configured by **dividing the N (maximum price) by 10** and get the quotient but **the count of 10 rupees coin will be always 1 less** than the quotient which we obtained.

Next, **5 rupees coin can be obtained by dividing the remainder** (i.e the amount left after removing the total amount made by 10 rupees coins) **by 5**. If the quotient is **odd then we have two 5 rupees coins** else **one 5 rupees coin**.

Now, we can have a **count of 1 rupee coin** by extracting the whole amount contributed by 10 rupees coins and 5 rupees coins. Once, the amount is extracted then the left amount will be either odd or even. If the amount is **odd then the number of 1 rupee coins is 1 and 2 if it is even**.

Lastly, extract the total amount contributed 10 rupees coins, 5 rupees coins, and 1 rupee coins. Then **divide the remaining amount by 2 the quotient obtained will be the count of 2 rupee coins**.

<br/>
<br/>

```\Philaland_coins> python philalandCoins.py```

```3```

```123```

```531```

```951```

Output :

```17```

```57```

```99```
