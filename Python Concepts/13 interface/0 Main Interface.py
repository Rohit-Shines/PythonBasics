from abc import *
class DBInterface(ABC): # this is an interface
   @abstractmethod
   def connect(self):
       pass
   @abstractmethod
   def disconnect(self):
       pass
