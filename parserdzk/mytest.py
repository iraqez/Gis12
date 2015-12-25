from parserdzk import datacadnum

koatuu = '6810100000'

d = []

def cadnum(koatuu):
    for zona in ['{0:02d}'.format(i) for i in range(27,28)]:
        for kvartal in ['{0:03d}'.format(i) for i in range(1,3)]:
            for parcel in ['{0:04d}'.format(i) for i in range(1,50)]:
                d.append(str(koatuu+':'+zona+':'+kvartal+":"+parcel))

    for i in d:
        try:
            if datacadnum.cnum(i) != None:
                print(datacadnum.cnum(i))
            else:
                raise TypeError
        except TypeError:
            pass

if __name__ == '__main__':
    print(cadnum(koatuu))