from parserdzk import datacadnum

koatuu = '6810100000'



def cadnum(koatuu):
    nums = []
    zonakvart = []

    notnum = 0
    zones = ['{0:02d}'.format(i) for i in range(1,100)]
    kvartals = ['{0:03d}'.format(i) for i in range(1,1000)]
    parcels = ['{0:04d}'.format(i) for i in range(1,10)]

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
                kvartal._get_next_or_previous_in_order()
 #               kvartal = kvartal + 1

            print(notnum)

if __name__ == '__main__':
    print(cadnum(koatuu))