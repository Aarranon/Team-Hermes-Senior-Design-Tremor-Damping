# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:25:28 2020

@author: Aarranon
"""

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(-10, 10, 2**10);

F_sat = 20; 
#motor saturation force, 
#force at which the motor will no longer increase it's torque 
#with increasing voltage across terminals

k_torque = 2;
#motor constant, converted to units of force

cutoff = 5.217;
#cutoff for actuator, from motor max force\

margin = 0.1;
#margin to add to the cutoff, in newtons



cutoff = cutoff + margin;
#add a bit of margin for actuator to actually work
#based on friction and such


y_mot = F_sat/(1+math.e**-(x/k_torque))-F_sat/2;
y_act = (cutoff*2)/(1+math.e**-((F_sat/(10*k_torque))*(x)))-(cutoff*2)/2;







fig = plt.figure();
ax = fig.add_subplot(1,1,1);
ax.spines['left'].set_position('center');
ax.spines['bottom'].set_position('zero');
ax.spines['right'].set_color('none');
ax.spines['top'].set_color('none');
ax.xaxis.set_ticks_position('bottom');
ax.yaxis.set_ticks_position('left');

plt.plot(x, y_mot, 'r', label='Motor Force Curve \n(derived from torque curve)');
plt.plot(x, y_act, 'b', label='Actuator Curve \n(limitations set from data)');
plt.legend(loc='upper left');
plt.show();
