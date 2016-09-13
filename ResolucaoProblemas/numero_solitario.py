# -*- coding: utf-8 -*-

##################################################################
## Problema do número solitário - Resolução por Mauricio Borges ##
##################################################################

############################################################
# A solução encontrada para o problema do número solitário #
# foi a utilização de um Set que guardasse o valor em sua  #
# primeira incidência e o descartasse em sua segunda. Com  #
# isso, apenas o número solitário sobrará e será exposto   #
# na tela.                                                 #
############################################################

#############################################
#             Início do código              #
#############################################
                                            
size = input()

while(size != 0):
    readSet = set()
    txt = raw_input()
    vector = (int(x) for x in txt.split())
    for number in vector:
        if number in readSet:
            readSet.discard(number)
        else:
            readSet.add(number)
    for number in readSet:
        print(str(number))
    size = input()

#############################################
#               Fim do código               #
#############################################
