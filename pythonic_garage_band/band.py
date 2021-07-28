from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod


class Band(ABC):
    created_Band = 0

    def __init__(self, name , members : list):
       self.name = name
       self.members = members
     
    def play_solos(self):
        return['face melting guitar solo',"bom bom buh bom","rattle boom crash"]    
    def __repr__(name):
        return 'Guitarist instance. Name = {}'.format(name)   
    def __str__ (name):
        return 'My name is {} and I play guitar'.format(name)   

    @classmethod
    def to_list (cls):
        if Band.created_Band == 0:
           Band.created_Band =+1
           return []
        else:
            return[Band.created_Band]
      


class Musician(Band):
    
    def __str__ (self):
           return 'My name is {} and I play bass'.format(self.name)    
    def __repr__(self):
           return 'Bassist instance. Name = {}'.format(self.name)  
    def get_instrument():
        pass
    def play_solos():
        pass   
    
class Guitarist(Musician):
        def __init__(self, name):
           self.name = name
        def __str__ (self):
           return 'My name is {} and I play guitar'.format(self.name)    
        def __repr__(self):
           return 'Guitarist instance. Name = {}'.format(self.name)
        def get_instrument(self):
           return "guitar"
        def play_solo(self):
            return  'face melting guitar solo'  
        
class Drummer(Musician):
        def __init__(self, name):
           self.name = name
        def __str__ (self):
           return 'My name is {} and I play drums'.format(self.name)    
        def __repr__(self):
           return 'Drummer instance. Name = {}'.format(self.name) 
        def get_instrument(self):
           return  "drums" 
        def play_solo(self):
           return  "rattle boom crash"         
       
class Bassist(Musician):
        def __init__(self, name):
           self.name = name   
        def get_instrument(self):
           return  "bass"
        def play_solo(self):
           return "bom bom buh bom"




