#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:52:49 2024

@author: stephenson
"""

import math
x = 3.1;
y = 1.0 - x;

print("This evalues to ", math.fabs(y))
#1 evaluated to 2.1 returns the absolute val of a num, as a float

print("This evalues to ", math.floor(x))
#2 evaluates to 3. this particular method rounds a number DOWN to the nearest integer.
print("This evalues to ", math.ceil(x))
#this evaluates to 4. rounds up to nearest int
print("This evaluates to", math.floor(y))
#this evaluates to -3 this, obviously then must round down to nearest int
print("This evalues to", math.ceil(y))
#this evaluates to -2, and again, here it must again round up