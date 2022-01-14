### reduce、itertools 的用法 ###

# import itertools
# from functools import reduce
#
# func = (lambda x, y: x + y)
# value = [1, 2, 3]
# print(reduce(func, value))
# print(list(itertools.accumulate(value, func)))


##    1. 定義一匿名函數 分別有 ( x,y )兩參數，請使用函數來計算 (3,4)
##       與 (0,0)的距離 及 (5,12) 與 (0,0)的距離
#
# import math
#
# x = 3
# y = 4
# # x = 5
# # y = 12
#
# func = (lambda x, y: math.sqrt(pow(x, 2) + pow(y, 2)))
#
# print(func(x, y))


# ##    2. 有三個List 分別為 5位選手的第一、二、三次試跑成績，請使用
# ##       map Function計算5位選手三次試跑成績，並取小數點後兩位
#
# score1_List = [12.07, 11.89, 12.05, 11.67, 11.91]
# score2_List = [11.87, 11.96, 12.01, 12.00, 11.95]
# score3_List = [11.83, 11.81, 11.93, 11.93, 11.84]
#
#
# def adder(x, y, z):
#     return round((x + y + z) / 3, 2)
#
#
# print(list(map(adder, score1_List, score2_List, score3_List)))

##    3. 加入 Player_List 並根據第2題的結果呈現每位選手平均成績

# Player_List = [f'{i}號選手成績 : ' for i in range(1, 6)]
# score1_List = [12.07, 11.89, 12.05, 11.67, 11.91]
# score2_List = [11.87, 11.96, 12.01, 12.00, 11.95]
# score3_List = [11.83, 11.81, 11.93, 11.93, 11.84]
#
#
# def adder(id, x, y, z):
#     return str(id), str(round((x + y + z) / 3, 2))
#
#
# print(list(map(adder, Player_List, score1_List, score2_List, score3_List)))

## 4. 使用 Reduce Function 計算 CS_Class , Stat_Class , Eng_Class 分數總和
##    並計算三個Class 分數的平均
#
# from functools import reduce
#
# CS_Class = [68, 76, 84, 53, 81]
# Stat_Class = [71, 70, 93, 62, 68]
# Eng_Class = [85, 96, 98, 88, 93]
#
# func = (lambda x, y: x + y)
# accumulate_1 = reduce(func, CS_Class)
# mean_1 = (accumulate_1) / len(CS_Class)
# print(mean_1)
#
# accumulate_2 = reduce(func, Stat_Class)
# mean_2 = (accumulate_2) / len(Stat_Class)
# print(mean_2)
#
# accumulate_3 = reduce(func, Eng_Class)
# mean_3 = (accumulate_3) / len(Eng_Class)
# print(mean_3)
#
#
# def accumlute(list_1, list_2, list_3)


# 以下為裝飾器的用法
def Login_Decorator(callback):
    def inner_func():
        account = input('請輸入帳號:')
        password = input('請輸入密碼:')
        callback(account, password)

    return inner_func


# @Login_Decorator
# def IG_Web(account, password):
#     if account == 'root' and password == 'P@ssword':
#         print('Login Success')
#     else:
#         print('Login Fail')
#
#
# IG_Web()

class Login:

    def __init__(self, account, password):
        self.account = account
        self.password = password

    def login(self):
        print(f'Account : {self.account}', f'Password : {self.password}')


## 子類別
class FacebookLogin(Login):

    def __init__(self, account, password):
        super().__init__(account, password)

    def login(self):
        print(f'Account : {self.account}',
              f'Password : {self.password}'
              f'Password : {self.password}')
        print("Facebook login Success.")


class LineLogin(Login):

    def __init__(self, account, password, email):
        super().__init__(account, password)
        self.email = email

    def login(self):
        print(f'Account : {self.account}',
              f'Password : {self.password}',
              f'E-mail : {self.email}')
        print("Facebook login Success.")


fb = FacebookLogin(account='fb_account', password='fb_password')
fb.login()
print('==' * 10)
line = LineLogin(account='line_account', password='line_password', email='test@gmail.com')
line.login()
