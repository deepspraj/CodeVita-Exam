# Accico Equi Pairs

The question was asked in Codevita Examination 2015

## Problem Statement

Ron Wesley has been bit by a three-headed snake and Harry Potter is searching for a potion. The Witch promises to tell the ingredients of the medicine if Harry can find equi pair of an array. Listen to the conversation between Harry The witch to know more about equi pairs. 

### Conversation

**The Witch** : To find the equi pair, you must know how to find the slices first. 

**Harry** : What is a slice? 

**The Witch** : If Z is an array with N elements, a slice of indices (X, Y) is Z[X] + Z[X+1]...Z[Y] 

**Harry** : How can I use it to find equi pair? 

**The Witch** : (a, b) is an equi pair if slice of (0, a-1) = slice of (a+1, b-1) = slice of (b+1, N-1) and b>a+1 and size of array >4

## Explanation

The above conversation pre-defines the way of program. 

**Please read it calmly and carefully.**
<br/>

```\accicoEquiPairs> python accicoEquiPairs.py```

```5 8 6 3 2 1 4 5 6 3 2 11 5 6 9 8 5 6 3 2```

Output :

```Array does not contain any equi pair```
