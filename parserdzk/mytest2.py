# -*- coding: utf-8 -*-

from itertools import product
from parserdzk import datacadnum

koatuu = '6821282200'

def cadnum(koatuu):
    notnum = 0 #лічильник неіснуючих ділянок підряд
    cnums = [] #список існуючих ділянок в КОАТУУ
    # zones = iter(['{0:02d}'.format(i) for i in range(1,5)])
    # kvartals = iter(['{0:03d}'.format(i) for i in range(1, 10)])
    # parcels = iter(['{0:04d}'.format(i) for i in range(1,20)])

#Парсинг зоны
    for zona in range(1,100):
        for kvartal, parcel in product(range(1,1000),range(1,10000)):
            cn = ':'.join([str(koatuu),'{0:02d}'.format(zona),'{0:03d}'.format(kvartal),'{0:04d}'.format(parcel)])
            if datacadnum.cnum(cn) != None:
                print('Зона: ' + '{0:02d}'.format(zona) + ' для КОАТУУ: ' + koatuu)
                notnum = 0
                break

            else:
                if notnum < 10:
                    notnum += 1
                    continue
                else:
                    print('Нет зоны: ' + '{0:02d}'.format(zona) + ' для КОАТУУ: ' + koatuu)
                    notnum=0
                    break




    # return cnums

if __name__ == '__main__':
    cadnum(koatuu)