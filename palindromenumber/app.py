class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False
        
        elif x == 0:
            return True
        
        else:

            digitos_normais = [int(digito) for digito in str(x)]
            print(digitos_normais)

            digitos_invertidos = [int(digito) for digito in str(x)[x::-1]]
            print(digitos_invertidos)

            if digitos_normais == digitos_invertidos:

                return True
            
            else:
                return False



#Se o numero for negativo nao pode ser palindromo
#Vou pegar o numero 121
#Vou pegar o numero ao contrário
#E vou comparar se os 2 sao iguais

solucao = Solution()
resultado = solucao.isPalindrome(656)
print(resultado)



















