from parserdzk import datacadnum

koatuu = 6810100000

d = []

for i in ['{0:04d}'.format(i) for i in range(1,1000)]:
    d.append('6810100000:11:003:'+i)


# d = [
#     '6810100000:11:003:0101',
#     '6810100000:11:003:0102',
#     '6810100000:11:003:0103',
#     '6810100000:11:003:0104',
#     '6810100000:11:003:0105',
#     '6810100000:11:003:0106',
#     '6810100000:11:003:0107',
#     '6810100000:11:003:0108',
#     '6810100000:11:003:0109',
#     '6810100000:11:003:0110',
# ]



for i in d:
    try:
        if datacadnum.cnum(i) != None:
            print(datacadnum.cnum(i))
        else:
            raise TypeError
    except TypeError:
        pass
#
# d = [x+1 for x in d]
#
# lst = ['{0:04d}'.format(i) for i in range(1,10000)]