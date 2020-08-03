# Super ASCII String Checker

The question was asked in Codevita Examination 2014

## Problem Statement

In the Byte land country, a string "S" is said to super ascii string if and only if count of each character in the string is equal to its ascii value.

In the Byte land country ascii code of 'a' is 1, 'b' is 2 ...'z' is 26.

Your task is to find out whether the given string is a super ascii string or not.

## Explanation

The Logic is explained as follow:

1. We need to create the dictionary with the key as ascii code of byte land and respective value as an alphabet.

2. Count all alphabets according to the sequence.

3. Check that count and key of the alphabet in the dictionary is the same or not.

4. Perform above steps for all alphabets simultaneously.

5. At some instance we found that the key and the ascii code is not same abort the remaining task and print No else keep performing the steps.

<br/>

```\superAsciiStringChecker> python superAsciiStringChecker.py```

```3```

```abbcccddddeeeee```

```eeeeddddccbba```

```pikachu```

Output :

```Yes```

```No```

```No```
