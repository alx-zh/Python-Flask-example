"""
метод __call__. Функторы и классы-декораторы | ООП Python
"""

import os 

from typing import Any


class Counter:
    def __init__(self) -> None:
        self.__counter = 0

    def __call__(self, step = 1, *args: Any, **kwds: Any) -> Any:
        print ("__call__")
        self.__counter += step
        return self.__counter

#--------------------

os.system('clear')

c = Counter()
c() # +1
c(3) # +3 = 4
c2 = Counter()
res1 =  c() # +1
res2 = c2(-2) # -2 

print (res1 , res2)


