
# import re
# solve = lambda s : max([sum([ord(letter)-ord('a')+1 for letter in consOnly]) for consOnly in re.split("a|e|i|o|u",s)])

# print(solve("hello")) # output : 26
# print(solve("chruschtschov")) # output : 80
# print(solve("rhythm")) # output : 92

def consonants(string):

    consonants = []
    consonants2 = []


    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in string:

        if char.lower() not in ['a', 'e', 'i', 'o', 'u',' '," "]:

            char2=alph.index(char)+1           

            consonants.append(char2)

        else:
            Sum = sum(consonants)
            consonants = []
            consonants2.append(Sum)

        Sum2 = sum(consonants)
        consonants2.append(Sum2)
        


    print (max(consonants2))    
   
    return max(consonants2)
   
    
consonants('strength')

