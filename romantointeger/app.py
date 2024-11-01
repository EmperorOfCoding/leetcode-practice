class Solution(object):
    def romanToInt(self, s):

        soma = 0
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s) - 1):

            if hashmap[s[i]] < hashmap[s[i + 1]]:

                soma -= hashmap[s[i]]

            else:
                soma += hashmap[s[i]]

        soma += hashmap[s[-1]]

        return soma







#Vou armazenar um dicionario com as chaves (letras romanas) e seus respectivos valores
#A minha entrada vai ser uma string, tenho que iterar sobre cada valor da string e somar
#Quando uma letra de menor valor vem depois de uma letra de valor maior, somamos os valores
#Quando uma letra de menor valor vem antes de uma letra de maior valor, subtraimos os valores

#Excecao: MCMXCIV 

solucao = Solution()
resultado = solucao.romanToInt('MCMXCIV')
print(resultado)

 




#:type s: str
#:rtype: int
       
        