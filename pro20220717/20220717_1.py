# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 15:44:01 2022

@author: mj031
"""
# ============================================================
# 시작 값과 끝값을 입력 받아서 그 구간의 합과 짝수 합, 홀수 합 출력하기
# =====================================================
# def test1():
#    start = int(input('시작 값 : '))
#    end = int(input('종료 값 : '))
#   sum_even = 0
#   sum_odd = 0
#   for value in range(start,end+1):
#       if value % 2 == 0:
#           sum_even += value
#       else:
#           sum_odd += value
#   print("짝수 합 : ",sum_even,"홀수 합 : ",sum_odd,"전체 합 : ",sum_even+sum_odd)
    
# test1()

# =========================================================================================


# ===================================================================================================
# 8~13:초등학생, 14~16:중학생, 17~19:고등학생,20~16:대학생, 27~:일반인
# 출생년도를 입력 받아서 어떤 학생인지 출력하세요
# ===================================================================================================

def test2():
    age = int(input("출생년도 : "))
    age = 2022 - age + 1
    
    if 8 <= age and age <= 13:
        print(age,':초등학생')
    elif 14 <= age and age <= 16:
        print(age,':중학생')
    elif 17 <= age and age <= 19:
        print(age,':고등학생')
    elif 20 <= age and age <= 26:
        print(age,':대학생')
    else:
        print(age,':일반인')


# test2()



# ===============================================================================
# 1~100 사이의 임의의 수를 발생시켜 맞추기, 몇번 만에 맞추는지 알려주기.
# ===============================================================================
import random
def test3():
    number = random.randint(1,100)
    count = 0
    while True:
        guess_number = int(input("추측한 숫자 : "))
        count += 1
        if number == guess_number:
            print('[',count,']','축하합니다! 정답입니다!')
            break
        elif number < guess_number:
            print('[',count,']','작은 수를 입력해주세요')
        elif number > guess_number:
            print('[',count,']','큰 수를 입력해주세요')
            
# test3()






# ===========================================================
# 원하는 구구단을 입력 받아서 출력
# ===========================================================
def gugudan(dan):
    for i in range(10):
        print(dan,' * ',i,' = ',dan*i)
def test4():
    while True:
       # dan = int(input("출력할 단[종료:q] : "))
        dan = input("출력할 단[종료:q] : ")
        if dan == 'q':
            print("### 구구단을 종료합니다 ###")
            break
        else:
            dan = int(dan)
            gugudan(dan)
    
    
    
# test4()



list_a = ['a','ab','abc']
for v in list_a:
    print(v)
    
for i in range(len(list_a)):
    print(i)

    
    
    
    
# ========================================================
# 로또 번호(1~45) 추첨기
# ========================================================
# def test5():
#     a = [1,2,5]
#     a.append(4)
    
#     print(a)
#     if 4 not in a:
#         print('존재하지 않습니다')
#     else:
#         print('존재합니다')
    
# test5()

def test5():
    lotto = []
    for v in range(6):
        value = random.randint(1,45)
        if value not in lotto:
            lotto.append(value)
    print('로또번호 : ',lotto)
    
    
    
# test5()


def test6():
    lotto = []
    while len(lotto) < 6:
        value = random.randint(1,6)
        if value not in lotto:
            lotto.append(value)
        
    print('로또번호 : ',lotto)
    
    
    
test6()
