# Minimum Product Array

The question was asked in Codevita Examination 2016

## Problem Statement

The task is to find the minimum sum of Products of two arrays of the same size, given that k modifications are
allowed on the first array. In each modification, one array element of the first array can either be increased or
decreased by 2.

## Explanation

The question above states that we can increase or decrease the certain number by twice the user input (i.e. k).

1. We need to find the product of first element of array1 and array2. If product and element of array2 are negative (i.e. < 0) then we need to increase the element of array1 and again find the product.

2. Now find the product of first element of array1 and array2. If product and element of array1 are negative (i.e. < 0) then we need to decrease the element of array1 and again find the product.

3. Now find the product of first element of array1 and array2. If product is positive (i.e. > 0) and element of array1 is negative (i.e. < 0) then we need to increase the element of array1 and again find the product.

4. Now find the product of first element of array1 and array2. If product and element of array1 are positive (i.e. > 0) then we need to decrease the element of array1 and again find the product.

Once, any one of the above conditions satisfies and new product is found then find difference between new product and old product.If the diff is less than maximum difference then add previously obtained product in the variable of the minimum sum.

Lastly, print the Minimum Sum obtained.

**Note: Array (specifically integer type) in python language means list data type with all the containing values are purely integers.**

<br/>
<br/>

```\minProductArray> python minProductArray.py```

```6 6```

```-2 6 3 -7 -4 5```

```-3 23 -86 43 -68 74```

Output :

```-805```
