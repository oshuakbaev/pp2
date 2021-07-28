class Solution:
    
    def subtractProductAndSum(self, n: int)->int:
        sum = 0 
        pr_dig = 1
        s = str(n)
        for i in s: 
            sum += int(i)
            pr_dig *= int(i)
        res = pr_dig - sum
        return res 
            
        