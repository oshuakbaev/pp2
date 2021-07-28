class Solution:
    def largestAltitude(self, gain:List[int])->int:
    a = 0
    h = 0 
    for i in range(len(gain)):
        a+=gain[i]
        if h < a:
            h = a 
    return h
    