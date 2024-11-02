class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            print("")

        prefix = strs[0]

        for i in range(1, len(strs)):

            while not strs[i].startswith(prefix):

                prefix = prefix[:-1]

                if not prefix:
                    print("")

        return prefix


            

solucao = Solution()
resultado = solucao.longestCommonPrefix(['map', 'mop', 'map'])
print(resultado)
#1 - Pegar os digitos da palavra toda

        











