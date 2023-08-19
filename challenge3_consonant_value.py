
def consonants(string):


    consonants = []

    alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for char in string:

        if char.lower() not in ['a', 'e', 'i', 'o', 'u',' '," "]:

            char2=alph.index(char)
            
            consonants.append(char2)



    print (max(consonants))      
    return max(consonants)
   
    
consonants('how are you')



