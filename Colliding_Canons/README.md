# Colliding Canons

The question was asked in Codevita Examination 2017

## Problem Statement

We have seen in many mythological movies, the arrows shot, by the opponents collide mid-air and one devour the other.
You wanted to simulate a similar situation for the video game you are designing. In the game, the opponents are in a tunnel and have a gun each. They can shoot bullets in any direction (within limits). The roof and floor of the tunnel are perfect surfaces and any object hitting them are bounced off according to the law of reflection (angle of incidence equals the angle of reflection), with unchanged speed. For simplicity, we can assume that the tunnel is a two-dimensional horizontal strip. Of course, this being the mythological world, gravity does not exist, and the bullets travel in straight lines at constant speed until being reflected (or they collide).

The two guns are positioned at half the height ( h ) of the tunnel, at a distance ( D ) apart. The two guns fire simultaneously. The trajectories of the bullets ( if extended ) will meet at a maximum of one point. They are said to collide if their trajectories meet, and the two bullets arrive at that point within 0.5 seconds of each other.

## Explanation

From inputs provided by the user, we can find the coordinates of the guns. 

And based on provided angles by the user of the guns, we can find the angle of collision. 

By using, **Sine Rule** on the triangle formed between points a, b, and c we can find the hypotenuse1 and hypotenuse2. 

Now divide the triangle into two right-angled triangles, from the newly formed triangle we can find the coordinates of the point of collision and get the desired result.

### For more explaination look for image below

<a href="https://ibb.co/5KKCh0R"><img src="https://i.ibb.co/XYY6xQC/Be-Funky-design.jpg" alt="Be-Funky-design" border="0" /></a>

<br/>

```\Colliding_Canons> python Colliding_Canons.py```

```3000,700```

```60,120,56,130```

Output :

```Yes,27.164,559.169```
