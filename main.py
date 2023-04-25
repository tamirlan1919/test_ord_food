#Менеджер контекста - это объект который опред контекст выполнения в
# операторе with
from random import randint as rrr
import contextlib


import requests 
from bs4 import BeautifulSoup 
from datetime import datetime 



# оздайте функцию – контекст менеджер, которая будет получать на вход ID валюты и возвращать информацию о ней в виде:

# (1 шт.) Австралийский доллар стоит(ят) 49,2779 руб.

# Если такой валюты нет – ошибка должна обрабатываться и выводиться, что такая валюта не найдена.

# Для получения курса валют воспользуйтесь AP


import random

class Randomiter():
    def __init__(self,limit,):
        self.limit = limit
        self.__reload = limit

    def __iter__(self):
        self.limit = self.__reload
        return self
    def __next__(self):
        if self.limit==0:
            raise StopIteration

        self.limit-=2
        return random.randint(0,100)
    
raind_iter = Randomiter(10)

for rand in raind_iter:
    print(rand)
