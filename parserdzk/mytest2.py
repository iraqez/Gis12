# -*- coding: utf-8 -*-

from parserdzk import datacadnum

koatuu = '6810100000'



def cadnum(koatuu):
    nums = []
    notnum = 0
    cnums = []

    for zona in ['{0:02d}'.format(i) for i in range(1,3)]:
        for kvartal in ['{0:03d}'.format(i) for i in range(1,3)]:
            for parcel in ['{0:04d}'.format(i) for i in range(1,10)]:
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
            notnum += 1
            print(notnum)

    return cnums

if __name__ == '__main__':
    cadnum(koatuu)