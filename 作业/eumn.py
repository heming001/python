# -*- coding: utf-8 -*-
from enum import Enum, unique


class Student(Enum):
    pass
    
    
bart = Student('Bart', Gender.Male)
print(bart.gender)