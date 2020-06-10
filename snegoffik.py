#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

from solid import *
from solid.objects import *
from solid.utils import *

SEGMENTS = 48

"""
Напоминалка: смотрим y - от нас (back-front),
z - вверх (up-down), x - вправо (right-left)
Порядок упоминания - x,y,z

"""

def snegg():
    
    larg = color(White)(sphere(30))
    midl = color(White)(up(40)(sphere(22)))
    smal = color(White)(up(70)(sphere(17)))
    nos = color(Red)(
        translate((0, 16, 70))(
            rotate(-90, [1, 0, 0])(
                cylinder(r1=4, r2=0.5, h = 14)
            )
        )
    )
    glaz1 = color(Black)(translate((-10, 10, 80))(sphere(1)))
    glaz2 = color(Black)(translate((10, 10, 80))(sphere(1)))
    
    ruka1 = color(White)(translate((-25, 0, 40))(sphere(6)))
    ruka2 = color(White)(translate((25, 0, 40))(sphere(6)))

    flig = translate((25, 0, 40))(
        color(White)((cylinder(r=0.5, h=20) + up(20)(cube([10, 0.5, 6], center=False)))))
    kr = translate((30,0.5,63))(
            color(Red)(rotate(90, [1, 0, 0])(circle(2.5))))
    
    snegovik = union()(larg, midl, smal, nos, glaz1, glaz2, ruka1, ruka2, flig, kr)

    return snegovik

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None

    file_out = scad_render_to_file(snegg(), out_dir=out_dir)
    print(f" SCAD file written to: \n{file_out}")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




