# -*- coding: utf-8 -*-

from parserdzk import datacadnum

koatuu = "6821282200"



def cadnum(koatuu):
    nums = []

    notnum = 0
    zones = iter('{0:02d}'.format(i) for i in range(1,100))
    kvartals = iter('{0:03d}'.format(i) for i in range(1,10))
    parcels = iter('{0:04d}'.format(i) for i in range(1,10))

    for zona in zones:
        for kvartal in kvartals:
            for parcel in parcels:
                cn = [koatuu,zona,kvartal,parcel]
                nums.append(":".join(cn))

    for i in nums:
        try:
            if datacadnum.cnum(i) != None:
                print(datacadnum.cnum(i))
                notnum = 0
            else:
                raise TypeError
        except TypeError:
            if notnum < 10:
                notnum = notnum + 1
            else:
                print(notnum)

if __name__ == '__main__':
    cadnum(koatuu)