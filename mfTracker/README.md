# MF Tracker

The question was asked in Codevita Examination 2015

## Problem Statement

Mani is a savvy investor. He is reviewing his financial investment performance. He is currently analyzing his investment into mutual funds he had made in the past. From those funds he earned a certain amount each. Coincidentally, it so happened that all the funds that Mani had invested in, had in turn invested the funds in same set of stocks. So when he exited, he exited all Mutual Funds at the same time. Mani has past statements from each Fund which tell him about the number of holdings of each stock and the value of the entire portfolio when he exited those funds.

Mani is now curious to find out what was the price of each stock across all funds when he exited. He wants to do this to find out if his decision to exit the funds based on today's price was right or wrong. Your task is to help Mani find stock prices when he exited them.

Compute stock prices up to 11 decimal places and print them up to 2 decimal places.

Let's say all funds invested in TCS, Infy and Wipro, then Mani has the following knowledge 

Fund 1 -> # of shares of TCS, Infy and Wipro each and overall value of Mani's portfolio
Fund 2 -> # of shares of TCS, Infy and Wipro each and overall value of Mani's portfolio
Fund 3 -> # of shares of TCS, Infy and Wipro each and overall value of Mani's portfolio

## Explanation

The problem is just a simple linear equations question where 3 unknowns are shares of TCS, Infosys and Wipro.

<br/>

```\mfTracker> python mfTracker.py```

```3```

```10 10 10 60000```

```10 20 0 50000```

```20 0 10 50000```

Output :

```1000.0```

```2000.0```

```3000.0```
