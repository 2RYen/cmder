# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 17:05:30 2022

@author: mj031
"""

# =============================================================================
# Calculator
# =============================================================================
class Calculator:
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2
    
    def add(self,operand1=None,operand2=None):
        if operand1 == None:
            return self.operand1 + self.operand2
        else:
            return operand1 + operand2
        
    
    def sub(self):
        return self.operand1 - self.operand2
    
    def mul(self):
        return self.operand1 * self.operand2
    
    def div(self):
        if self.operand2 != 0:
            return self.operand1 / self.operand2
        else:
            return None
    
cal = Calculator(10,0)
print("덧셈 :",cal.add())
print("덧셈 :",cal.add(20,40))
print("뺄셈 :",cal.sub())
print("곱셈 :",cal.mul())
print("나눗셈 :",cal.div())