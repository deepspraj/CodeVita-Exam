 ##
 # @author Deepak Prajapati
 # @email deepprajapati01@gmail.com
 # @create date 2020-07-04 13:05:06
 # @modify date 2020-07-04 13:05:06
 ##

import os
import math

def ans_calculator (h,d,la,ls,ra,rs):
    angle3 = (180 - la - ra)
    angle3 = math.radians(angle3)
    la = math.radians(la)
    ra = math.radians(ra)
    
    hypo1 = (d * math.sin(ra) / math.sin(angle3))
    hypo2 = (d * math.sin(la) / math.sin(angle3))
    velo1 = (hypo1/ls)
    velo2 = (hypo2/rs)

    isit = 'No'
    if(abs(velo1-velo2)<=0.5):
        isit = 'Yes'
        
    yint = (hypo2*math.sin(ra))
    
    if (yint>int(h/2)):
        y = abs(yint - h)
    else:
        y = yint
    temp = pow(hypo2,2) - pow(yint,2)
    x = math.sqrt(temp)
    
    if(x<(d/2)):
        x = (d/2) - x
    else:
        x= x - (d/2)
    if(isit == 'Yes'):
        ans = isit + ',' + str(round(x,3)) + ',' + str(round(y,3))
    else:
        ans = isit
    print(ans)
h , d = map(int, input().split(','))
la, ls, ra, rs = map(int, input().split(','))

if((-85<=la<=85) and (-85<=ra<=85) and (0<ls<1000) and (0<rs<1000) and (0<h<10000) and (0<d<10000)):
    ans_calculator ( h, d,la, ls, ra, rs)
    os.system('Pause')
else:
    exit()