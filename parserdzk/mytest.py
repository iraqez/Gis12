from parserdzk import datacadnum

koatuu = '6810100000'

d = []

for zona in ['{0:02d}'.format(i) for i in range(1,20)]:
    for kvartal in ['{0:03d}'.format(i) for i in range(1,20)]:
        for parcel in ['{0:04d}'.format(i) for i in range(1,200)]:
            d.append(str(koatuu+':'+zona+':'+kvartal+":"+parcel))

for i in d:
    try:
        if datacadnum.cnum(i) != None:
            print(datacadnum.cnum(i))
        else:
            raise TypeError
    except TypeError:
        print('Нет данных по участку: ' + i)
        # pass