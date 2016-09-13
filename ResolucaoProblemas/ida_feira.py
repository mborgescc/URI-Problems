# -*- coding: utf-8 -*-

#############################################################
## Problema da Ida à feira - Resolução por Mauricio Borges ##
#############################################################

##############################################################
# A solução encontrada para o problema da ida à feira foi a  #
# utilização de um "dicionário" (dict) para armazenar o nome #
# das frutas e legumes e associá-los a um valor              #
##############################################################

#############################################
#             Início do código              #
#############################################

offeredFruits = {}                                         
numberOfTimes = input()

for _ in range(numberOfTimes):
    totalValue = 0
    offeredQuantity = input()
    for _ in range(offeredQuantity):
        info = raw_input().split()
        offeredFruits[info[0]] = float(info[1])
    thingsToBuy = input()
    for _ in range(thingsToBuy):
        info = raw_input().split()
        totalValue += offeredFruits[info[0]]*int(info[1])
    print("R$ %.2f" % totalValue)

#############################################
#               Fim do código               #
#############################################
