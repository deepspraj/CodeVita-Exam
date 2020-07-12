# Logic Pyramid

The question was asked in Codevita Examination 2016

## Problem Statement

Identify the logic behind the series 6 28 66 120 190 276....

The numbers in the series should be used to create a Pyramid. The base of the Pyramid will be the widest and will start converging towards the top where there will only be one element. Each successive layer will have one number less than that on the layer below it. The width of the Pyramid is specified by an input parameter N. In other words, there will be N numbers on the bottom layer of the pyramid.

The Pyramid construction rules are as follows:

1. First number in the series should be at the top of the Pyramid
2. Last N number of the series should be on the bottom-most layer of the Pyramid, with Nth number being the right-most number of this layer.
3. Numbers less than 5-digits must be padded with zeroes to maintain the sanctity of a Pyramid when printed.

## Explanation



```\logicPyramid> python logicPyramid.py```

```7```

Output :

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```00006```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```00028 00066```

&nbsp;&nbsp;&nbsp;&nbsp;```00120 00190 00276```

&nbsp;&nbsp;&nbsp;```00378 00496 00630 00780```

&nbsp;&nbsp;```00946 01128 01326 01540 01770```

&nbsp;```02016 02278 02556 02850 03160 03486```

```03828 04186 04560 04950 05356 05778 06216```
