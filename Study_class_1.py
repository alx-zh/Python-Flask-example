

from string import ascii_letters

#10. Пример использования объектов property 
#Объектно-ориентированное программирование Python

class Person:

    s_rus = 'йцукенгшщзхъёфывапролджэячсмить-'
    s_rus_upper = s_rus.upper()

    def __init__(self, fio, old, ps, weight):
        self.verify_fio(fio)
        self.verify_age(old)
        self.verify_ps(ps)
        self.verify_w(weight)


        self.__fio = fio.split() 
        self.__old = old
        self.__ps = ps
        self.__weight = weight
    """
    def get_fio(self):
        return self.__fio
    """
    @classmethod 
    def verify_fio(cls, fio):
        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")
        
        f = fio.split()

        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ascii_letters + cls.s_rus + cls.s_rus_upper

        for s in f:
            if len(s) <1:
                raise TypeError("ФИО должно содержать символы")
            
            if len(s.strip(letters)) != 0:
                raise TypeError("ФИО должно содержать допустимые символы и дефис")

    @classmethod 
    def verify_age(cls, old):
        if type(old) not in (int,float):
            raise TypeError("Возраст должен быть вещественным числом")

        if old < 14 or old > 120:
            raise TypeError("Возраст должен быть указан в диапазоне [14; 120]")

    @classmethod    
    def verify_w(cls, w):
        if type(w) not in (int,float) or w < 20:
            raise TypeError("Вес должен быть вещественным числом и быть не меньше 20")

    @classmethod         
    def verify_ps(cls, ps):
        if type(ps) != str:
            raise TypeError("Паспорт должен быть указан строкой")
        
        p = ps.split()
        
        if len(p) != 2:
            raise TypeError("Неверный формат паспорта")

        for s in p:
            if not s.isdigit():
                raise TypeError("Паспорт должен быть указан цифрами")
    
    #FIO
    @property 
    def fio(self):
        return self.__fio
    
    #WGHT
    @property 
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self,weight):
        self.verify_w(weight)
        self.__weight = weight

    #OLD
    @property 
    def old(self):
        return self.__old
    
    @old.setter
    def old(self,old):
        self.verify_age(old)
        self.__old = old

    #PS
    @property 
    def ps(self):
        return self.__ps
    
    @ps.setter
    def ps(self,ps):
        self.verify_ps(ps)
        self.__ps = ps
    


#----------------

p = Person('Соколов Сергей Иванович', 20,'1234 567890', 60)



p.old = 100
p.weight = 80 
p.ps = '4321 123456'

p.doc = 'document'

print(p.fio)
print(p.old)
print(p.ps)

print( p.__dict__)

print(" -- finish -- ")





        




