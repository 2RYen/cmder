# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 15:16:03 2022

@author: mj031
"""

# ==========================================================
# Circle class
# - 속성: radius
# - 메소드: get_circumference(), get_area()
# ==========================================================
import math
class Circle:
    def __init__(self, radius2):
        self.radius2 = radius2
    
    def get_circumference(self):
        return 2 * math.pi * self.radius2
    
    def get_area(self):
        return math.pi * self.radius2    # **2
    
circle1 = Circle(10)
circle2 = Circle(20)
print("원의 넓이 :",circle1.get_area())
print("원의 둘레 :",circle1.get_circumference())