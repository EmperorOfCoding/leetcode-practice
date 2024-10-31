class Solution(object): #hashMap
    def twoSum(self, nums, target):

        hashmap = {}

        for i, num in enumerate(nums):

            diff = target - num

            if diff in hashmap:

                return [hashmap[diff], i]
            
            hashmap[num] = i
            




solucao = Solution()
resultado = solucao.twoSum([2, 4, 5, 7, 5], 6)
print(resultado)

#nums = [2, 7, 11, 15]
#target = 9













