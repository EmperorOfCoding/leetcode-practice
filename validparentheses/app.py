class Solution(object):
    def isValid(self, s):

        hashmap = {

            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for char in s:

            if char in hashmap:
                stack.append(char)

            else:
                if not stack or hashmap[stack.pop()] != char:
                    return False


        return len(stack) == 0







solucao = Solution()
resultado = solucao.isValid('()[]')
print(resultado)


#limite: ()[]{}
#formatos válidos (), [], {}, ([{}])

#Os parenteses so sao validos quando fechados por ele mesmos (o inicio fecha o final
#Solucao: Verificar se o primeiro parenteses é igual ao ultimo parenteses (signifca que foi fechado pelo mesmo parenteses)


