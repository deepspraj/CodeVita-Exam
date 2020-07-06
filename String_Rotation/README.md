# String Rotation

The question was asked in Codevita Examination 2018

## Problem Statement

Rotate a given String in the specified direction by specified magnitude.

After each rotation make a note of the first character of the rotated String, after all rotation are performed the accumulated first character as noted previously will form another string, say FIRSTCHARSTRING.

Check If FIRSTCHARSTRING is an Anagram of any substring of the Original string.

If yes print "YES" otherwise "NO". Input

The first line contains the original string s. The second line contains a single integer q. The ith of the next q lines contains character d[i] denoting direction and integer r[i] denoting the magnitude.

## Explaination

The user will provide us the string (word). 

Next, the user will state the length of the substring. 

Now the user will provide the location of the letters of the substring which are located in the string. 

Once, we get all the letters we need to form substring. And check for the anagram of the formed word in the string's substring. 

If we get at least one anagram then we print **'Yes'** else **'No'**.

<br/>
<br/>

```\String_Rotation> python stringRotation.py```

```alphabets```

```5```

```l 0```

```r 8```

```l 4```

```r 6```

```l 2```

Output :

```YES```
