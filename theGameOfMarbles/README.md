# The Game of Marbles

The question was asked in Codevita Examination 2016

## Problem Statement

Darrell and Sally are two best friends. They had a large collection of marbles. They devised a game with it to play in their free time which will also help them to improve their math. One of them will have to select a certain number of marbles and give a hint to find the number. The other will have to guess the first number that matches the given criteria and vice versa.

Your task is to act as a judge for this game. When the player finds the answer, you will have to verify the answer. If answer is right, add 10 points to that player. If the player passes the question, you will have to give the right answer (no change in points in this case). You should also announce the winner at the end of the game.

*Hint to find the number:*

When the marbles are put into a group of x1, x2, x3,...(where x1, x2, x3 can be any number from 1 to 100), it falls into a perfect group.(No marble is left without a group).

### Example 

When Darrell says the number falls into a perfect set when she groups them into sets of 3 and 5, the answer could be 15 or 30 and so on. Since the first number that matches the criteria is 15, 15 will be the answer.

*(Explanation: when 15 marbles is put into groups of 3, We will get 5 sets of 3 marbles each and when it is put into groups of 5, we will get 3 sets of 5 marbles each. For 16 marbles, we will get 5 sets of 3 marbles each and one marble will be left without a proper group. So 16 cannot be the answer).*

<a href="https://ibb.co/g38rgLJ"><img src="https://i.ibb.co/zrgmfTZ/abcd.jpg" alt="abcd" border="0"></a>

***NOTE: Please have a look at Sample Input and Output before you read the Input and Output specification.***

## Explanation

The logic is explained as follows:

1. The accurate answer to question asked by the questioner is **LCM** of the quantity of marbles.

2. The question always starts with questioner name and **x** quantity of marbles.

3. We take question and answer from the user in every repetition of for loop. Therefore, we limited the range of the for loop to n/2.

4. As soon as, the question is asked by the questioner we need to calculate the accurate answer.

5. Once the answerer resolves the asked question. We need checking whether the answer answered by the answerer is correct or not.

6. If the answer is correct then credit 10 points to answerer's account else do not credit the answerer.

7. Perform above 3 steps n/2 times (Reason: step 3).

8. Print the competition's statistics and winner.

<br/>

```\theGameOfMarbles> python theGameOfMarbles.py```

***Input :*** ```8```

***Input :*** ```Darrell 40,17```

***Output :*** ```Darrell's question is 40,17```

***Input :*** ```A Sally 680```

***Output :*** ```Correct Answer```

***Output :*** ```Sally: 10 points```

***Input :*** ```Sally 36,8```

***Output :*** ```Sally's question is 36,8```

***Input :*** ```A Darrell 96```

***Output :*** ```Incorrect Answer```

***Output :*** ```Darrell: 0 points```

***Input :*** ```Darrell 7,34```

***Output :*** ```Darrell's question is 7,34```

***Input :*** ```A Sally 238```

***Output :*** ```Correct Answer```

***Output :*** ```Sally: 10 points```

***Input :*** ```Sally 11,23```

***Output :*** ```Sally's question is 11,23```

***Input :*** ```A Darrell 253```

***Output :*** ```Correct Answer```

***Output :*** ```Darrell: 10 points```

***Result :***

```Total Points```

```Darrell : 10 points```

```Sally : 20 points```

```Game Result : Sally is winner```
