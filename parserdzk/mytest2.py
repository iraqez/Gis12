# -*- coding: utf-8 -*-

from parserdzk import datacadnum

koatuu = "681010000"



def cadnum(koatuu):
    nums = [] #номера кадастрових ділянок
    notnum = 0 #лічильник неіснуючих ділянок підряд
    cnums = [] #список існуючих ділянок в КОАТУУ

    for zona in ['{0:02d}'.format(i) for i in range(1,3)]:
        for kvartal in iter(['{0:03d}'.format(i) for i in range(1,3)]):
            for parcel in iter(['{0:04d}'.format(i) for i in range(1,10)]):
                cn = [koatuu,zona,kvartal,parcel]
                nums.append(":".join(cn))

    for i in nums:
        try:
            if datacadnum.cnum(i) != None:
                cnums.append(datacadnum.cnum(i))
                print(datacadnum.cnum(i))

                notnum = 0
            else:
                raise TypeError
        except TypeError:
            if notnum < 20:
                notnum += 1
                print(notnum)
            else:
                pass
                # next(kvartal)

    return cnums

if __name__ == '__main__':
    cadnum(koatuu)