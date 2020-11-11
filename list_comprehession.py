# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 20:54:47 2019

@author: Lucas
"""

import numpy as np
x = np.random.randint(0,100,10)
print(x)
y = x[x%2==1]
print(y)