

class Band():
    instances = []

    def __init__(self, name , members ):
       self.name = name
       self.members = members
       Band.instances.append(self.name)
     
    def play_solos(self):
       solo_list = []
       for member in self.members:
          solo_list.append(member.play_solo())
       return solo_list 
       
    def __str__ (self):
         return '{}'.format(self.name)  
    
    def __repr__(self):
         return '{}'.format(self.name)  

     
    @classmethod
    def to_list(cls):
       return cls.instances
      

class Musician():
   
    def __init__(self,name):
            self.name= name

    def __str__ (self):
           return 'My name is {} and I play {}'.format(self.name,self.get_instrument())    
    def __repr__(self):
           return '{} instance. Name = {}'.format(self.__class__.__name__,self.name)  

    def get_instrument(self):
      return '{}'.format(self.name)
    
    def play_solo(self):
      return '{}'.format(self.name)
    

class Guitarist(Musician):

   def get_instrument(self):
      return "guitar"
   def play_solo(self):
      return  'face melting guitar solo'  
        
class Drummer(Musician):

   def get_instrument(self):
      return  "drums" 
   def play_solo(self):
      return  "rattle boom crash"         
       
class Bassist(Musician):
   def get_instrument(self):
      return  "bass"
   def play_solo(self):
      return "bom bom buh bom"




if __name__ == '__main__':
   print('work')
   Band('x',[1,2,3])
   print(Band.play_solos())
   
