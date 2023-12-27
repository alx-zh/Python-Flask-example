
import os 

#11. Дескрипторы (data descriptor и non-data descriptor) | ООП Python

class integer:

    @classmethod
    def verify_coord(cls,value):
        if type(value) != int:
            raise TypeError("Координата должна быть целым числои")
    
    def __set_name__(self,owner,name):
        self.name = "_"+name

    def __get__(self,instance,owner):
        return isinstance.__dict__(self.name)
    
    def __set__(self,instance,value):
        self.verify_coord(value)
        print(f"__set__:{self.name} = {value}")
        instance.__dict__[self.name] = value

    

class Point3d:
    x = integer()
    y = integer()
    z = integer()

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    
#---------------
os.system('clear')

p = Point3d(1,2,3)

p.y = '5'

print(p.__dict__)

print("- - - finish - - -")
        

