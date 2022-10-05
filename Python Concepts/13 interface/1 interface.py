from abc import *
class DBInterface(ABC): # this is an interface
   @abstractmethod
   def connect(self):
       pass
   @abstractmethod
   def disconnect(self):
       pass

class Bank(ABC):
   @abstractmethod # abstract An abstract method is a method that is declared without an implementation (without braces, and followed by a semicolon),
   def balance_check(self):
       pass
   @abstractmethod
   def interest(self):
       pass

class SBI(Bank):
   def balance_check(self):
       print("Balance is 100 rupees")
   def interest(self):
       print("SBI interest is 5 rupees")


s = SBI()
s.balance_check()
s.interest()