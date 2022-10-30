class Solution:
    def isPalindrome(self,x=121):
        if x < 0: return False # Base condition
        number = x  # Store the number in a variable
        reverse = 0  # This will store the reverse of the number
        while number:
            ###### Main Logic  ###
            reverse = reverse * 10 + number % 10 ##
            number //= 10

        print(x == reverse) # this is bolean expression prints true of false
        return

obj = Solution()
obj.isPalindrome()