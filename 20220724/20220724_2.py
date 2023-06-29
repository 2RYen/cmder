# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 16:48:12 2022

@author: mj031
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def do_eat(self):
        print(self.name,"이 밥을 먹는다.")
        
class Employee(Person):
    def __init__(self, name, age, salary, hire_date):
        super().__init__(name, age)
        self.salary = salary
        self.hire_date = hire_date
        
    def do_work(self):
        print(self.name,"가 열심히 일을 한다.")
    
    def get_info(self):
        print("이름 :",self.name,", 급여:",self.salary,", 입사일:",self.hire_date)
        
person = Person('홍길동',28)
person.do_eat()

employee = Employee('최수지',22,2000000,'20220501')
employee.do_eat()
employee.do_work()
employee.get_info()

    