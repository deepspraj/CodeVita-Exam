# Distribute Books

The question was asked in Codevita Examination 2019

## Problem Statement

For enhancing the book reading, the school distributed storybooks to students as part of the Children’s day celebrations.
To increase the reading habit, the class teacher decided to exchange books every week so that everyone will have a different book to read. She wants to know how many unique exchanges are possible in such a way that students don't repeat the book.

## Explaination

The problem can be solved in two ways:

1. Formula Method
2. Closest Integer Method

### Method 1

In this method, we need to find the subfactorial (unique combinations) of the given integer by using the formula.

#### !n = (n-1)(!(n-1) + !(n-2))

### Method 2

In this method, when we divide factorial by exponential (e = 2.71828) gives the closest number to the subfactorial of the given integer.

<br>

```\Distribute_books> python distributeBooks.py```

```6```

Output :

```265```

### [For More details](https://en.wikipedia.org/wiki/Derangement)