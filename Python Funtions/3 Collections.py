import collections

class Solution:
    def firstUniqChar(self, s="lleetcode") -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s) # learn collections package # counts how many times character repeates
        print(count) # Counter({'e': 3, 'l': 1, 't': 1, 'c': 1, 'o': 1, 'd': 1})

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1: # checking the values number in count
                print(" the index value",idx)
                return
        print(-1)
        return -1

obj=Solution()
obj.firstUniqChar()