# -*- coding: utf-8 -*-

from parserdzk import datacadnum

koatuu = "6821282200"



def cadnum(koatuu):
 #   nums = [] #номера кадастрових ділянок
    notnum = 0 #лічильник неіснуючих ділянок підряд
    cnums = [] #список існуючих ділянок в КОАТУУ
    kvartals = iter(['{0:03d}'.format(i) for i in range(1,3)])

    for zona in ['{0:02d}'.format(i) for i in range(1,3)]:
        for kvartal in kvartals:
            for parcel in iter(['{0:04d}'.format(i) for i in range(1,20)]):
                # cn = [koatuu,zona,kvartal,parcel]
                cc = ":".join([koatuu,zona,kvartal,parcel])
                try:
                    if datacadnum.cnum(cc) != None:
                        cnums.append(datacadnum.cnum(cc))
                        print(datacadnum.cnum(cc))
                        print()

                        notnum = 0
                    else:
                        raise TypeError
                except TypeError:
                    if notnum < 3:
                        notnum += 1
                        print(notnum)
                    else:
                        pass

    return cnums

if __name__ == '__main__':
    cadnum(koatuu)