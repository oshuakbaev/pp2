class Solution:
    address = input()
    def defangIPaddr(self, address):
        self.address =address.replace(".","[.]")
        return self.address
    def my_funct(self):
        print(self.address)

ans = Solution()
print(ans.my_funct())
