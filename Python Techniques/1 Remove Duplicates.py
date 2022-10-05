class Solution:
    def removeDuplicates(self, l1=[1, 1, 2,3,3,4]):
        l2=list(dict.fromkeys(l1))
        print(l2)

obj = Solution()
obj.removeDuplicates()

###### Reverse a string #### start:stop:step
print("apple" [::-1]) #elppa

print([2, 33, 222, 14, 25][:-1]); # [2, 33, 222, 14]

#### Generator Concept ###
my_list = [2, 4, 9, 14, 17]
value = sum(x**2 for x in my_list)
print(value) # 586 -> which is square of all the numbers added together