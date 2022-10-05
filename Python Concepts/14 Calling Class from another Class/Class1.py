
class Display:

    def __init__(self):
        self.var1 = 1
        self.var2 = 2
    # Public Method
    def displayText(self,x,y):
        print("Geeks 1 Geeks !")
        print(x+y)
        z=10

    # Protected Method
    def _displayText2(self):
        print("Geeks 2 Geeks !")

    # Private Method
    def __displayText3(self):
        print("Geeks 3 Geeks !")

# class Display2(Display): # Child Class
#
#     def __init__(self):
#         super().__init__() # this will import variables of parent class to child class
#
#     def apple(self):
#         print("var1", self.var1)
#         print("var2", self.var2)
#         obj.displayText() # Calling Def from Parent Class
#         obj._displayText2()  # Calling protected Def from Parent Class-> Executes
#         # obj.__displayText()  # Calling private Def from Parent Class-> Not executes
#
# obj = Display2()
# obj.apple()







