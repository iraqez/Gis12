# -*- coding: utf-8 -*-

from parserdzk import datacadnum

koatuu = '6810100000'



def cadnum(koatuu):
    d = []
    for zona in ['{0:02d}'.format(i) for i in range(100)]:
        for kvartal in ['{0:03d}'.format(i) for i in range(1000)]:
            for parcel in ['{0:04d}'.format(i) for i in range(10000)]:
                d.append(str(koatuu+':'+zona+':'+kvartal+":"+parcel))

    # for i in d:
    #     try:
    #         if datacadnum.cnum(i) != None:
    #             print(datacadnum.cnum(i))
    #         else:
    #             raise TypeError
    #     except TypeError:
    #         continue

if __name__ == '__main__':
    print(cadnum(koatuu))