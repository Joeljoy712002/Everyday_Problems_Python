class Solution(object):
    def lengthOfLastWord(self, s):
      
        words = s.split()
        last_element = words[-1]

        return len(last_element)