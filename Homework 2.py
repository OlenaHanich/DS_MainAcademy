# -*- coding: utf-8 -*-

# -- Sheet --

import math
height = [185, 185, 176, 171, 163, 186, 186, 170, 192, 174]
i = 0
sum = 0
while i<len(height):
    sum += height[i]
    i += 1
mean_height = sum / len(height)
print ('Середній зріст в групі', mean_height)
n=0
p=0
while n<len(height):
    p += (height[n] - mean_height)**2
    n += 1
std=math.sqrt(p/len(height))
print ('Cтандартне відхилення дорівнює', std)
list.sort(height)
if len(height)%2 == 0:
    median_height = (height[int(len(height)/2)]+height[int(len(height)/2-1)])/2
else:
    median_height = height[int(len(height)/2)]
print('Медіанне значення дорівнює',median_height)    


height = [185, 185, 176, 171, 163, 186, 186, 170, 192, 174]
import statistics
import numpy
a = statistics.mean(height)
b = statistics.median(height)
c = numpy.std(height)
print('Середнє значення дорівнює', a,'Медіана дорівнює', b,'Стандартне відхилення дорівнює',c)

